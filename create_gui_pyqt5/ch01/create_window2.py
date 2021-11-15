# create_window.py
import sys

from PyQt6.QtCore import (
    Qt, QSize
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6: app with custom QMainWindow")
        self.setGeometry(50, 50, 640, 480)
        self.button = QPushButton('Click Me!')
        self.button.clicked.connect(QApplication.instance().quit)
        self.setCentralWidget(self.button)

app = QApplication(sys.argv)
app.setFont(QApplication.font("QMenu"))

window = MainWindow()
window.show()

# run your application
app.exec()
