"""
* calendar.py: PyQt5 version of the Qt widgets analog clock demo
* @author: Manish Bhobe
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import os
import pathlib
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[3], 'common_files'))
from pyqt5_utils import PyQtApp


class AnalogClock(QWidget):
    def __init__(self, parent: QWidget = None):
        super(AnalogClock, self).__init__(parent)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.setWindowTitle("Analog Clock")
        self.resize(200, 200)
        self.pixMap = QPixmap(200, 200)
        self.pixMap.fill(QColor(Qt.transparent))
        self.update()
        self.timer.start(1000)

    def update(self):
        hourHand = [QPoint(7, 8), QPoint(-7, 8), QPoint(0, -40)]
        minuteHand = [QPoint(7, 8), QPoint(-7, 8), QPoint(0, -70)]

        hourColor = QColor(Qt.white)  # QColor(180, 142, 173)
        minuteColor = QColor(0, 235, 203, 115)
        side = min(self.width(), self.height())
        time = QTime.currentTime()

        painter = QPainter(self.pixMap)
        try:
            painter.begin(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.translate(self.width() // 2, self.height() // 2)
            painter.scale(side / 200.0, side / 200.0)

            # draw hour hand
            painter.setPen(Qt.NoPen)
            painter.setBrush(hourColor)
            painter.save()
            painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
            painter.drawConvexPolygon(*hourHand)
            painter.restore()

            # draw hour notches across analog clock face
            painter.setPen(hourColor)
            for i in range(12):
                painter.drawLine(88, 0, 96, 0)
                painter.rotate(30.0)

            # draw minute hand
            painter.setPen(Qt.NoPen)
            painter.setBrush(minuteColor)
            painter.save()
            painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
            painter.drawConvexPolygon(*minuteHand)
            painter.restore()

            # draw minute notches across clock face
            painter.setPen(minuteColor)

            for j in range(60):
                if j % 5 != 0:
                    painter.drawLine(92, 0, 96, 0)
                painter.rotate(6.0)
        finally:
            painter.end()
            self.repaint()

    def paintEvent(self, e: QPaintEvent) -> None:
        # print("in paintEvent", flush=True)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixMap)


def loadStyleSheet() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    print(f"loasStyleSteet() -> You are {here}")
    darkss_dir = os.path.join(here, "styles", "dark")
    sys.path.append(darkss_dir)
    import stylesheet_rc

    darkss_path = os.path.join(darkss_dir, "stylesheet.css")
    assert os.path.exists(darkss_path)
    print(f"LoasStyleSheet() -> loading dark stylesheet from {darkss_path}")
    stylesheet = ""
    with open(darkss_path, "r") as f:
        stylesheet = f.read()
    return stylesheet


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = PyQtApp(sys.argv)

    clock = AnalogClock()
    clock.setStyleSheet(loadStyleSheet())
    clock.move(100, 100)
    clock.show()

    rect = clock.geometry()
    clock1 = AnalogClock()
    clock1.move(rect.left() + rect.width() // 4 + 20, rect.top() + rect.height() + 10)
    clock1.show()

    return app.exec()


if __name__ == "__main__":
    main()
