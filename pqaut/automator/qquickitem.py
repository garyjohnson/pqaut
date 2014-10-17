import types

from PyQt5.Qt import QPointF, QPoint, QObject

import pqaut.automator.factory as factory
import pqaut.automator.qobject
import pqaut.server


class QQuickItemAutomator(pqaut.automator.qobject.QObjectAutomator):

    def __init__(self, target):
        self._target = target

    def click(self):
        pointf = self.target.mapToScene(QPointF(0.0, 0.0))
        x = pointf.x()
        y = pointf.y()
        x += self.value_or_default("width", 0.0) / 2.0
        y += self.value_or_default("height", 0.0) / 2.0
        point = QPoint(x,y)
        root_widget = pqaut.server.get_root_widget()
        pqaut.server.clicker.click_on(root_widget.target, point)

    def global_position(self):
        return self.target.mapToScene(QPointF(0.0, 0.0))

    def is_offscreen(self):
        first_child = pqaut.server.get_root_widget()
        root_width = first_child.value_or_default('width', 0.0)
        root_height = first_child.value_or_default('height', 0.0)
        pointf = self._target.mapToScene(QPointF(0.0, 0.0))
        x = pointf.x()
        y = pointf.y()
        width = self.value_or_default("width", 0.0)
        height = self.value_or_default("height", 0.0) 
        return x+width <= 0 or x >= root_width or y+height <= 0 or y >= root_height

    def get_children(self):
        children = []

        try:
            children = self._target.childItems()
            if children is None:
                children = self._target.findChildren(QObject)
        except Exception as e:
            pass

        return [factory.automate(c) for c in children];

    def is_match(self, value, matching_automation_type=None):
        text = self.get_value()
        nbsp = u"\u00A0"
        text_with_normalized_spaces = text.replace(nbsp, " ")
        if value == text_with_normalized_spaces or value == text or value == self.get_name() or value == self.automation_id():
            if matching_automation_type is None or len(matching_automation_type) == 0:
                return True
            elif matching_automation_type == self.automation_type():
                return True

        return False

    def to_json(self, is_recursive = False):
        json= { 'type':self._target.__class__.__name__, 
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
                'visible':self.value_or_default('visible', True),
                'enabled':self.value_or_default('enabled', False),
                'offscreen':self.is_offscreen(),
                }

        if is_recursive:
            children_json = []
            for child in self.get_children():
                children_json.append(child.to_json(is_recursive))
            json['children'] = children_json

        return json

    def value_or_default(self, value_name, default):
        value = default

        try:
            meta_object = self._target.metaObject()

            index = meta_object.indexOfProperty(value_name)
            if index >= 0:
                value = meta_object.property(index).read(self._target)

            if type(value) == types.StringType:
                return value.decode('utf-8')
            return value
        except Exception as ex:
            return default
