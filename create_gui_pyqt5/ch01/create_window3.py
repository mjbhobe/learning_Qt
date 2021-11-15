# create_window3.py - size window
import sys

from PyQt6.QtCore import (
    Qt, QSize
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton
)

class MainWindow(QMainWindow):
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
        self.button.clicked.connect(QApplication.instance().quit)
        self.setCentralWidget(self.button)

app = QApplication(sys.argv)
app.setFont(QApplication.font("QMenu"))

window = MainWindow()
window.show()

# run your application
app.exec()
