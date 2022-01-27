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

        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.spinBox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinBox)

        self.pb = QPushButton("Quit")
        self.pb.setDefault(True)
        self.pb.clicked.connect(qApp.quit)

        layout2 = QHBoxLayout()
        layout2.addStretch()
        layout2.addWidget(self.pb)

        #vlayout = QVBoxLayout()
        # vlayout.addLayout(layout)
        # vlayout.addLayout(layout2)

        self.setLayout(layout)

        # connect valueChanged signals to each other
        self.dial.valueChanged.connect(self.spinBox.setValue)
        self.spinBox.valueChanged.connect(self.dial.setValue)
        self.resize(350, 200)
        self.setWindowTitle("Qt Signals & Slots Demo")


def loadStyleSheet() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    print(f"loasStyleSteet() -> You are {here}")
    darkss_dir = os.path.join(here, "styles", "dark")
    sys.path.append(darkss_dir)
    import stylesheet_rc

    darkss_path = os.path.join(darkss_dir, "stylesheet.css")
    assert os.path.exists(darkss_path)
    print(f"LoasStyleSheet() -> loading dark stylesheet from {darkss_path}")
    stylesheet = ""
    with open(darkss_path, "r") as f:
        stylesheet = f.read()
    return stylesheet


def main():
    app = PyQtApp(sys.argv)

    w = Form()
    stylesheet = loadStyleSheet()
    w.setStyleSheet(stylesheet)
    w.move(100, 100)
    w.show()

    rect = w.geometry()
    w1 = Form()
    w1.setFont(app.getFont())
    w1.show()
    w1.move(rect.left() + rect.width() + 50, rect.top() + rect.height() // 4 + 50)

    return app.exec()


if __name__ == "__main__":
    main()
