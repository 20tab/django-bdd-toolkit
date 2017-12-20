

class BasePage(object):

    def __init__(self, context):
        self.context = context
        self.browser = context.browser
