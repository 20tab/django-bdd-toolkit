from behave import given, when, then

from tests.features.pages.home import HomePage


@given('a homepage')
def homepage_url(context):
    context.page = HomePage(context)


@when('I visit the homepage')
def visit_url(context):
    context.page.visit()


@then('I should see the 20tab logo')
def check_logo(context):
    context.test.assertTrue(context.page.browser.find_by_id('logo'))
