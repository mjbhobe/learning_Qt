#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HelloWorld.py - hello world
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# using qdarkstyle (@see: https://github.com/ColinDuquesnoy/QDarkStyleSheet)
import qdarkstyle
# to detect dark themes (@see: https://pypi.org/project/darkdetect/)
import darkdetect


class HelloWorld(QWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.label = QLabel(f"Hello World! Welcome to GUI programming with PyQt {PYQT_VERSION_STR}")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.setWindowTitle("Hello World!")


def main():
    app = QApplication(sys.argv)
    app.setFont(QApplication.font("QMenu"))
    app.setStyle("Fusion")
    if darkdetect.isDark():
        # apply dark stylesheet
        app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        # setDarkPalette(app)

    w = HelloWorld()
    w.show()

    return app.exec()


if __name__ == '__main__':
    main()
