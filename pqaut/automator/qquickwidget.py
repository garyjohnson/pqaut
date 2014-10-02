import pqaut.automator.factory as factory
import pqaut.automator.qwidget


class QQuickWidgetAutomator(pqaut.automator.qwidget.QWidgetAutomator):

    def __init__(self, target):
        self._target = target

    def get_children(self):
        children = []
        root_object = self._target.rootObject()
        if root_object is not None:
            children.append(factory.automate(root_object))
        return children
