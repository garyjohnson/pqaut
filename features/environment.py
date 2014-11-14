from behave import use_step_matcher

import features.support.helpers as helpers


use_step_matcher("re")

def before_all(context):
    context.config.logging_level="ERROR"
    context.config.setup_logging()

def after_scenario(context, scenario):
    helpers.kill_app(context)
