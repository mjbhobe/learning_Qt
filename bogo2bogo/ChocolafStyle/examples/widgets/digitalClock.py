"""
* digitalClock.py: PyQt5 version of Qt widgets digital clock using 
*    QLCDNumber widget and the Chocolaf theme & no titlebar
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

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[2], 'common_files'))
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
        self.resize(250, 150)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm")
        # simulate 'blinking' for every alternate click
        if ((time.second() % 2) == 0):
            text = ' '.join([text[:2], text[3:]])
        self.display(text)


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = PyQtApp(sys.argv)
    app.setStyle("Chocolaf")

    win = DigitalClock()
    # no titlebars - right click on Windows taskbar icon to close
    win.setWindowFlag(Qt.FramelessWindowHint)
    win.move(100, 100)
    win.show()

    return app.exec()


if __name__ == "__main__":
    main()
