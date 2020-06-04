"""
// ============================================================================
// drawWindow.py: custom QMainWindow derived class for main window
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// My experiments with the Qt Framework. Use at your own risk!!
// ============================================================================
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DrawWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("PyQt5 Doodle - Step02: Handling Events")
        self.setStyleSheet("background-color: white")
        self.setGeometry(QRect(100,100,640,480))

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
