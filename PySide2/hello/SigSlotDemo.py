# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class SigSlotDemoWindow(QMainWindow):
    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.label = QLabel("Click the button to see a fun message")
        self.btn = QPushButton("Click Me!")
        self.setupUi()

    def setupUi(self):
        layout1 = QHBoxLayout()
        layout1.addWidget(self.label)
        layout1.addWidget(self.btn)
        # self.layout = QVBoxLayout()
        # self.layout.addLayout(layout1)
        self.setLayout(layout1)
        self.setWindowTitle("Qt Signals & Slots")

        # setup signals & slots
        self.btn.clicked.connect(self.btnClicked)

    def btnClicked(self):
        msg = """This is a <b>PySide6</b> GUI application<br>
                 Created using Qt6 and PySide6<br/><br/>
                 Author: Manish Bhobe"""
        QMessageBox.information(self, "Fun Message", msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = SigSlotDemo()
    win.show()

    sys.exit(app.exec())
