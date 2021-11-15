# signals_and_slots4.py - temperature converter demo
import sys, random, platform

from PyQt5.QtCore import (
    Qt, QSize, PYQT_VERSION_STR
)
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton, QSpinBox, QLabel,
    QVBoxLayout, QHBoxLayout
)

SEED = 42
random.seed(SEED)
IS_PYQT6 = PYQT_VERSION_STR.startswith('6')

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6: Signals & Slots")
        self.label1 = QLabel("Celcius Temp: ")
        self.spinBox = QSpinBox()
        self.spinBox.setRange(-100,100)
        self.faren = QLabel("<html>&deg;Faren")
        self.version = QLabel(f"Built with Python {platform.python_version()} and PyQt {PYQT_VERSION_STR}")
        self.button = QPushButton('Quit!')
        self.button.setToolTip('Quit Application')

        # layout the controls
        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.label1)
        self.layout1.addWidget(self.spinBox)
        self.layout1.addWidget(self.faren)
        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.version)
        self.layout2.addStretch()
        self.layout2.addWidget(self.button)
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.layout1)
        self.layout.addLayout(self.layout2)
        self.setLayout(self.layout)

        # signals & slots
        self.button.clicked.connect(QApplication.instance().quit)
        self.spinBox.valueChanged.connect(self.convertTemp)

        # trigger the signal
        self.spinBox.setValue(32)

    def convertTemp(self):
        celcius = self.spinBox.value()
        faren = ((9.0/5.0) * celcius) + 32.0
        self.faren.setText(f"<html><b>{faren:.2f}</b> &deg;Farenheit</html>")


app = QApplication(sys.argv)
appFont = QApplication.font("QMenu")
# appFont.setPointSize(12)
app.setFont(appFont)

window = QMainWindow()
window.setWindowTitle('PyQt Temp Converter')
widget = MainWidget()
window.setCentralWidget(widget)
window.show()

# run your application
# if IS_PYQT6:
app.exec()
# else:
#     app.exec_()
