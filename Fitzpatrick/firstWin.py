#!/usr/bin/env python

"""
# firstWin.py - my first PyQt application
#
# @author: Manish Bhobe
# My experiments with Python, PyQt, Data Science & ML
# Source code released for learning purposes only. Use at your own risk!!
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # create main window, with label as central widget
    win = QMainWindow()

    widget = QWidget()
    layout = QVBoxLayout()
    label = QLabel(f"Hello World! Welcome to PyQt {PYQT_VERSION_STR}")
    label.setAlignment(Qt.AlignCenter)
    win.setWindowTitle("Hello PyQt")
    layout.addWidget(label)
    widget.setLayout(layout)
    win.setCentralWidget(widget)
    win.show()

    # event loop
    return app.exec()

if __name__ == "__main__":
    main()
