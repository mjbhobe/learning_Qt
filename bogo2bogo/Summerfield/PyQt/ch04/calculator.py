#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
* calculator.py - Python expression evaluator/calculator
* @author: Manish Bhobe
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import math
import os
import pathlib
import sys

import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[3], 'common_files'))
from pyqt5_utils import PyQtApp


class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.browser = QTextBrowser()
        x = math.sin(20)
        y = np.arange(10)
        font = QFont("Consolas")
        font.setPointSize(11)
        self.browser.setFont(font)
        self.lineEdit = QLineEdit("Type an expression & press Enter")
        self.quitBtn = QPushButton("Quit!")
        self.lineEdit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout2 = QHBoxLayout()
        layout2.addWidget(self.lineEdit)
        layout2.addWidget(self.quitBtn)
        layout.addLayout(layout2)
        self.setLayout(layout)
        self.lineEdit.setFocus()
        self.lineEdit.returnPressed.connect(self.updateUi)
        self.quitBtn.clicked.connect(qApp.quit)
        self.resize(640, 480)
        self.setWindowTitle(f"PyQt {PYQT_VERSION_STR} Calculator")

    def updateUi(self):
        try:
            text = self.lineEdit.text()
            self.browser.append(f"{text} = <b>{eval(text)}</b>")
        except:
            self.browser.append(f"<font color=red>{text} is invalid!</font>")


def main():
    app = PyQtApp(sys.argv)

    w = Form()
    w.setFont(app.getFont())
    w.show()

    return app.exec()


if __name__ == "__main__":
    main()
