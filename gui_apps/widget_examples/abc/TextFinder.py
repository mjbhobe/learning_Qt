# textFinder.py - based on Online example from Qt Documentation
import sys
import os
import pathlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import TextFinderForm


class TextFinder(QWidget):
    def __init__(self):
        super(TextFinder, self).__init__()
        p = pathlib.Path(__file__)
        uiFilePath = os.path.join(os.path.split(str(p))[0], "TextFinder.ui")
        # uiFilePath = os.path.join(str(p.parent[1]), "TextFinder.ui")
        uic.loadUi(uiFilePath, self)


def main():
    app = QApplication(sys.argv)
    app.setFont(QApplication.font("QMenu"))

    w = TextFinder()
    w.setFont(QApplication.font("QMenu"))
    w.show()

    return app.exec()


if __name__ == "__main__":
    main()
