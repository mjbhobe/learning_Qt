#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Widgets.py - signals & slots
import sys
import os
import pathlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import darkdetect

sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common_files'))
import mypyqt5_utils as utils

quotes = {
    'Nelson Mandela': 'The greatest glory in living lies not in never falling, but in rising every time we fall.',
    'Walt Disney': 'The way to get started is to quit talking and begin doing.',
    'Steve Jobs': 'Your time is limited, so don\'t waste it living someone else\'s life. Don\'t be trapped by dogma – which is living with the results of other people\'s thinking.',
    'Eleanor Roosevelt': 'If life were predictable it would cease to be life, and be without flavor.',
    'Oprah Winfrey': 'If you look at what you have in life, you\'ll always have more. If you look at what you don\'t have in life, you\'ll never have enough.',
    'James Cameron': 'If you set your goals ridiculously high and it\'s a failure, you will fail above everyone else\'s success.',
    'John Lennon': 'Life is what happens when you\'re busy making other plans.'
}


class WidgetsForm(QMainWindow):
    def __init__(self, parent: QWidget = None):
        super(WidgetsForm, self).__init__(parent)
        # load the UI
        p = pathlib.Path(__file__)
        uiFilePath = os.path.join(os.path.split(str(p))[0], "MainWindow.ui")
        self.ui = uic.loadUi(uiFilePath, self)
        self.setupUi()

    def setupUi(self):
        self.ui.closeButton.clicked.connect(QApplication.instance().exit)
        # add quotes to combobox
        for people in sorted(quotes.keys()):
            self.ui.quotesCombo.addItem(people)
        self.ui.quotesCombo.currentIndexChanged.connect(self.quoteChanged)
        for os_name in sorted(['Windows', 'MacOS', 'Ubuntu', 'Kubuntu', 'Chrome OS']):
            self.ui.osComboBox.addItem(os_name)
        self.ui.osComboBox.currentIndexChanged.connect(self.osNameChanged)
        self.ui.lineEdit.setEnabled(False)
        self.ui.quoteEdit.setEnabled(False)
        self.ui.horizontalSlider.setValue(25)
        self.ui.verticalSlider.setValue(75)
        self.ui.osComboBox.setCurrentIndex(1)
        self.ui.quotesCombo.setCurrentIndex(5)

    def quoteChanged(self, index):
        person = self.ui.quotesCombo.currentText()
        self.ui.quoteEdit.setText(f"<html>{quotes[person]} - <i>{person}</i></html>")

    def osNameChanged(self):
        os_name = self.ui.osComboBox.currentText()
        self.lineEdit.setText(f'You love {os_name}')


def main():
    app = QApplication(sys.argv)
    font = QFont("SF UI Text", QApplication.font("QMenu").pointSize())
    app.setFont(font)
    app.setStyle("Fusion")

    if darkdetect.isDark():
        utils.setDarkPalette(app)

    w = WidgetsForm()
    w.setFont(QFont(font.family(), font.pointSize() - 1))
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
