#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
* sigslots2.py - many to 1 signal handler
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
        texts = ["One", "Two", "Three", "Four", "Five"]
        layout = QHBoxLayout()
        for text in texts:
            button = QPushButton(text)
            button.clicked.connect(self.btnClicked)
            layout.addWidget(button)
        self.label = QLabel("Which button clicked?")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setWindowTitle("Qt Signals & Slots Demo")

    def btnClicked(self):
        button = self.sender()
        self.label.setText(f"You clicked {button.text()}")


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
    # app.setLightStyle()

    w = Form()
    w.setStyleSheet(loadStyleSheet())
    # w.setFont(app.getFont())
    w.show()

    return app.exec()


if __name__ == "__main__":
    main()
