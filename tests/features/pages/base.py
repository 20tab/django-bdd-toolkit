"""Define base page model."""
from splinter import Browser


class BasePage:
    """Base page providing a browser, a url and basic interactions."""

    url = None

    def __init__(self, context, driver_name='chrome', *args, **kwargs):
        """Initialize the browser."""
        self.browser = Browser(driver_name=driver_name, *args, **kwargs)
