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
        self.setWindowTitle("PyQt5 Doodle - Step04: Drawing lines")
        self.setStyleSheet("background-color: white")
        self.setGeometry(QRect(100,100,640,480))
        self.modified = False
        self.image = QImage()
        self.points = []
        self.dragging = False
        self.penColor = QColor(qRgb(0, 65, 255))
        self.penWidth = 3
        self.setMouseTracking(True)

    def drawLine(self, painter):
        if len(self.points) > 0:
            #print(f"In drawLine() function - drawing points {self.points}")
            pen = QPen(self.penColor, self.penWidth)
            painter.setPen(pen)
            lastPt = None
            for i, pt in enumerate(self.points):
                if i > 0:
                    painter.drawLine(lastPt, pt)
                lastPt = pt

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

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.drawLine(painter)
        painter.end()

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            # clear out any line drawn
            self.points = []
            self.update()
            # start a new line
            pt = QPoint(e.pos().x(), e.pos().y())
            #print(f"Got mousePressEvent at ({pt.x()}, {pt.y()})")
            self.points.append(pt)
            self.modified = True
            self.dragging = True
        elif e.button() == Qt.RightButton:
            self.points = []
            self.modified = False
            self.update()

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        if (e.buttons() == Qt.LeftButton):
            pt = QPoint(e.pos().x(), e.pos().y())
            #print(f"Got mouseMoveEvent event at ({pt.x()}, {pt.y()})")
            self.points.append(pt)
            self.update()
        else:
            e.accept()

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if (e.button() == Qt.LeftButton) and (self.dragging):
            pt = QPoint(e.pos().x(), e.pos().y())
            self.points.append(pt)
            #print(f"Got mouseReleaseEvent event at ({pt.x()}, {pt.y()})")
            self.dragging = False
            self.update()
        else:
            e.accept()
