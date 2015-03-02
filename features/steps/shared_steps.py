import subprocess

from behave import *

import pqaut.client as pqaut
import features.support.helpers as helpers
from nose.tools import assert_equal


@given('I am running "(?P<app_name>[^"]*)"$')
def i_am_running_app(context, app_name):
    helpers.launch_app(context, app_name)

@then('I see "(?P<target>[^"]*)"$')
def then_i_see(context, target):
    pqaut.assert_is_visible(target)

@then('I do not see "(?P<target>[^"]*)"$')
def then_i_do_not_see(context, target):
    pqaut.assert_is_not_visible(target)

@then('I see "(?P<name>[^"]*)" with type "(?P<automation_type>[^"]*)"$')
def then_i_see_with_type(context, name, automation_type):
    pqaut.assert_is_visible(name, automation_type)

@then('I do not see "(?P<name>[^"]*)" with type "(?P<automation_type>[^"]*)"$')
def then_i_do_not_see_with_type(context, name, automation_type):
    pqaut.assert_is_not_visible(name, automation_type)

@when('I tap on "(?P<name>[^"]*)"$')
def i_tap_on(context, name):
    pqaut.tap(name)

@when(u'I enter "(?P<input>[a-z]*)" in text input')
def i_set_input(context, input):
    pqaut.input('text_input', input)

@step(u'I set the slider "(?P<automation_id>.*)" to "(?P<value>.*)"')
def step_impl(context, automation_id, value):
    pqaut.set_value(automation_id=automation_id, property='value', value=value)

@step(u'the slider "(?P<automation_id>.*)" is "(?P<value>.*)"')
def step_impl(context, automation_id, value):
    assert_equal(pqaut.get_value(automation_id, 'value'), int(value))
