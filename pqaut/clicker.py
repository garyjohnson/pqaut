from __future__ import unicode_literals
import os
import logging

from PyQt5.Qt import QObject, QWidget, QPoint, QPointF, QTest, Qt, pyqtSignal


logger = logging.getLogger(__name__)

class Clicker(QObject):
    do_click = pyqtSignal(QObject, QPoint)

    def __init__(self):
        super(QObject, self).__init__()
        self.do_click.connect(self._click_on_ui_thread, type=Qt.QueuedConnection)

    def click_on(self, target, point = QPoint(0,0)):
        logger.debug("clicking {} at {},{}".format(target, point.x(), point.y()))
        self.do_click.emit(target, point)

    def _click_on_ui_thread(self, widget, point):
        try:
            QTest.mouseClick(widget, Qt.LeftButton, Qt.NoModifier, point)
            logger.debug("successfully clicked {} from UI thread".format(widget))
        except Exception as error:
            logger.error("error happened while trying to click {} from UI thread: {}".format(widget, error))
