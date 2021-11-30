#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SigSlots.py - signals & slots
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


class Dialog(QDialog):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        p = pathlib.Path(__file__)
        uiFilePath = os.path.join(
            os.path.split(str(p))[0], "dialog.ui")
        self.ui = uic.loadUi(uiFilePath, self)
        self.setupUi()

    def setupUi(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        p = pathlib.Path(__file__)
        uiFilePath = os.path.join(
            os.path.split(str(p))[0], "mainwindow.ui")
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
    app = QApplication(sys.argv)
    app.setFont(QApplication.font("QMenu"))
    app.setStyle("Fusion")
    palSwitcher = utils.PaletteSwitcher(app)

    if darkdetect.isDark():
        # apply dark stylesheet
        # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        # utils.setDarkPalette(app)
        palSwitcher.setDarkPalette()

    # create the main main window
    mainWin = MainWindow()
    mainWin.setFont(QApplication.font("QMenu"))
    mainWin.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
