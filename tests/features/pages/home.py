from django.urls import reverse

from tests.features.pages.base import BasePage


class HomePage(BasePage):

    def __init__(self, context):
        super().__init__(context)
        self.url = context.get_url(reverse('home'))

    def visit(self):
        self.browser.visit(self.url)
