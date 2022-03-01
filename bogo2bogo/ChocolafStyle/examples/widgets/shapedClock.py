"""
* shapedClock.py: PyQt version of the ShapedClock Qt widgets application using Chocolaf style
* @author (Chocolaf): Manish Bhobe
*
* PyQt demo code taken from https://github.com/baoboa/pyqt5/tree/master/examples/widgets
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import os
import pathlib
import sys
import unicodedata

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[2], 'common_files'))
from pyqt5_utils import PyQtApp


class ShapedClock(QWidget):
    hourHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -40)
    ])

    minuteHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -70)
    ])

    hourColor = QColor(127, 0, 127)
    minuteColor = QColor(0, 127, 127, 191)

    def __init__(self, parent=None):
        super(ShapedClock, self).__init__(parent,
                                          Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

        quitAction = QAction("E&xit", self, shortcut="Ctrl+Q",
                             triggered=QApplication.instance().quit)
        self.addAction(quitAction)

        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setToolTip("Drag the clock with the left mouse button.\n"
                        "Use the right mouse button to open a context menu.")
        self.setWindowTitle(self.tr("Shaped Analog Clock"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        time = QTime.currentTime()

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(ShapedClock.hourColor)

        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(ShapedClock.hourHand)
        painter.restore()

        painter.setPen(ShapedClock.hourColor)

        for i in range(12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(ShapedClock.minuteColor)

        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(ShapedClock.minuteHand)
        painter.restore()

        painter.setPen(ShapedClock.minuteColor)

        for j in range(60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)

            painter.rotate(6.0)

    def resizeEvent(self, event):
        side = min(self.width(), self.height())

        maskedRegion = QRegion(self.width() / 2 - side / 2, self.height() / 2 - side / 2, side, side, QRegion.Ellipse)
        self.setMask(maskedRegion)

    def sizeHint(self):
        return QSize(250, 250)


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = PyQtApp(sys.argv)
    app.setStyle("Chocolaf")

    win = ShapedClock()
    win.move(100, 100)
    win.show()

    return app.exec()


if __name__ == "__main__":
    main()
