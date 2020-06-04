"""
// ============================================================================
// line.py: represents one line in the Doodle, with its own color & width
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

class Line(QObject):
    def __init__(self, penWidth=3, penColor=QColor(qRgb(0,65,255))):
        super(QObject, self).__init__()
        self.penWidth = min(max(2, penWidth), 12)
        self.penColor = penColor
        self.points = []

    def setPenWidth(self, penWidth):
        newWidth = min(max(2, penWidth), 12)
        if self.penWidth != newWidth:
            self.penWidth = newWidth

    def setPenColor(self, penColor):
        self.penColor = penColor

    def numPoints(self):
        return len(self.points)

    def append(self, pt: QPoint) -> None:
        self.points.append(pt)

    def draw(self, painter: QPainter) -> None:
        if self.numPoints() > 0:
            pen = QPen(self.penColor, self.penWidth)
            painter.setPen(pen)
            lastPt = None
            for i, pt in enumerate(self.points):
                if i > 0:
                    painter.drawLine(lastPt, pt)
                lastPt = pt
