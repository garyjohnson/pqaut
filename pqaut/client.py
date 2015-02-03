from __future__ import unicode_literals
import os
import time
import json
import logging

import requests
from nose.tools import assert_equals, assert_true, assert_is_not_none, assert_is_none, assert_false


RETRIES=100
TIMEOUT=3

def wait_for_automation_server():
    logger.info('waiting for automation server')
    connected = False
    retry_count = 0
    while (retry_count < RETRIES):
        retry_count += 1
        time.sleep(0.5)
        try:
            response = requests.get("http://0.0.0.0:5123/ping", timeout=TIMEOUT)
            if response.status_code == 200:
                connected = True
                break
        except requests.exceptions.Timeout as ex:
            logger.debug('pqaut timed out waiting for automation server: {}'.format(ex))
        except Exception as ex:
            logger.debug('error occurred while waiting for automation server: {}'.format(ex))

    if not connected:
        raise Exception('pqaut timed out waiting for automation server')

def tap(name, automation_type = None):
    logger.info('tapping on {} with automation_type {}'.format(name, automation_type))
    assert_is_visible(name, automation_type)
    time.sleep(0.4)
    headers = {'Content-type': 'application/json', 'Accept': 'application/json' }
    body = {'query':{'window_name':'', 'value':name, 'automation_type':automation_type}}
    try:
        response = requests.post('http://0.0.0.0:5123/click', data=json.dumps(body), headers=headers, timeout=TIMEOUT)
    except requests.exceptions.Timeout as ex:
        logger.debug('pqaut timed out tapping on {}: {}'.format(name, ex))
    except Exception as ex:
        logger.debug('error occurred while tapping on {}: {}'.format(name, ex))
    time.sleep(0.3)

def input(input_item, value):
    logger.info('setting input on on {} with {}'.format(input_item, value))
    headers = {'Content-type': 'application/json', 'Accept': 'application/json' }
    body = {'query':{'window_name':'', 'input_item':input_item, 'automation_type':None, 'value':value}}
    try:
        response = requests.post('http://0.0.0.0:5123/input', data=json.dumps(body), headers=headers, timeout=TIMEOUT)
    except requests.exceptions.Timeout as ex:
        logger.debug('pqaut timed out inputing on {}: {}'.format(input_item, ex))
    except Exception as ex:
        logger.debug('error occurred while inputing on {}: {}'.format(input_item, ex))
    time.sleep(0.3)

def assert_is_not_visible(name, automation_type = None, timeout=3):
    assert_true(_wait_for_element_to_not_be_visible(name, automation_type, timeout), 'Found element but expected it to not be visible')

def assert_is_visible(name, automation_type = None, timeout=3):
    assert_is_not_none(_wait_for_visible_element(name, automation_type, timeout), 'Visible element not found with name {0} and type {1}'.format(name, automation_type))

def _wait_for_element_to_not_be_visible(name, automation_type, timeout):
    retries = 0
    delay = 0.3
    while retries * delay < timeout:
        retries += 1

        try:
            logger.debug('trying to find invisible element {} with type {}'.format(name, automation_type))
            found_element = find_element(name, automation_type)
        except requests.exceptions.Timeout as ex:
            logger.debug('pqaut timed out while looking for {}: {}'.format(name, ex))
            time.sleep(delay)
            continue
        except requests.exceptions.ConnectionError as ex:
            logger.debug('error occurred while looking for element: {}'.format(ex))
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
            logger.debug('trying to find element {} with type {}'.format(name, automation_type))
            found_element = find_element(name, automation_type)
        except requests.exceptions.Timeout as ex:
            logger.debug('pqaut timed out while looking for {}: {}'.format(name, ex))
            time.sleep(delay)
            continue
        except requests.exceptions.ConnectionError as ex:
            logger.debug('error occurred while looking for element: {}'.format(ex))
            time.sleep(delay)
            continue

        if found_element is not None and _element_is_visible(found_element):
            return found_element

        time.sleep(delay)

    return None

def find_element(name, automation_type):
    headers = {'Content-type': 'application/json', 'Accept': 'application/json' }
    body = {'query':{'window_name':'', 'value':name, 'automation_type':automation_type}}
    response = requests.post('http://0.0.0.0:5123/find_element', data=json.dumps(body), headers=headers, timeout=TIMEOUT)
    found_element = response.json()
    if len(found_element.keys()) == 0:
        return None

    return found_element

def _element_is_visible(element):
    return element["visible"] and not element["offscreen"]

log_levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
}
log_level_name = os.environ.get('PQAUT_LOG', 'ERROR')
logging.basicConfig(level=log_levels[log_level_name])
logger = logging.getLogger(__name__)
logger.setLevel(log_levels[log_level_name])
logger.info('pqaut log level is {}'.format(log_level_name))
