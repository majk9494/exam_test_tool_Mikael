
from behave import *
from playwright.sync_api import sync_playwright


@given("I open the reading list page")
def step_open_page(context):

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://tap-ht25-testverktyg.github.io/exam/")

    context.playwright = playwright
    context.browser = browser
    context.page = page


@when("I navigate to add book page")
def step_go_to_add_book(context):

    context.page.get_by_role("link", name="Lägg till bok").click()


@when("I fill in title and author")
def step_fill_book_form(context):

    context.page.get_by_placeholder("Titel").fill("Python Testing")

    context.page.get_by_placeholder("Författare").fill("Araceli")


@when("I submit the book form")
def step_submit_book(context):

    context.page.get_by_role("button", name="Lägg till").click()


@then("I should see the new book")
def step_verify_new_book(context):

    assert context.page.locator("text=Python Testing").is_visible()

