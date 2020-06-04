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
from line import *

class DrawWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("PyQt5 Doodle - Step05: Drawing multiple lines")
        self.setStyleSheet("background-color: white")
        self.setGeometry(QRect(100,100,640,480))
        self.modified = False
        self.image = QImage()
        self.lines = []
        self.dragging = False
        self.penColor = QColor(qRgb(0, 65, 255))
        self.penWidth = 3
        self.currLine = None
        self.setMouseTracking(True)

    def drawLines(self, painter: QPainter) -> None:
        for line in self.lines:
            line.draw(painter)

    # operating system Events
    def closeEvent(self, e):
        """ called just before the main window closes """
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
        """ handler for paint events """
        painter = QPainter()
        painter.begin(self)
        self.drawLines(painter)
        painter.end()

    def mousePressEvent(self, e: QMouseEvent) -> None:
        """ handler for mouse press (left or right button) events """
        if e.button() == Qt.LeftButton:
            # start a new line
            self.currLine = Line(self.penWidth, self.penColor)
            self.lines.append(self.currLine)
            pt = QPoint(e.pos().x(), e.pos().y())
            #print(f"Got mousePressEvent at ({pt.x()}, {pt.y()})")
            self.currLine.append(pt)
            self.modified = True
            self.dragging = True
        elif e.button() == Qt.RightButton:
            for line in self.lines:
                line = None
            self.lines = []
            self.modified = False
            self.update()

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        """ handler for mouse drag (left or right button) events
            NOTE: you must call setMouseTracking(True) so window can receive mouse drag events
        """
        if (e.buttons() == Qt.LeftButton) and (self.dragging):
            assert self.currLine != None, "FATAL: self.currLine is None, when expecting valid!"
            pt = QPoint(e.pos().x(), e.pos().y())
            self.currLine.append(pt)
            self.update()
        else:
            e.accept()

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        """ handler for mouse (left or right button) released events """
        if (e.button() == Qt.LeftButton) and (self.dragging):
            assert self.currLine != None, "FATAL: self.currLine is None, when expecting valid!"
            pt = QPoint(e.pos().x(), e.pos().y())
            self.currLine.append(pt)
            #print(f"Got mouseReleaseEvent event at ({pt.x()}, {pt.y()})")
            self.dragging = False
            self.update()
        else:
            e.accept()

    def mouseDoubleClickEvent(self, e: QMouseEvent) -> None:
        """ handler for mouse double click events """
        if (e.button() == Qt.LeftButton):
            # left button double click - change pen newWidth
            newWidth, ok = QInputDialog.getInt(self, "Pen Width",
                                           "Enter new pen width (2-12):",
                                           self.penWidth, 2, 12)
            if ok:  # user clicked Ok on QInputDialog
                self.penWidth = newWidth
        elif (e.button() == Qt.RightButton):
            newColor= QColorDialog.getColor(self.penColor, self)
            if newColor.isValid():
                self.penColor = newColor
