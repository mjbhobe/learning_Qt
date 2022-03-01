"""
* mainWindowApp.py: illustrates using QMainWindow class with Chocolaf
* @author (Chocolaf): Manish Bhobe
*
* PyQt demo code taken from https://github.com/baoboa/pyqt5/tree/master/examples/widgets
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import os
import pathlib
import sys
import logging

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[2], 'common_files'))
from pyqt5_utils import PyQtApp
# import textEditor_rc


class RegExpDialog(QDialog):
    MaxCaptures = 6

    def __init__(self, parent=None):
        super(RegExpDialog, self).__init__(parent)

        self.patternComboBox = QComboBox()
        self.patternComboBox.setEditable(True)
        self.patternComboBox.setSizePolicy(QSizePolicy.Expanding,
                                           QSizePolicy.Preferred)

        patternLabel = QLabel("&Pattern:")
        patternLabel.setBuddy(self.patternComboBox)

        self.escapedPatternLineEdit = QLineEdit()
        self.escapedPatternLineEdit.setReadOnly(True)
        palette = self.escapedPatternLineEdit.palette()
        palette.setBrush(QPalette.Base,
                         palette.brush(QPalette.Disabled, QPalette.Base))
        self.escapedPatternLineEdit.setPalette(palette)

        escapedPatternLabel = QLabel("&Escaped Pattern:")
        escapedPatternLabel.setBuddy(self.escapedPatternLineEdit)

        self.syntaxComboBox = QComboBox()
        self.syntaxComboBox.addItem("Regular expression v1", QRegExp.RegExp)
        self.syntaxComboBox.addItem("Regular expression v2", QRegExp.RegExp2)
        self.syntaxComboBox.addItem("Wildcard", QRegExp.Wildcard)
        self.syntaxComboBox.addItem("Fixed string", QRegExp.FixedString)

        syntaxLabel = QLabel("&Pattern Syntax:")
        syntaxLabel.setBuddy(self.syntaxComboBox)

        self.textComboBox = QComboBox()
        self.textComboBox.setEditable(True)
        self.textComboBox.setSizePolicy(QSizePolicy.Expanding,
                                        QSizePolicy.Preferred)

        textLabel = QLabel("&Text:")
        textLabel.setBuddy(self.textComboBox)

        self.caseSensitiveCheckBox = QCheckBox("Case &Sensitive")
        self.caseSensitiveCheckBox.setChecked(True)
        self.minimalCheckBox = QCheckBox("&Minimal")

        indexLabel = QLabel("Index of Match:")
        self.indexEdit = QLineEdit()
        self.indexEdit.setReadOnly(True)

        matchedLengthLabel = QLabel("Matched Length:")
        self.matchedLengthEdit = QLineEdit()
        self.matchedLengthEdit.setReadOnly(True)

        self.captureLabels = []
        self.captureEdits = []
        for i in range(self.MaxCaptures):
            self.captureLabels.append(QLabel("Capture %d:" % i))
            self.captureEdits.append(QLineEdit())
            self.captureEdits[i].setReadOnly(True)
        self.captureLabels[0].setText("Match:")

        checkBoxLayout = QHBoxLayout()
        checkBoxLayout.addWidget(self.caseSensitiveCheckBox)
        checkBoxLayout.addWidget(self.minimalCheckBox)
        checkBoxLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addWidget(patternLabel, 0, 0)
        mainLayout.addWidget(self.patternComboBox, 0, 1)
        mainLayout.addWidget(escapedPatternLabel, 1, 0)
        mainLayout.addWidget(self.escapedPatternLineEdit, 1, 1)
        mainLayout.addWidget(syntaxLabel, 2, 0)
        mainLayout.addWidget(self.syntaxComboBox, 2, 1)
        mainLayout.addLayout(checkBoxLayout, 3, 0, 1, 2)
        mainLayout.addWidget(textLabel, 4, 0)
        mainLayout.addWidget(self.textComboBox, 4, 1)
        mainLayout.addWidget(indexLabel, 5, 0)
        mainLayout.addWidget(self.indexEdit, 5, 1)
        mainLayout.addWidget(matchedLengthLabel, 6, 0)
        mainLayout.addWidget(self.matchedLengthEdit, 6, 1)

        for i in range(self.MaxCaptures):
            mainLayout.addWidget(self.captureLabels[i], 7 + i, 0)
            mainLayout.addWidget(self.captureEdits[i], 7 + i, 1)
        self.setLayout(mainLayout)

        self.patternComboBox.editTextChanged.connect(self.refresh)
        self.textComboBox.editTextChanged.connect(self.refresh)
        self.caseSensitiveCheckBox.toggled.connect(self.refresh)
        self.minimalCheckBox.toggled.connect(self.refresh)
        self.syntaxComboBox.currentIndexChanged.connect(self.refresh)

        self.patternComboBox.addItem("[A-Za-z_]+([A-Za-z_0-9]*)")
        self.textComboBox.addItem("(10 + delta4)* 32")

        self.setWindowTitle("RegExp")
        self.setFixedHeight(self.sizeHint().height())
        self.refresh()

    def refresh(self):
        self.setUpdatesEnabled(False)

        pattern = self.patternComboBox.currentText()
        text = self.textComboBox.currentText()

        escaped = str(pattern)
        escaped.replace('\\', '\\\\')
        escaped.replace('"', '\\"')
        self.escapedPatternLineEdit.setText('"' + escaped + '"')

        rx = QRegExp(pattern)
        cs = Qt.CaseSensitive if self.caseSensitiveCheckBox.isChecked() else Qt.CaseInsensitive
        rx.setCaseSensitivity(cs)
        rx.setMinimal(self.minimalCheckBox.isChecked())
        syntax = self.syntaxComboBox.itemData(self.syntaxComboBox.currentIndex())
        rx.setPatternSyntax(syntax)

        palette = self.patternComboBox.palette()
        if rx.isValid():
            palette.setColor(QPalette.Text,
                             self.textComboBox.palette().color(QPalette.Text))
        else:
            palette.setColor(QPalette.Text, Qt.red)
        self.patternComboBox.setPalette(palette)

        self.indexEdit.setText(str(rx.indexIn(text)))
        self.matchedLengthEdit.setText(str(rx.matchedLength()))

        for i in range(self.MaxCaptures):
            self.captureLabels[i].setEnabled(i <= rx.captureCount())
            self.captureEdits[i].setEnabled(i <= rx.captureCount())
            self.captureEdits[i].setText(rx.cap(i))

        self.setUpdatesEnabled(True)


if __name__ == '__main__':
    LOG_FILE_PATH = f"{__file__}.log"
    logging.basicConfig(filename=LOG_FILE_PATH, level=logging.DEBUG)
    app = PyQtApp(sys.argv)
    app.setStyle("Chocolaf")

    mainWin = RegExpDialog()
    mainWin.show()
    sys.exit(app.exec())
