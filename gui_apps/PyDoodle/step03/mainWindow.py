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


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle("PyQt5 Doodle - Step03: Drawing points")
        #self.setGeometry(QRect(100, 100, 640, 480))
        self.resize(QGuiApplication.primaryScreen().availableSize() * 4 / 5)
        self.modified = False
        self.points = []

    # operating system Events
    def closeEvent(self, e):
        if self.modified:
            resp = QMessageBox.question(self, "Confirm Close",
                                        "This will close the application.\nOk to quit?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if resp == QMessageBox.Yes:
                e.accept()
            else:
                e.ignore()
        else:
            e.accept()

    def paintEvent(self, e: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        try:
            font = QFont("monospace", 11)
            painter.setFont(font)

            if len(self.points) > 0:
                for pt in self.points:
                    pos = f"({pt.x()},{pt.y()})"
                    painter.drawText(pt.x(), pt.y(), pos)
        finally:
            painter.end()

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            # user pressed left mouse button - display point where
            # the mouse left button was clicked
            pt = QPoint(e.pos().x(), e.pos().y())
            self.points.append(pt)
            self.modified = True
        elif e.button() == Qt.RightButton:
            # user pressed right mouse button - clear display of
            # previous left mouse clicks, if any
            self.points = []
            self.modified = False

        # force repaint NOW!
        self.update()
