"""Define BDD environment."""
from django.conf import settings
from pkg_resources import load_entry_point
from splinter import Browser
from splinter.driver.webdriver.chrome import Options


def before_scenario(context, scenario):
    """Prepare context for scenario."""
    if "browser.firefox" in scenario.tags:
        driver_name = "firefox"
    elif "browser.chrome" in scenario.tags:
        driver_name = "chrome"
    else:
        driver_name = getattr(settings, "BDD_DEFAULT_BROWSER", "chrome")
    params = {
        "driver_name": driver_name,
        "headless": getattr(settings, "BDD_HEADLESS_BROWSER", False),
        "incognito": getattr(settings, "BDD_INCOGNITO_BROWSER", False),
        "wait_time": getattr(settings, "BDD_DEFAULT_WAIT_TIME", 5),
        "fullscreen": getattr(settings, "BDD_FULLSCREEN_BROWSER", False),
    }
    language = {
        "intl.accept_languages": getattr(settings, "BDD_BROWSER_LANGUAGE", "en-US")
    }
    if driver_name == "firefox":
        params.update(
            {
                "profile_preferences": language,
                "capabilities": {"moz:webdriverClick": False},
            }
        )
    elif driver_name == "chrome":
        driver_package_name_constant_name = "BDD_CHROME_DRIVER_PACKAGE_NAME"
        driver_package_name = getattr(settings, driver_package_name_constant_name, None)
        if driver_package_name:
            with open(
                f"{settings.BASE_DIR}/requirements.txt", "r"
            ) as test_packages_list:
                for line in test_packages_list:
                    if driver_package_name in line:
                        load_entry_point(
                            line, "console_scripts", "chromedriver-path",
                        )
        else:
            raise Exception(
                "Please install a chrome driver package and ensure it is "
                f"specified in the {driver_package_name_constant_name} setting."
            )
        options = Options()
        options.add_experimental_option("prefs", language)
        params.update({"options": options})
    context.browser = Browser(**params)


def after_scenario(context, scenario):
    """Clean context for scenario."""
    context.browser.quit()
