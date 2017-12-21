"""Define steps for the home feature."""
from behave import given, when, then

from tests.features.pages.home import HomePage


@given('a homepage')
def get_page(context):
    """Create the home page."""
    context.page = HomePage(context)


@when('I visit the homepage')
def visit_page(context):
    """Visit the home page."""
    context.page.visit()


@then('I should see the 20tab logo')
def check_logo(context):
    """Check the presence of the logo element."""
    context.test.assertTrue(context.page.browser.find_by_id('logo'))
