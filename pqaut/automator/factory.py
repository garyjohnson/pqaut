import importlib
import PyQt5.Qt


def automate(target):
    automators = ['QQuickWindow', 'QQuickItem', 'QQuickWidget', 'QWidget', 'QObject']

    for class_name in automators:
        qt_type = getattr(PyQt5.Qt, class_name)
        automator_module = importlib.import_module('pqaut.automator.{}'.format(class_name.lower()))
        automator_type = getattr(automator_module, '{}Automator'.format(class_name))

        if qt_type is not None and automator_type is not None and isinstance(target, qt_type):
            return automator_type(target)

    raise Exception('No automator found for {}'.format(target))

