import pqaut.automator.factory as factory
import pqaut.automator.qwidget


class QQuickWidgetAutomator(pqaut.automator.qwidget.QWidgetAutomator):

    def __init__(self, target):
        self._target = target

    def get_children(self):
        return [factory.automate(self._target.rootObject())]
