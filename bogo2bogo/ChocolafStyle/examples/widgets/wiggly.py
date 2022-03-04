"""
* wiggly.py - wiggly widget in a QDialog using Chocolaf theme
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

# sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[2], 'common_files'))
# from pyqt5_utils import PyQtApp
import chocolaf
from chocolaf.utils.pyqtapp import PyQtApp


class WigglyWidget(QWidget):
    def __init__(self, parent=None):
        super(WigglyWidget, self).__init__(parent)

        self.setBackgroundRole(QPalette.Midlight)
        self.setAutoFillBackground(True)

        newFont = self.font()
        newFont.setPointSize(newFont.pointSize() + 20)
        self.setFont(newFont)

        self.timer = QBasicTimer()
        self.text = ''

        self.step = 0
        self.timer.start(60, self)

    def paintEvent(self, event):
        sineTable = (0, 38, 71, 92, 100, 92, 71, 38, 0, -38, -71, -92, -100, -92, -71, -38)

        metrics = QFontMetrics(self.font())
        x = (self.width() - metrics.width(self.text)) / 2
        y = (self.height() + metrics.ascent() - metrics.descent()) / 2
        color = QColor()

        painter = QPainter(self)

        for i, ch in enumerate(self.text):
            index = (self.step + i) % 16
            color.setHsv((15 - index) * 16, 255, 191)
            painter.setPen(color)
            painter.drawText(x, y - ((sineTable[index] * metrics.height()) / 400), ch)
            x += metrics.width(ch)

    def setText(self, newText):
        self.text = newText

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.step += 1
            self.update()
        else:
            super(WigglyWidget, self).timerEvent(event)


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        wigglyWidget = WigglyWidget()
        lineEdit = QLineEdit()
        closeBtn = QPushButton("Close")
        closeBtn.clicked.connect(self.accept)

        hlayout = QHBoxLayout()
        hlayout.addWidget(lineEdit)
        hlayout.addWidget(closeBtn)

        layout = QVBoxLayout()
        layout.addWidget(wigglyWidget)
        # layout.addWidget(lineEdit)
        layout.addLayout(hlayout)
        self.setLayout(layout)

        lineEdit.textChanged.connect(wigglyWidget.setText)

        lineEdit.setText("PyQt5 with Chocolaf Theme")

        self.setWindowTitle("Wiggly")
        self.resize(650, 200)


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = PyQtApp(sys.argv)
    app.setStyle("Chocolaf")

    win = Dialog()
    win.move(100, 100)
    win.show()

    return app.exec()


if __name__ == "__main__":
    main()
