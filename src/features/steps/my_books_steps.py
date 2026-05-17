
from behave import *

@when("I navigate to My Books")
def step_open_my_books(context):
    context.page.get_by_role("button", name="Mina böcker").click()

@then("I should see favorite books")
def step_see_favorites(context):
    context.page.wait_for_timeout(500)
    assert context.page.get_by_text("Why Your Tests Are Lying to You").is_visible()

