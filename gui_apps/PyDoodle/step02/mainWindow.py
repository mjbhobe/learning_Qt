"""
// ============================================================================
// mainWindow.py: custom QMainWindow derived class for main window
//
// Tutorial - PyQt5 Doodle Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL) 
// @author: Manish Bhobe
// My experiments with the Qt Framework. Use at your own risk!!
// ============================================================================
"""
import sys
import os
import pathlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import darkdetect

sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common'))
import mypyqt5_utils as utils


class MainWindow(utils.PalMainWindow):
    def __init__(self, palSwitcher: utils.PaletteSwitcher):
        super(MainWindow, self).__init__(palSwitcher)
        self.setWindowTitle("PyQt5 Doodle - Step02: Handling Events")
        # self.setStyleSheet("background-color: white")
        self.setGeometry(QRect(100, 100, 640, 480))
    #     self.palSwitcher = palSwitcher
    #     self.timer = QTimer()
    #     self.timer.timeout.connect(self.switchPalette)
    #     self.timer.start(1000)

    # def switchPalette(self):
    #     if (darkdetect.isDark() and (not self.palSwitcher.isDarkPaletteInUse())) \
    #             or ((not darkdetect.isDark()) and self.palSwitcher.isDarkPaletteInUse()):
    #         self.palSwitcher.swapPalettes()

    # operating system Events
    def closeEvent(self, e: QCloseEvent) -> None:
        resp = QMessageBox.question(self, "Confirm Close",
                                    "This will close the application.\nOk to quit?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resp == QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            QMessageBox.information(self, "PyQt Doodle",
                                    "You have pressed the LEFT mouse button")
        elif e.button() == Qt.RightButton:
            QMessageBox.information(self, "PyQt Doodle",
                                    "You have pressed the RIGHT mouse button")
