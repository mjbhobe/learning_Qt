#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
* sigslots.py - illustrates signals & slots with PyQt
* @author: Manish Bhobe
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import os
import pathlib
import sys

from PyQt5.QtWidgets import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[3], 'common_files'))
from pyqt5_utils import PyQtApp


class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.browser = QTextBrowser()

        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.spinBox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(self.dial)
        # layout.addStretch()
        layout.addWidget(self.spinBox)
        self.setLayout(layout)

        # connect valueChanged signals to each other
        self.dial.valueChanged.connect(self.spinBox.setValue)
        self.spinBox.valueChanged.connect(self.dial.setValue)
        self.resize(350, 200)
        self.setWindowTitle("Qt Signals & Slots Demo")


def main():
    app = PyQtApp(sys.argv)

    w = Form()
    w.setFont(app.getFont())
    w.show()

    return app.exec()


if __name__ == "__main__":
    main()
