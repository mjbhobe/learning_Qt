# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from SigSlotDemo import SigSlotDemoWindow

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.label = QLabel(f"Hello PySide6")
        self.setupUi()

    def setupUi(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    window = SigSlotDemoWindow()
    window.show()
    sys.exit(app.exec())
