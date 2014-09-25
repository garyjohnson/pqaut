#!/usr/bin/env python
import os, sys
sys.path.append(os.path.abspath('.'))
import pqaut.server as pqaut

import PyQt5.Qt as Qt

class Root(Qt.QWidget):

    def __init__(self):

        super(Qt.QWidget, self).__init__()
        button = Qt.QPushButton('This is QButton.text', self)
        button.setGeometry(0,0,400,100)
        button.clicked.connect(lambda: label.setText('Button was clicked'))

        label = Qt.QLabel()
        label.setGeometry(0,0,400,100)

        layout = Qt.QGridLayout(self)
        layout.addWidget(button)
        layout.addWidget(label)

        self.setGeometry(0,0,400,100)
        self.show()

pqaut.start_automation_server()
app = Qt.QApplication(sys.argv)
root = Root()
sys.exit(app.exec_())
