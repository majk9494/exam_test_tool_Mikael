
from behave import *


@when("I favorite a book")
def step_favorite_book(context):

    buttons = context.page.locator("button")

    buttons.nth(0).click()


@then("the book should appear in My Books")
def step_verify_favorite(context):

    context.page.get_by_role("link", name="Mina böcker").click()

    assert context.page.locator("body").is_visible()

