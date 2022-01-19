import sys, os
import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QWidget):
    def __init__(self):
        super(Form,self).__init__()
        self.label = QLabel(f"Hello, welcome to Qt GUI programming with {PYQT_VERSION_STR}")
        self.btn = QPushButton("Quit!")
        self.btn.setToolTip("Quit application")
        self.btn.clicked.connect(qApp.quit)
        lay1 = QHBoxLayout()
        lay1.addWidget(self.label)
        lay1.addWidget(self.btn)
        lay2 = QVBoxLayout()
        lay2.addLayout(lay1)
        self.setLayout(lay2)
        self.setWindowTitle("Hello PyQt")
        

def main():
    app = QApplication(sys.argv)
    app.setFont(app.font("QMenu"))
    ss = qdarkstyle.load_stylesheet()
    ss += "\nQPushButton{min-height:1.5em; min-width:5em}"
    app.setStyleSheet(ss)

    w = Form()
    w.show()

    return app.exec()

if __name__ == '__main__':
    main()
