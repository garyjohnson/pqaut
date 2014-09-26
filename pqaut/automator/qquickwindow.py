import types

import pqaut.automator.factory as factory
import pqaut.automator.qobject


class QQuickWindowAutomator(pqaut.automator.qobject.QObjectAutomator):

    def __init__(self, target):
        self._target = target

    def clickable_target(self, point):
        return self.target

    def get_children(self):
        return [factory.automate(self._target.contentItem())]
