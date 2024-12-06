from behave import *
from hamcrest import assert_that, equal_to


@step("the home page is opened")
def step_impl(context):
    context.homepage.open_page()


@step("the '{field}' field is filled with '{text}'")
def step_impl(context, field, text):
    field = '' if field == '[blank]' else field
    text = '' if text == '[blank]' else text
    context.homepage.fill_out_field(field, text)


@step("the '{button}' button is clicked")
def step_impl(context, button):
    context.homepage.click_button(button)
    if button == "Reset":
        context.homepage.click_button("Close")


@step("the '{error}' message is shown")
def step_impl(context, error):
    assert_that(context.homepage.get_error_message("login error"), equal_to(error))


@given("the '{product}' is added to the cart")
def step_impl(context, product):
    context.homepage.add_product_to_cart(product)


@then("the price should read '{total}'")
def step_impl(context, total):
    assert_that(context.homepage.get_total(), equal_to(total))


@then("the '{page}' page is opened")
def step_impl(context, page):
    assert_that(context.homepage.get_current_url(), equal_to(context.homepage.pages[page]))


@then("the '{error}' checkout message is shown")
def step_impl(context, error):
    assert_that(context.homepage.get_error_message("checkout error"), equal_to(error))


@when("the '{item}' is removed from the cart")
def step_impl(context, item):
    context.homepage.remove_product_from_cart(item)


@then("the cart should be empty")
def step_impl(context):
    assert_that(context.homepage.is_cart_empty(), equal_to(True))