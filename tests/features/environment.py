from browser import Browser


def before_all(context):
    context.browser = Browser()


def after_all(context):
    context.browser.close()
