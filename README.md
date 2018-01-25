# bdd-framework
A Django2+, Py3.6+, Selenium3+ pattern framework to easily setup BDD tests,
using 
[behave](https://github.com/behave/behave),
[behave-django](https://github.com/behave/behave-django),
and [splinter](https://github.com/cobrateam/splinter).

## Install
In a Python 3.6, Django 2+ environment, install the following packages:

```shell
pip install behave behave-django selenium splinter
```

### Behave

*If you have some behave related errors try to install it from Github as explained in the [behave documentations](http://behave.readthedocs.io/en/latest/install.html#using-the-github-repository).*

Run the following command to install the newest version from the Github repository:

```shell
pip install git+https://github.com/behave/behave
```
or (faster option)
```shell
pip install https://github.com/behave/behave/archive/master.zip#egg=behave
```

## Configuration
Create a `behave.ini` file in the Django project root directory containing to
indicate the paths to the testing directories (or the `feature` directory
inside of them), e.g.:
```ini
[behave]
paths = tests/bdd/
        myapp/tests/bdd/
        myotherapp/tests/bdd/
```

#### Django Settings
In order for the tests to locate your project static files, it is important to
correctly set the `STATICFILES_DIRS`, e.g.:

```python
STATICFILES_DIRS = (
    os.path.abspath('static'),
)
```

In order to define the default browser for Selenium testing, set
`BDD_DEFAULT_BROWSER` to either `'chrome'` (the default) or `'firefox'`.
To enable headless testing (PhantomJS is deprecated), set
`BDD_HEADLESS_BRWOSER` to `True` (default is `False`).

**Tips**
Do not forget to include `behave_django` among the installed apps:

```python
INSTALLED_APPS += ('behave_django',)
```

## Testing
Inside each BDD testing directory, test files should be created according to
the following structure (the `steps` directory is often found
inside the `feature` directory):
```shell
bdd/
    __init__.py
    features/
        myfeature.feature
    pages/
        __init__.py
        mypage.py
    steps/
        __init__.py
        mysteps.py
```

### 1. Features
Define BDD features written in
[Gherkin](https://github.com/cucumber/cucumber/wiki/Gherkin)
in `.feature` files inside a directory named `features`. In case a web UI test
is performed, the Chrome browser is used by default, nonetheless this can be
changed decorating a certain Scenario with `@browser.firefox` or
`@browser.phantomjs`.

**Tips**
Features and scenarios can be tagged as described
[here](
https://pythonhosted.org/behave/tutorial.html#controlling-things-with-tags
), this allows running only a specific subset of tests (e.g. those related to a
given user story).

### 2. Steps
Implement each step defined in the feature files, in Python files inside the
`steps` directory. Use `behave` decorators: `given`, `when` and `then` (`and`
and `but` steps should be decorated as the preceding main step).

### 3. Pages (Optional)
In case a web UI is being tested, it is useful to define page objects tailored
on specific web pages. `splinter` is used to provide basic interaction with the
pages and lets the user choose which `selenium` driver (e.g. Chrome, Firefox or
PhantomJS) to use. Each page class should be defined in Python files inside the
`pages` directory and should inherit from the `BasePage` class found in
`pages/base.py`. Each page is independent and might be instantiated with a
different driver. The tools provided by `splinter` are accessible (and
extendable) via `self.browser` (e.g. it might be convenient to define locators
as the logo one in the smaple project).

## Resources
* [behave documentation](https://behave.readthedocs.io/en/latest/index.html)
* [behave-django documentation](
    https://behave-django.readthedocs.io/en/latest/
)
* [splinter documentation](https://splinter.readthedocs.io/en/latest/)
