"""Define BDD environment."""
from django.conf import settings
from splinter import Browser


def before_scenario(context, scenario):
    """Prepare context for scenario."""
    if 'browser.firefox' in scenario.tags:
        driver_name = 'firefox'
    elif 'browser.chrome' in scenario.tags:
        driver_name = 'chrome'
    else:
        driver_name = getattr(settings, 'BDD_DEFAULT_BROWSER', 'chrome')
    headless = getattr(settings, 'BDD_HEADLESS_BROWSER', False)
    context.browser = Browser(driver_name=driver_name, headless=headless)


def after_scenario(context, scenario):
    """Clean context for scenario."""
    context.browser.quit()
