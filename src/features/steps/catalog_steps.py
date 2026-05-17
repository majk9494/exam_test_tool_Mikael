
from behave import *

@when("I navigate to catalog")
def step_go_to_catalog(context):
    context.page.get_by_role("button", name="Katalog").click()

@then("I should see books in the catalog")
def step_see_books_in_catalog(context):
    assert context.page.get_by_text("Ormar på ett plan").is_visible()

@then("I should see the catalog page")
def step_see_catalog_page(context):
    assert context.page.get_by_text("Sidan för dig som gillar att läsa").is_visible()


