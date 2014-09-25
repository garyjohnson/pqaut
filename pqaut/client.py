import requests
import time
import json
from lettuce import world
from nose.tools import assert_equals, assert_true, assert_is_not_none, assert_is_none, assert_false


def wait_for_automation_server():
    while (True):
        time.sleep(0.5)
        try:
            response = requests.get("http://localhost:5123/ping")
            if response.status_code == 200:
                break
        except:
            pass

def tap(name, automation_type = None):
    assert_is_visible(name, automation_type)
    time.sleep(0.4)
    headers = {'Content-type': 'application/json', 'Accept': 'application/json' }
    body = {'query':{'window_name':'', 'value':name, 'automation_type':automation_type}}
    response = requests.post('http://localhost:5123/click', data=json.dumps(body), headers=headers)
    time.sleep(0.3)

def assert_is_not_visible(name, automation_type = None, timeout=3):
    assert_true(_wait_for_element_to_not_be_visible(name, automation_type, timeout), u"Found element but expected it to not be visible")

def assert_is_visible(name, automation_type = None, timeout=3):
    assert_is_not_none(_wait_for_visible_element(name, automation_type, timeout), u"Visible element not found with name {0} and type {1}".format(name, automation_type))

def _wait_for_element_to_not_be_visible(name, automation_type, timeout):
    retries = 0
    delay = 0.3
    while retries * delay < timeout:
        retries += 1

        try:
            found_element = _find_element(name, automation_type)
        except requests.exceptions.ConnectionError:
            time.sleep(delay)
            continue

        if found_element is None or not _element_is_visible(found_element):
            return True

        time.sleep(delay)

    return False

def _wait_for_visible_element(name, automation_type, timeout):
    retries = 0
    delay = 0.3
    while retries * delay < timeout:
        retries += 1

        try:
            found_element = _find_element(name, automation_type)
        except requests.exceptions.ConnectionError:
            time.sleep(delay)
            continue

        if found_element is not None and _element_is_visible(found_element):
            return found_element

        time.sleep(delay)

    return None

def _element_is_visible(element):
    return element["visible"] and not element["offscreen"]

def _find_element(name, automation_type):
    headers = {'Content-type': 'application/json', 'Accept': 'application/json' }
    body = {'query':{'window_name':'', 'value':name, 'automation_type':automation_type}}
    response = requests.post('http://localhost:5123/find_element', data=json.dumps(body), headers=headers)
    found_element = response.json()
    if len(found_element.keys()) == 0:
        return None

    return found_element

