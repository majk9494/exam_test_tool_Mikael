
from behave import *

@given("I open the reading list page")
def step_open_page(context):
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")

@when("I navigate to add book page")
def step_go_to_add_book(context):
    context.page.get_by_role("button", name="Lägg till bok").click()

@when("I fill in title and author")
def step_fill_book_form(context):
    context.page.get_by_label("Titel").fill("Python Testing")
    context.page.get_by_label("Författare").fill("Test Författare")

@when("I submit the book form")
def step_submit_book(context):
    context.page.get_by_role("button", name="Lägg till ny bok").click()

@then("I should see the new book")
def step_verify_new_book(context):
    context.page.get_by_role("button", name="Katalog").click()
    assert context.page.get_by_text("Python Testing").is_visible()

