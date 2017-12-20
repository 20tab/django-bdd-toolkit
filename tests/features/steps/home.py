from behave import given, when, then

from pages.home import HomePage, HomePageLocator


@given('a homepage')
def homepage_url(context):
    context.page = HomePage(context.browser, context.test.live_server_url)


@when('I visit the homepage')
def visit_url(context):
    context.page.visit()


@then('I should see the 20tab logo')
def check_logo(context):
    logo = HomePageLocator().LOGO
    context.test.assertTrue(context.page.find(*logo))
