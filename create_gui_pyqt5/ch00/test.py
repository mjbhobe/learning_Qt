# test.py
import sys
#   from PyQt5.QtCore import *
from PyQt6.QtWidgets import  (QApplication, QWidget, QLineEdit,
    QPushButton, QHBoxLayout
)

def main():
    app = QApplication(sys.argv)
    app.setFont(QApplication.font("QMenu"))

    # create the gui
    window = QWidget()
    lineEdit = QLineEdit()
    button = QPushButton("Clear")
    layout = QHBoxLayout()
    layout.addWidget(lineEdit)
    layout.addWidget(button)

    # signals & slots
    button.clicked.connect(lineEdit.clear)

    window.setLayout(layout)
    window.setWindowTitle("Why?? (Python)")
    window.show()

    return app.exec()

if __name__ == "__main__":
  main()
