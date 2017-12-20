from django.urls import reverse
from selenium.webdriver.common.by import By


class HomePageLocator(object):
    # Home Page Locators

    LOGO = (By.ID, "logo")


class HomePage(object):

    def __init__(self, context):
        self.driver = context.browser.driver
        self.url = context.get_url(reverse('home'))

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def fill(self, text, *locator):
        self.find(*locator).send_keys(text)

    def click(self, *locator):
        self.find(*locator).click()

    def visit(self):
        self.driver.get(self.url)

    def get_page_title(self):
        return self.driver.title
