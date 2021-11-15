# signals_and_slots3.py - one widget can throw multiple signals
import sys, random, platform

from PyQt5.QtCore import (
    Qt, QSize, PYQT_VERSION_STR
)
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QPushButton,
    QLabel, QFontComboBox, QHBoxLayout, QVBoxLayout
)

SEED = 42
random.seed(SEED)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Select Font:')
        self.fontCombo = QFontComboBox()
        self.pushButton = QPushButton("Press Me!")
        self.pushButton.setCheckable(True)
        # signals & Slots
        self.pushButton.clicked.connect(self.button_clicked)
        self.pushButton.clicked.connect(self.button_checked)
        self.setCentralWidget(self.pushButton)

    def button_clicked(self):
        print('Button was clicked')

    def button_checked(self, checked):
        print('Button checked? ', checked)

app = QApplication(sys.argv)
appFont = QApplication.font("QMenu")
# appFont.setPointSize(12)
app.setFont(appFont)

window = MainWindow()
window.setWindowTitle('PyQt Signals & Slots - 3')
window.show()

# run your application
app.exec()
