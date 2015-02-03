from __future__ import unicode_literals
from collections import OrderedDict
import logging

from PyQt5.Qt import QObject

import pqaut.automator.factory as factory
import pqaut.key_press


logger = logging.getLogger(__name__)

class QObjectPropertySetter(pqaut.key_press.PropertySetter):
    def set_value(self):
        setattr(self.target, self.property_name, self.value)

class QObjectAutomator(object):

    def __init__(self, target):
        self._target = target

    @property
    def target(self):
        return self._target

    def click(self):
        pass

    def clickable_target(self, point):
        return _target

    def is_offscreen(self):
        return False

    def get_children(self):
        children = []

        try:
            children = self._target.findChildren(QObject)
        except Exception as ex:
            logger.debug('could not find children on {}: {}'.format(self._target, ex))

        logger.debug('found children {} on {}'.format(self._target, children))
        return [factory.automate(c) for c in children];

    def is_match(self,value=None, automation_id=None, automation_type=None):
        return False

    def automation_id(self):
        return self.value_or_default('automation_id', None)

    def automation_type(self):
        return self.value_or_default('automation_type', '')

    def get_name(self):
        return self.value_or_default('objectName', '')

    def get_value(self):
        return self.value_or_default('text', '')

    def to_json(self, is_recursive=False):
        json=OrderedDict([ 
            ('type',self._target.__class__.__name__), 
            ('value',self.value_or_default('text', '')),  
        ])

        if is_recursive:
            children_json = []
            for child in self.get_children():
                children_json.append(child.to_json(is_recursive))
            json['children'] = children_json

        return json

    def hasmethod(self, method_name):
        return hasattr(self._target, method_name) and callable(getattr(self._target, method_name))

    def value_or_default(self, value_name, default):
        value = default
        if self.hasmethod(value_name):
            method = getattr(self._target, value_name)
            try:
                value = method()
            except Exception as e:
                pass

        elif hasattr(self._target, value_name):
            value = getattr(self._target, value_name)

        return value

    def set_value(self, value_name, value):
        property_setter = QObjectPropertySetter(self._target, 'text', value)
        sip.transferto(property_setter, self._target)
        try:
            pqaut.server.key_press.input(property_setter)
        except Exception as ex:
            logger.debug("error on  set value on ui thread: {}".format(ex))

