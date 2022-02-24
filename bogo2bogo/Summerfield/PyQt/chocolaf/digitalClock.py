"""
* digitalClock.py: digital clock using QLCDNumber widget
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


class DigitalClock(QLCDNumber):
    def __init__(self, parent: QWidget = None):
        super(DigitalClock, self).__init__(parent)
        self.setSegmentStyle(QLCDNumber.Filled)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)   # trigger every second
        self.showTime()

        self.setWindowTitle("Digital Clock")
        self.resize(150, 60)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm")
        # simulate 'blinking' for every alternate click
        if ((time.second() % 2) == 0):
            text = ' '.join([text[:2], text[3:]])
        self.display(text)


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

    win = DigitalClock()
    # use chocolaf stylesheet
    win.setStyleSheet(app.getStyleSheet("Chocolaf"))
    win.move(100, 100)
    win.show()

    rect = win.geometry()
    win1 = DigitalClock()   # will use QDarkStyle
    win1.setStyleSheet(app.getStyleSheet("QDarkStyle-dark"))
    win1.move(rect.left() + rect.width() // 4 + 20, rect.top() + rect.height() + 10)
    win1.show()

    return app.exec()


if __name__ == "__main__":
    main()
