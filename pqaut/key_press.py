from __future__ import unicode_literals
import os
import logging

from PyQt5.Qt import QObject, QWidget, QPoint, QPointF, QTest, Qt, pyqtSignal, QApplication, QVariant, pyqtSlot


logger = logging.getLogger(__name__)

class PropertySetter(QObject):
    def __init__(self, target, property, value):
        super(QObject, self).__init__()
        self.target = target
        self.property = property
        self.value = value

    def set_value(self):
        raise NotImplementedError()

class KeyPress(QObject):
    set_value = pyqtSignal(QObject)

    def __init__(self):
        super(QObject, self).__init__()
        self.set_value.connect(self._set_value_on_ui_thread, type=Qt.QueuedConnection)

    def input(self, property_setter):
        logger.debug("setting property {} to {} ".format(property_setter.property, property_setter.value))
        self.set_value.emit(property_setter)

    def _set_value_on_ui_thread(self, property_setter):
        try:
            property_setter.set_value()
        except Exception as ex:
            logger.debug(ex)

