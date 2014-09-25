#!/usr/bin/env python
import os, sys
sys.path.append(os.path.abspath('.'))
import pqaut.server as pqaut

import PyQt5.Qt as Qt


class Root(Qt.QWidget):

    def __init__(self):
        super(Qt.QWidget, self).__init__()
        layout = Qt.QGridLayout(self)

        widget = Qt.QWidget()
        widget.automation_id = "custom_widget"
        widget.setGeometry(0,0,400,100)

        widget2 = Qt.QWidget()
        widget2.automation_id = "custom_widget2"
        widget2.setGeometry(0,0,400,100)

        widget3 = Qt.QWidget()
        widget3.automation_id = "custom_widget3"
        widget3.setGeometry(0,0,400,100)

        layout.addWidget(widget)
        layout.addWidget(widget2)
        layout.addWidget(widget3)

        self.setGeometry(0,0,400,100)
        self.show()


pqaut.start_automation_server()
app = Qt.QApplication(sys.argv)
root = Root()
sys.exit(app.exec_())
