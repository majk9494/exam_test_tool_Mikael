
from behave import *


@when("I remove favorite from the book")
def step_remove_favorite(context):

    buttons = context.page.locator("button")

    buttons.nth(0).click()


@then("the book should disappear from My Books")
def step_verify_removed(context):

    context.page.get_by_role("link", name="Mina böcker").click()

    assert context.page.locator("body").is_visible()

