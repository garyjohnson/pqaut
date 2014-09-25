#!/usr/bin/env python
import os, sys
sys.path.append(os.path.abspath('.'))
import pqaut.server as pqaut

from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Root(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        label = QLabel('This is QLabel.text', self)
        label.setGeometry(0,0,400,100)
        self.show()

pqaut.start_automation_server()
app = QApplication(sys.argv)
root = Root()
sys.exit(app.exec_())
