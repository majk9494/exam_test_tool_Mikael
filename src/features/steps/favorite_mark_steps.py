
from behave import *

@when("I favorite a book")
def step_favorite_book(context):
    context.favorited_book_title = "Why Your Tests Are Lying to You"
    context.page.locator('[data-testid="star-Why Your Tests Are Lying to You"]').click()
    context.page.wait_for_timeout(500)

@then("the book should appear in My Books")
def step_verify_favorite(context):
    context.page.get_by_role("button", name="Mina böcker").click()
    context.page.wait_for_timeout(500)
    assert context.page.get_by_text("Why Your Tests Are Lying to You").is_visible()




