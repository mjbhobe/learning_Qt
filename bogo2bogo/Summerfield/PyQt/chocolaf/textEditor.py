"""
* textEditor.py - simple text editor in PyQt
* @author: Manish Bhobe
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import os
import pathlib
import sys
import webbrowser

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[3], 'common_files'))
from pyqt5_utils import PyQtApp
import textEditor_rc


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.copiedtext = ""
        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.editorFont = QFont("Consolas", 12)
        self.textEdit.setFont(self.editorFont)
        self.setCentralWidget(self.textEdit)
        self.textEdit.setText(" ")

        exitAction = QAction(QIcon(':/edit_delete.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        newAction = QAction(QIcon(':/file_new.png'), 'New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New File')
        newAction.triggered.connect(self.__init__)

        openAction = QAction(QIcon(':/file_open.png'), 'Open...', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open File')
        openAction.triggered.connect(self.openo)

        saveAction = QAction(QIcon(':/file_save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save File')
        saveAction.triggered.connect(self.save)

        undoAction = QAction(QIcon(':/edit_undo.png'), 'Undo', self)
        undoAction.setShortcut('Ctrl+Z')
        undoAction.setStatusTip('Undo')
        undoAction.triggered.connect(self.textEdit.undo)

        redoAction = QAction(QIcon(':/edit_redo.png'), 'Redo', self)
        redoAction.setShortcut('Ctrl+Y')
        redoAction.setStatusTip('Redo')
        redoAction.triggered.connect(self.textEdit.redo)

        copyAction = QAction(QIcon(':/edit_copy.png'), 'Copy', self)
        copyAction.setShortcut('Ctrl+C')
        copyAction.setStatusTip('Copy')
        copyAction.triggered.connect(self.copy)

        pasteAction = QAction(QIcon(':/edit_paste.png'), 'Paste', self)
        pasteAction.setShortcut('Ctrl+V')
        pasteAction.setStatusTip('Paste')
        pasteAction.triggered.connect(self.paste)

        cutAction = QAction(QIcon(':/edit_cut.png'), 'Cut', self)
        cutAction.setShortcut('Ctrl+X')
        cutAction.setStatusTip('Cut')
        cutAction.triggered.connect(self.cut)

        aboutAction = QAction('About', self)
        aboutAction.setStatusTip('About')
        aboutAction.triggered.connect(self.about)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setStyleSheet("QMenuBar {background-color: rgb(25, 32, 48);}")

        fileMenu = menubar.addMenu('&File')
        fileMenu.setStyleSheet("QMenu {background-color: rgb(32, 32, 32);}")
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        fileMenu2 = menubar.addMenu('&Edit')
        fileMenu2.addAction(undoAction)
        fileMenu2.addAction(redoAction)
        editActions = fileMenu2.addMenu("&Actions...")
        editActions.addAction(cutAction)
        editActions.addAction(copyAction)
        editActions.addAction(pasteAction)
        # fileMenu2.addSeparator()
        # fileMenu2.addAction(cutAction)
        # fileMenu2.addAction(copyAction)
        # fileMenu2.addAction(pasteAction)

        fileMenu3 = menubar.addMenu('&Help')
        fileMenu3.addAction(aboutAction)

        tb1 = self.addToolBar('File')
        tb1.addAction(newAction)
        tb1.addAction(openAction)
        tb1.addAction(saveAction)

        tb2 = self.addToolBar('Edit')
        tb2.addAction(undoAction)
        tb2.addAction(redoAction)
        tb2.addAction(cutAction)
        tb2.addAction(copyAction)
        tb2.addAction(pasteAction)

        tb3 = self.addToolBar('Exit')
        tb3.addAction(exitAction)

        self.setGeometry(350, 150, 750, 600)
        self.setWindowTitle('Text Editor')
        self.setWindowIcon(QIcon(':/text_editor_icon.png'))
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit without Saving?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.statusBar().showMessage('Quiting...')
            event.accept()

        else:
            event.ignore()
            self.save()
            event.accept()

    def openo(self):
        self.statusBar().showMessage('Open Text Files ')
        docsPath = QStandardPaths.standardLocations(QStandardPaths.DocumentsLocation)
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            docsPath[-1], "Text Files (*.txt *.c *.cpp *.h *.hxx *.py *.java *.bat *.sh)")
        self.statusBar().showMessage('Open File')
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

    def save(self):
        self.statusBar().showMessage('Add extension to file name')
        fname = QFileDialog.getSaveFileName(self, 'Save File')
        data = self.textEdit.toPlainText()

        file = open(fname[0], 'w')
        file.write(data)
        file.close()

    def copy(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedtext = textSelected

    def paste(self):
        self.textEdit.append(self.copiedtext)

    def cut(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedtext = textSelected
        self.textEdit.cut()

    def about(self):
        QMessageBox.about(self, "About TextEditor",
                          "<b>TextEditor</b>: Simple text editor with PyQt")


if __name__ == '__main__':
    app = PyQtApp(sys.argv)
    app.setStyle("Chocolaf")

    ex = Example()
    sys.exit(app.exec())
