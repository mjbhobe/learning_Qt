# -*- coding: utf-8 -*-
# textFinder.py - based on Online example from Qt Documentation
import sys
import os
import pathlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
# to detect dark themes (@see: https://pypi.org/project/darkdetect/)
import darkdetect

sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common_files'))
import mypyqt5_utils as utils

import TextFinderForm


class TextFinder(QWidget):
    def __init__(self):
        super(TextFinder, self).__init__()
        # self.setWindowTitle(f'Text Finder Demo: PySide {PySide2.__version__}')
        self.setWindowTitle(f'Text Finder Demo: PyQt {PYQT_VERSION_STR}')
        p = pathlib.Path(__file__)
        uiFilePath = os.path.join(os.path.split(str(p))[0], "TextFinder.ui")
        # uiFilePath = os.path.join(str(p.parent[1]), "TextFinder.ui")
        self.ui = uic.loadUi(uiFilePath, self)
        # self.ui = uiLoader.load(uiFilePath, self)
        self.loadTextFile()
        self.ui.textEdit.setEnabled(False)
        self.ui.findButton.setMinimumWidth(100)
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
    app.setStyle("Fusion")
    palSwitcher = utils.PaletteSwitcher(app)

    if darkdetect.isDark():
        #utils.setDarkPalette(app)
        palSwitcher.setDarkPalette()

    w = TextFinder()
    w.setFont(font)
    w.show()

    return app.exec_()


if __name__ == "__main__":
    main()
