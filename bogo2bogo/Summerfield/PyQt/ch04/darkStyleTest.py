#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
* darkStyleTest.py - test QDarkStyle
* @author: Manish Bhobe
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import sys
import os
import pathlib
import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[3], 'common_files'))
from mypyqt5_utils import PyQtApp

class Form(QWidget):
    def __init__(self):
        super(Form,self).__init__()
        self.browser = QTextBrowser()
        font = QFont("Consolas")
        font.setPixelSize(12)
        self.browser.setFont(font)
        self.lineEdit = QLineEdit("Type an expression & press Enter")
        self.lineEdit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)
        self.lineEdit.setFocus()
        self.lineEdit.returnPressed.connect(self.updateUi)
        self.resize(640, 480)
        self.setWindowTitle(f"PyQt {PYQT_VERSION_STR} Calculator")

    def updateUi(self):
        pass

def main():
    app = PyQtApp(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    w = Form()
    w.setFont(app.getFont())
    w.show()

    return app.exec()


if __name__ == "__main__":
    main()
