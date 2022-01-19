#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
* interestCalc.py: compound interest calculator exercise
* @author: Manish Bhobe
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import os
import pathlib
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[3], 'common_files'))
from pyqt5_utils import PyQtApp


class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.label1 = QLabel("Principal:")
        self.principal = QSpinBox()
        self.label2 = QLabel("Rate:")
        self.rate = QDoubleSpinBox()
        self.label3 = QLabel("Years:")
        self.years = QSpinBox()
        self.label4 = QLabel("Amount:")
        self.interest = QLabel("Final Amount")
        self.label4 = QLabel("Amount:")
        self.amount = QLabel("Final Amount")
        self.setupUi()

    def setupUi(self):
        self.principal.setPrefix("$")
        self.principal.setRange(1000, 100000)
        self.principal.setSingleStep(1000)
        self.principal.setValue(2000)
        self.label2 = QLabel("Rate:")
        self.rate = QDoubleSpinBox()
        self.rate.setSuffix("%")
        self.rate.setRange(0.01, 10.00)
        self.rate.setSingleStep(0.05)
        self.rate.setValue(5.25)
        self.label3 = QLabel("Years:")
        self.years = QComboBox()
        for i in range(1, 11):
            self.years.addItem(f"{i} years")
        self.years.setCurrentIndex(1)

        # layout in grid layout
        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.principal, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.rate, 1, 1)
        layout.addWidget(self.label3, 2, 0)
        layout.addWidget(self.years, 2, 1)
        layout.addWidget(self.label4, 3, 0)
        layout.addWidget(self.amount, 3, 1)
        self.setLayout(layout)

        # connect signals & slots
        self.principal.valueChanged.connect(self.calcInterest)
        self.rate.valueChanged.connect(self.calcInterest)
        self.years.currentIndexChanged.connect(self.calcInterest)
        # display initial calculation
        self.calcInterest()

        self.setWindowTitle(f"PyQt {PYQT_VERSION_STR} interest calculator")

    def calcInterest(self):
        p = float(self.principal.value())
        r = float(self.rate.value())
        y = self.years.currentIndex() + 1
        a = p * ((1 + (r / 100.0)) ** y)
        self.amount.setText(f"$ {a:.2f}")


def main():
    app = PyQtApp(sys.argv)
    # app.setLightStyle()

    w = Form()
    w.setFont(app.getFont())
    w.show()

    return app.exec()


if __name__ == "__main__":
    main()
