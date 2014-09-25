import subprocess

from lettuce import *

import pqaut.client as pqaut


@step(u'I am running "([^"]*)"$')
def given_i_am_running_app(step, app_name):
    world.launch_app(app_name)

@step(u'I see "([^"]*)"$')
def then_i_see(step, target):
    pqaut.assert_is_visible(target)

@step(u'I do not see "([^"]*)"$')
def then_i_do_not_see(step, target):
    pqaut.assert_is_not_visible(target)

@step(u'I see "([^"]*)" with type "([^"]*)"$')
def then_i_see_with_type(step, name, automation_type):
    pqaut.assert_is_visible(name, automation_type)

@step(u'I do not see "([^"]*)" with type "([^"]*)"$')
def then_i_do_not_see_with_type(step, name, automation_type):
    pqaut.assert_is_not_visible(name, automation_type)

@step(u'I tap on "([^"]*)"$')
def i_tap_on(step, name):
    pqaut.tap(name)

