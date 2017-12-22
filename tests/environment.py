"""Define BDD environment."""
from splinter import Browser


def before_scenario(context, scenario):
    """Prepare context for scenario."""
    if 'browser.firefox' in scenario.tags:
        driver_name = 'firefox'
    elif 'browser.phantomjs' in scenario.tags:
        driver_name = 'phantomjs'
    else:
        driver_name = 'chrome'
    context.browser = Browser(driver_name=driver_name)


def after_scenario(context, scenario):
    """Clean context for scenario."""
    context.browser.quit()
