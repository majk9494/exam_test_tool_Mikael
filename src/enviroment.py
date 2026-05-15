
def after_scenario(context, scenario):

    context.browser.close()

    context.playwright.stop()
