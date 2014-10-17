import os
import requests
import time
import json
import logging
from lettuce import world
from nose.tools import assert_equals, assert_true, assert_is_not_none, assert_is_none, assert_false


TIMEOUT=3

def wait_for_automation_server():
    logger.info('waiting for automation server')
    while (True):
        time.sleep(0.5)
        try:
            response = requests.get("http://0.0.0.0:5123/ping", timeout=TIMEOUT)
            if response.status_code == 200:
                break
        except requests.exceptions.Timeout as ex:
            logger.debug(u'pqaut timed out waiting for automation server: {}'.format(ex))
        except Exception as ex:
            logger.debug(u'error occurred while waiting for automation server: {}'.format(ex))
            pass

def tap(name, automation_type = None):
    logger.info(u'tapping on {} with automation_type {}'.format(name, automation_type))
    assert_is_visible(name, automation_type)
    time.sleep(0.4)
    headers = {'Content-type': 'application/json', 'Accept': 'application/json' }
    body = {'query':{'window_name':'', 'value':name, 'automation_type':automation_type}}
    try:
        response = requests.post('http://0.0.0.0:5123/click', data=json.dumps(body), headers=headers, timeout=TIMEOUT)
    except requests.exceptions.Timeout as ex:
        logger.debug(u'pqaut timed out tapping on {}: {}'.format(name, ex))
    except Exception as ex:
        logger.debug(u'error occurred while tapping on {}: {}'.format(name, ex))
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
            logger.debug(u'trying to find invisible element {} with type {}'.format(name, automation_type))
            found_element = _find_element(name, automation_type)
        except requests.exceptions.Timeout as ex:
            logger.debug(u'pqaut timed out while looking for {}: {}'.format(name, ex))
            time.sleep(delay)
            continue
        except requests.exceptions.ConnectionError as ex:
            logger.debug(u'error occurred while looking for element: {}'.format(ex))
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
            logger.debug(u'trying to find element {} with type {}'.format(name, automation_type))
            found_element = _find_element(name, automation_type)
        except requests.exceptions.Timeout as ex:
            logger.debug(u'pqaut timed out while looking for {}: {}'.format(name, ex))
            time.sleep(delay)
            continue
        except requests.exceptions.ConnectionError as ex:
            logger.debug(u'error occurred while looking for element: {}'.format(ex))
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
    response = requests.post('http://0.0.0.0:5123/find_element', data=json.dumps(body), headers=headers, timeout=TIMEOUT)
    found_element = response.json()
    if len(found_element.keys()) == 0:
        return None

    return found_element

log_levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
}
log_level_name = os.environ.get('PQAUT_LOG', 'ERROR')
logging.basicConfig(level=log_levels[log_level_name])
logger = logging.getLogger(__name__)
logger.info('pqaut log level is {}'.format(log_level_name))
