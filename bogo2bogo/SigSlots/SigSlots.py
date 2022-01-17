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
# from mypyqt5_utils import ThemeSetter
from mypyqt5_utils import PaletteSwitcher

palSwitcher : PaletteSwitcher = None


class SigSlots(QMainWindow):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        p = pathlib.Path(__file__)
        uiFilePath = os.path.join(os.path.split(str(p))[0], "mainwindow.ui")
        self.ui = uic.loadUi(uiFilePath, self)
        self.setupUi()

    def setupUi(self):
        self.ui.slider.setValue(25)
        self.ui.qtVer.setText(f"Build with PyQt {PYQT_VERSION_STR}")


def main():
    app = QApplication(sys.argv)
    app.setFont(QApplication.font("QMenu"))
    app.setStyle("Fusion")
    palSwitcher = PaletteSwitcher(app)

    if darkdetect.isDark():
        #utils.setDarkPalette(app)
        #ThemeSetter.setDarkTheme(app)
        palSwitcher.setDarkPalette()

    w = SigSlots()
    w.show()

    return app.exec()


if __name__ == '__main__':
    main()
