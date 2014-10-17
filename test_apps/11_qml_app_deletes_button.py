#!/usr/bin/env python
import os, sys
sys.path.append(os.path.abspath('.'))
import pqaut.server as pqaut

import PyQt5.Qt as Qt


pqaut.start_automation_server()
app = Qt.QApplication(sys.argv)

engine = Qt.QQmlEngine()
component = Qt.QQmlComponent(engine)
component.loadUrl(Qt.QUrl('test_apps/11_qml_app_deletes_button.qml'))
for error in component.errors():
    print error.description()
window = component.create()
window.show()

sys.exit(app.exec_())
