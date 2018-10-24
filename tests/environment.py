"""Define BDD environment."""
from django.conf import settings
from pkg_resources import load_entry_point
from splinter import Browser
from splinter.driver.webdriver.chrome import Options


def before_scenario(context, scenario):
    """Prepare context for scenario."""
    if 'browser.firefox' in scenario.tags:
        driver_name = 'firefox'
    elif 'browser.chrome' in scenario.tags:
        driver_name = 'chrome'
    else:
        driver_name = getattr(settings, 'BDD_DEFAULT_BROWSER', 'chrome')
    params = {
        'driver_name': driver_name,
        'headless': getattr(settings, 'BDD_HEADLESS_BROWSER', False),
        'incognito': getattr(settings, 'BDD_INCOGNITO_BROWSER', False),
        'wait_time': getattr(settings, 'BDD_DEFAULT_WAIT_TIME', 5),
        'fullscreen': getattr(settings, 'BDD_FULLSCREEN_BROWSER', False),
    }
    language = {
        'intl.accept_languages': getattr(
            settings, 'BDD_BROWSER_LANGUAGE', 'en-US'
        )
    }
    if driver_name == 'firefox':
        params.update({
            'profile_preferences': language,
            'capabilities': {'moz:webdriverClick': False},
        })
    elif driver_name == 'chrome':
        load_entry_point('chromedriver-binary==2.43.0', 'console_scripts', 'chromedriver-path')
        options = Options()
        options.add_experimental_option('prefs', language)
        params.update({
            'options': options
        })
    context.browser = Browser(**params)


def after_scenario(context, scenario):
    """Clean context for scenario."""
    context.browser.quit()
