from __future__ import unicode_literals
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

    def is_match(self, value, matching_automation_type = None):
        text = self.get_value()
        nbsp = "\u00A0"
        text_with_normalized_spaces = text.replace(nbsp, ' ')
        if value == text_with_normalized_spaces or value == text or value == self.get_name() or value == self.automation_id():
            if matching_automation_type is None or len(matching_automation_type) == 0:
                return True
            elif matching_automation_type == self.automation_type():
                return True

        return False

    def to_json(self, is_recursive=False):
        json= {'type':self.target.__class__.__name__, 
                'automation_id': self.automation_id(),
                'automation_type':self.automation_type(),
                'name':self.get_name(), 
                'value':self.get_value(), 
                'frame': { 
                    'x':self.value_or_default('x', 0),
                    'y':self.value_or_default('y', 0),
                    'width':self.value_or_default('width', 0),
                    'height':self.value_or_default('height', 0),
                }, 
                'global_position': {
                    'x':self.global_position().x(),
                    'y':self.global_position().y(),
                },
                'visible':self.value_or_default('isVisible', True),
                'enabled':self.value_or_default('isEnabled', False), 
                'offscreen':self.is_offscreen(),
                }

        if is_recursive:
            children_json = []
            for child in self.get_children():
                children_json.append(child.to_json(is_recursive))
            json['children'] = children_json

        return json

