#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HelloWorld.py - hello world
import os
import pathlib
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# using qdarkstyle (@see: https://github.com/ColinDuquesnoy/QDarkStyleSheet)
# import qdarkstyle
# to detect dark themes (@see: https://pypi.org/project/darkdetect/)

sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common_files'))
from pyqt5_utils import PyQtApp


class HelloWorld(QWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.label = QLabel(f"Hello World! Welcome to Python GUI programming with PyQt {PYQT_VERSION_STR}")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.setWindowTitle("Hello World!")


def main():
    app = PyQtApp(sys.argv)

    w = HelloWorld()
    w.move(100, 100)
    w.show()

    return app.exec()


if __name__ == '__main__':
    main()
