from behave import *
from web_behave.pageobjects.key_presses_page import KeyPressesPageObject
from nose.tools import assert_equal

use_step_matcher("parse")


@given("the key_presses page is open")
def step_impl(context):
    context.current_page = KeyPressesPageObject()
    context.current_page.open()


@when("the key: {key} were pressed")
def step_impl(context, key):
    context.current_page.send_key(key)


@then('message with text: "{message}" should appear')
def step_impl(context, message):
    assert_equal(message, context.current_page.get_message())