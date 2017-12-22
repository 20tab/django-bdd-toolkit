"""Define homepage page model."""
from django.urls import reverse

from tests.features.pages.base import BasePage


class HomePage(BasePage):
    """Homepage model and interactions."""

    def __init__(self, context, *args, **kwargs):
        """Set the homepage url."""
        self.url = context.get_url(reverse('home'))
        super().__init__(context, *args, **kwargs)

    @property
    def logo_locator(self):
        """Return the logo web element."""
        return self.browser.find_by_id('logo')

    def visit(self):
        """Use the browser to visit the homepage url."""
        self.browser.visit(self.url)
