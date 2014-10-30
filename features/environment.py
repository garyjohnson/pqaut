from behave import use_step_matcher

import features.support.helpers as helpers


use_step_matcher("re")

def after_scenario(context, scenario):
    helpers.kill_app(context)
