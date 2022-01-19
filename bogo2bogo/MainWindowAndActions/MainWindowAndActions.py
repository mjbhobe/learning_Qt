#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SigSlots.py - signals & slots
import os
import pathlib
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *

sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common_files'))
from pyqt5_utils import PyQtApp


class Dialog(QDialog):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        p = pathlib.Path(__file__)
        uiFilePath = os.path.join(os.path.split(str(p))[0], "dialog.ui")
        self.ui = uic.loadUi(uiFilePath, self)
        self.setupUi()

    def setupUi(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        p = pathlib.Path(__file__)
        uiFilePath = os.path.join(os.path.split(str(p))[0], "mainwindow.ui")
        self.ui = uic.loadUi(uiFilePath, self)
        self.setupUi()

    def setupUi(self):
        self.ui.actionNewWindow.triggered.connect(self.newWindow)

    def newWindow(self):
        dlg = Dialog(self)
        dlg.setFont(QApplication.font("QMenu"))
        dlg.ui.label.setText("I am a modal dialog")
        dlg.setModal(True)
        dlg.exec()


def main():
    app = PyQtApp(sys.argv)

    # create the main main window
    mainWin = MainWindow()
    mainWin.setFont(app.getFont())
    mainWin.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
