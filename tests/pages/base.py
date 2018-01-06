"""Define base page model."""


class BasePage:
    """Base page providing a browser, a url and basic interactions."""

    url = None

    def __init__(self, context, *args, **kwargs):
        """Initialize the browser."""
        self.browser = context.browser
