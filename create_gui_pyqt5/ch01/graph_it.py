# graph_it.py: plots in PyQt application
import sys, random

SEED = 42
random.seed(SEED)

from PyQt5.QtCore import (
    Qt, QSize, PYQT_VERSION_STR
)
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton, QSpinBox, QLabel,
    QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QPalette
import pyqtgraph as pg
import numpy as np

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        backColor = self.palette().color(QPalette.Window)

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground(backColor)
        self.pen = pg.mkPen(width=3, color=(0,128,255))
        self.celcius = np.arange(-100, 100, 10)
        self.farenheit = ((9.0/5.0) * self.celcius) + 32.0
        # draw a plot of celcius/farenheit
        self.graphWidget.plot(self.celcius, self.farenheit, pen=self.pen)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.graphWidget)
        self.setLayout(self.layout)


app = QApplication(sys.argv)
appFont = QApplication.font("QMenu")
appFont.setPointSize(12)
appFont.setFamily('Arial')
app.setFont(appFont)

window = QMainWindow()
window.setWindowTitle('PyQt Plot Example')
widget = MainWidget()
window.setCentralWidget(widget)
window.show()

# run your application
app.exec()
