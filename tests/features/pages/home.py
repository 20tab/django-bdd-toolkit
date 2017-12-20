from django.urls import reverse
from selenium.webdriver.common.by import By


class HomePageLocator(object):
    # Home Page Locators

    LOGO = (By.ID, "logo")


class HomePage(object):

    def __init__(self, browser, host):
        self.driver = browser.driver
        self.host = host
        relative_url = reverse('home')
        self.url = f'{host}{relative_url}'

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
