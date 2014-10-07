import os
import bottle
import json
import threading
import logging

from bottle import template
from PyQt5.Qt import QApplication, QQuickWindow

import pqaut.automator.factory as factory
import pqaut.clicker


@bottle.get("/ping")
def ping():
    if get_root_widget() is None:
        bottle.abort(503, "Still booting up, try again later")

    return 'Ping!'

@bottle.post("/click")
def click():
    return_value = {}
    window_name = get_query_value('window_name')
    value = get_query_value('value')
    automation_type = get_query_value('automation_type')

    try:
        widget = find_widget_in(get_root_widget(window_name), value, automation_type)
        if widget is not None:
            return_value = widget.to_json()
            widget.click()
    except Exception as error:
        logger.error("/click got error {0}".format(error))

    return return_value

@bottle.post("/find_element")
def find_element():
    found_json = {}
    window_name = get_query_value('window_name')
    value = get_query_value('value')
    automation_type = get_query_value('automation_type')

    widget = find_widget_in(get_root_widget(window_name), value, automation_type)
    if widget is not None:
        found_json = widget.to_json()

    logger.debug('found element: {}'.format(found_json))
    return found_json

@bottle.get("/")
def ui_tree():
    return template("<pre>{{ui_tree}}</pre>", ui_tree=json.dumps(get_root_widget().to_json(is_recursive=True), sort_keys=False, indent=4, separators=(',',': ')))

def get_query_value(name):
    if bottle.request.json is not None:
        return bottle.request.json.get('query', {}).get(name, '')

    return ''

def get_root_widget(window_name = ''):
    root_widget = None

    quick_windows = [window for window in QApplication.topLevelWindows() if isinstance(window, QQuickWindow)]
    logger.debug('root QQuickWindows: {}, root widgets: {}'.format(quick_windows, QApplication.topLevelWidgets()))
    for root_widget in quick_windows:
        root_widget = factory.automate(root_widget)
        if len(window_name) > 0 and root_widget.is_match(window_name):
            break

    if root_widget is None and any(quick_windows):
        root_widget = factory.automate(quick_windows[0]) 

    if root_widget is None:
        for root_widget in QApplication.topLevelWidgets():
            root_widget = factory.automate(root_widget)
            if len(window_name) > 0 and root_widget.is_match(window_name):
                break

    if root_widget is None and any(QApplication.topLevelWidgets()):
        root_widget = factory.automate(QApplication.topLevelWidgets()[0]) 

    logger.debug('found root widget: {}'.format(root_widget if root_widget is None else root_widget.target))
    return root_widget

def find_widget_in(parent, value, automation_type):
    for child in parent.get_children():
        if child.is_match(value, automation_type):
            return child

        found_widget = find_widget_in(child, value, automation_type)
        if found_widget is not None:
            return found_widget

    return None

def start_automation_server():
    debug = log_level_name is 'DEBUG'
    if debug:
        logger.info("Starting bottle in debug mode")
    thread = threading.Thread(target=bottle.run, kwargs={'host':'localhost', 'port':5123, 'quiet':(not debug), 'debug':debug})
    thread.setDaemon(True)
    thread.start()


log_levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
}
log_level_name = os.environ.get('PQAUT_LOG', 'DEBUG')
logging.basicConfig(level=log_levels[log_level_name])
logger = logging.getLogger(__name__)
logger.info('pqaut log level is {}'.format(log_level_name))
clicker = pqaut.clicker.Clicker()
