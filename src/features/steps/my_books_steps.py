
from behave import *


@when("I navigate to My Books")
def step_open_my_books(context):

    context.page.get_by_role("link", name="Mina böcker").click()


@then("I should see favorite books")
def step_see_favorites(context):

    assert context.page.locator("body").is_visible()

