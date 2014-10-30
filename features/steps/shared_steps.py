import subprocess

from behave import *

import pqaut.client as pqaut
import features.support.helpers as helpers


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

