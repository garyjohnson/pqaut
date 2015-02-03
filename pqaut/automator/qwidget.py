from __future__ import unicode_literals
from collections import OrderedDict
import types

import pqaut.automator.factory as factory
import pqaut.automator.qobject
import pqaut.server

class QWidgetAutomator(pqaut.automator.qobject.QObjectAutomator):

    def __init__(self, target):
        self._target = target

    def click(self):
        pqaut.server.clicker.click_on(self._target)

    def clickable_target(self, point):
        return self.target.childAt(point.x(), point.y())

    def global_position(self):
        return self.target.mapToGlobal(self.target.pos())

    def is_offscreen(self):
        return self.target.visibleRegion().isEmpty()

    def is_match(self, value=None, automation_id=None, automation_type=None):
        text = self.get_value()
        nbsp = "\u00A0"
        text_with_normalized_spaces = text.replace(nbsp, " ")
        print('matching value: {}, automation_id: {}, automation_type: {}'.format(value, automation_id, automation_type))

        if automation_type is not None and len(automation_type) > 0 and automation_type != self.automation_type():
            return False

        if value  in [text_with_normalized_spaces, text, self.get_name()]:
                return True

        if automation_id is not None and automation_id == self.automation_id():
                return True

        return False

    def to_json(self, is_recursive=False):
        json=OrderedDict([
                ('type',self.target.__class__.__name__), 
                ('automation_id', self.automation_id()),
                ('automation_type',self.automation_type()),
                ('name',self.get_name()), 
                ('value',self.get_value()), 
                ('visible',self.value_or_default('isVisible', True)),
                ('enabled',self.value_or_default('isEnabled', False)), 
                ('offscreen',self.is_offscreen()),
                ('frame', OrderedDict([
                    ('x',self.value_or_default('x', 0)),
                    ('y',self.value_or_default('y', 0)),
                    ('width',self.value_or_default('width', 0)),
                    ('height',self.value_or_default('height', 0)),
                ])), 
                ('global_position', OrderedDict([
                    ('x',self.global_position().x()),
                    ('y',self.global_position().y()),
                ])),
            ])

        if is_recursive:
            children_json = []
            for child in self.get_children():
                children_json.append(child.to_json(is_recursive))
            json['children'] = children_json

        return json

