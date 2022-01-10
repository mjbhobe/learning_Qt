#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Factorial.py: calculate factorials
import os
import pathlib
import platform
import sys

import darkdetect
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from scipy.special import factorial

sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common_files'))
#import mypyqt5_utils as utils
from mypyqt5_utils import ThemeSetter

class FactorialWidget(QWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.label = QLabel("Number:")
        self.number = QLineEdit("")
        self.calculate = QPushButton("Calculate")
        self.quit = QPushButton("Quit")
        self.factorial = QTextEdit("")
        self.setupUi()
        self.resize(640, 480)

    def setupUi(self):
        self.setWindowTitle(f"PyQt {PYQT_VERSION_STR} Factorial")

        layout1 = QHBoxLayout()
        layout1.addWidget(self.label)
        layout1.addWidget(self.number)
        layout1.addWidget(self.calculate)
        layout1.addWidget(self.quit)

        layout2 = QVBoxLayout()
        layout2.addLayout(layout1)
        layout2.addWidget(self.factorial)
        self.setLayout(layout2)

        self.calculate.setToolTip("Calculate factorial")
        self.calculate.setEnabled(False)
        self.calculate.setDefault(True)
        self.quit.setToolTip("Quit Application")
        self.factorial.setReadOnly(True)
        self.factorial.setEnabled(False)

        if (platform.system() in ['Windows']):
            # on Windows use Consolas
            font = QFont('Consolas')
            font.setPixelSize(12)
        else:
            # Mac or Linux
            mono = QFont('Monospace')
            font.setPixelSize(12)
            #font = QFont(mono.family(), mono.pointSize()-1)

        self.factorial.setFont(font)
        regExp = QRegExp("[1-9][0-9]{0,9}")
        self.number.setValidator(QRegExpValidator(regExp))

        # setup signals & slots
        self.number.textChanged.connect(self.textChanged)
        self.quit.clicked.connect(QApplication.instance().quit)
        self.calculate.clicked.connect(self.calculateFactorial)

    def textChanged(self, text):
        self.calculate.setEnabled(len(text.strip()) != 0)

    def calculateFactorial(self):
        self.factorial.clear()

        QApplication.setOverrideCursor(Qt.WaitCursor)
        num = int(self.number.text())
        fact = int(factorial(num, True))
        self.factorial.setText(str(fact))

        QApplication.restoreOverrideCursor()


def main():
    app = QApplication(sys.argv)
    app.setFont(QApplication.font("QMenu"))
    app.setStyle("Fusion")
    if darkdetect.isDark():
        ThemeSetter.setDarkTheme(app)

    w = FactorialWidget()
    w.setFont(QApplication.font("QMenu"))
    w.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
