import subprocess
import os

from lettuce import *

import pqaut.client as pqaut


world.app_process = None

@world.absorb
def launch_app(app_name):
    if "DEBUG" in os.environ:
        world.app_process = subprocess.Popen(["python", "test_apps/{0}".format(app_name)])
    else:
        world.app_process = subprocess.Popen(["python", "test_apps/{0}".format(app_name)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pqaut.wait_for_automation_server()

@after.each_scenario
def after_each(obj):
    if world.app_process:
        subprocess.Popen.kill(world.app_process)
