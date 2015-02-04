import logging

from behave import use_step_matcher

import features.support.helpers as helpers


use_step_matcher("re")
logging.getLogger("requests").setLevel(logging.ERROR)

def before_all(context):
    context.config.setup_logging()

def after_scenario(context, scenario):
    helpers.kill_app(context)
