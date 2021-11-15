# textFinder.py - based on Online example from Qt Documentation
import sys
import os
import pathlib
import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# from PyQt6 import uic
from PySide2.QtUiTools import *

import TextFinderForm

uiLoader = QUiLoader()


class TextFinder(QWidget):
    def __init__(self):
        super(TextFinder, self).__init__()
        self.setWindowTitle(f'Text Finder Demo: PySide {PySide2.__version__}')
        p = pathlib.Path(__file__)
        uiFilePath = os.path.join(os.path.split(str(p))[0], "TextFinder.ui")
        # uiFilePath = os.path.join(str(p.parent[1]), "TextFinder.ui")
        #uic.loadUi(uiFilePath, self)
        self.ui = uiLoader.load(uiFilePath, self)
        self.loadTextFile()
        self.ui.findButton.clicked.connect(self.findButtonClicked)

    def loadTextFile(self):
        p = pathlib.Path(__file__)
        filePath = os.path.join(os.path.split(str(p))[0], "input.txt")
        with open(filePath, 'r') as f:
            lines = ''.join(f.readlines())  # convert list to str
            # lines = ''.join(lines)
            self.ui.textEdit.setText(lines)

    def findButtonClicked(self):
        # move text cursor to beginning of text file
        cursor = self.ui.textEdit.textCursor()
        cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor, 1)
        searchString = self.ui.findText.text()
        self.ui.textEdit.find(searchString)  # , QTextDocument.FindWholeWords)


def main():
    app = QApplication(sys.argv)
    font = QFont("SF UI Text", QApplication.font("QMenu").pointSize())
    app.setFont(font)  # QApplication.font("QMenu"))

    w = TextFinder()
    w.setFont(QApplication.font("QMenu"))
    w.show()

    return app.exec_()


if __name__ == "__main__":
    main()
