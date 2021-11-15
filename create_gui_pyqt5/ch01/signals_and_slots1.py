# signals_and_slots1.py - handling signale (button clicks)
import sys

from PyQt6.QtCore import (
    Qt, QSize
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton
)

class MainWindow(QMainWindow):
    checked = False

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6: app with custom QMainWindow")
        # set minimum size
        self.setMinimumSize(QSize(100,100))
        # initial size
        #self.setFixedSize(QSize(400,300))
        self.resize(400, 300)
        # set maximum size
        self.setMaximumSize(QSize(600,500))
        self.button = QPushButton('Click Me!')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.toggle_me)
        self.setCentralWidget(self.button)

    def toggle_me(self):
        if self.checked:
            self.button.setText('I am un-checked')
        else:
            self.button.setText('I am checked')

        self.checked = not self.checked

app = QApplication(sys.argv)
app.setFont(QApplication.font("QMenu"))

window = MainWindow()
window.show()

# run your application
app.exec()
