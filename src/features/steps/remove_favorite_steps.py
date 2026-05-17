
from behave import *

@when("I remove favorite from the book")
def step_remove_favorite(context):
    # Vi är redan på katalogen efter favorite-steget, klicka stjärnan igen för att avmarkera
    context.page.locator('[data-testid="star-Why Your Tests Are Lying to You"]').click()
    context.page.wait_for_timeout(500)

@then("the book should disappear from My Books")
def step_verify_removed(context):
    context.page.get_by_role("button", name="Mina böcker").click()
    context.page.wait_for_timeout(500)
    content = context.page.locator("body").inner_text()
    assert "Why Your Tests Are Lying to You" not in content



