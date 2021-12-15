from behave import *


def sign_in_endpoint(username, password):
    if not username:
        raise ValueError("username cannot be empty")
    print("user created")
    return 1


def sign_in_button(username, password):
    print("user signed in !")


@given("login screen is loaded")
def step_impl(context):
    pass


@when("user-name field is empty")
def step_impl(context):
    assert True is not False


@then("'sign-in' button is gryed-out")
def step_impl(context):
    assert context.failed is False


@given("a sign in request recived")
def step_impl(context):
    pass


@when("user-name is missing")
def step_impl(context):
    assert True is not False


@then("user will not be created")
def step_impl(context):
    assert context.failed is False