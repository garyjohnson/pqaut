import os
import subprocess

import pqaut.client as pqaut


def launch_app(context, app_name):
    if 'DEBUG' in os.environ:
        context.test_app_process = subprocess.Popen(["python", "test_apps/{0}".format(app_name)], env=os.environ)
    else:
        context.test_app_process = subprocess.Popen(["python", "test_apps/{0}".format(app_name)], env=os.environ, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pqaut.wait_for_automation_server()

def kill_app(context):
    if context.test_app_process:
        subprocess.Popen.kill(context.test_app_process)
