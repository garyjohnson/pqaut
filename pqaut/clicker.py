import os

from PyQt5.Qt import QObject, QWidget, QPoint, QPointF, QTest, Qt, pyqtSignal


def log(message):
    if "DEBUG" in os.environ:
        print("[pqaut] {0}".format(message))
        print("")

class Clicker(QObject):
    do_click = pyqtSignal(QWidget, QPoint)

    def __init__(self):
        super(QObject, self).__init__()
        self.do_click.connect(self._click_on_ui_thread, type=Qt.BlockingQueuedConnection)

    def click_on(self, target, point = QPoint(0,0)):
        log("Clicking {} at {},{}".format(target, point.x(), point.y()))
        self.do_click.emit(target, point)

    def _click_on_ui_thread(self, widget, point):
        try:
            QTest.mouseClick(widget, Qt.LeftButton, Qt.NoModifier, point)
            log("Successfully clicked {} from UI thread".format(widget))
        except Exception as error:
            log("Error happened while trying to click {} from UI thread: {}".format(widget, error))
