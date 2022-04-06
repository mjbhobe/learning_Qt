#!/usr/bin/env python
import sys, random

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self, parent: QWidget = None):
        super(MyWidget, self).__init__(parent)

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.label = QLabel("Hello World")
        self.setMinimumSize(200, 150)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.magic)
    
        # layout the controls
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.setWindowTitle(f"PyQt {PYQT_VERSION_STR} Magic")
        

    def magic(self):
        self.label.setText(random.choice(self.hello))


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # create & show the GUI
    win = MyWidget()
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    