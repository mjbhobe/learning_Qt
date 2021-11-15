# -*- coding: utf-8 -*-
"""
// ============================================================================
// mainWindow.py: custom QMainWindow derived class for main window
//
// Tutorial - PyQt5 Doodle Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL) 
// @author: Manish Bhobe
// My experiments with the Qt Framework. Use at your own risk!!
// ============================================================================
"""
import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from drawWindow import DrawWindow
from doodle import Doodle

WinTitle = "PyQt5 Doodle - Step08: Separating the Doodle"

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle(WinTitle)
        self.setWindowIcon(QIcon("./icons/32x32/painting.png"))
        self.setGeometry(QRect(100, 100, 640, 480))
        self.drawWindow = DrawWindow()
        self.setCentralWidget(self.drawWindow)
        self.setupActions()
        self.setupMenubar()
        self.setupToolbar()
        self.statusBar().showMessage("PyQt5 Doodle: random doodling application by Manish Bhobe")

    def setupActions(self):
        self.fileNewAction = QAction(QIcon("./icons/32x32/new.png"), "&New Doodle", self)
        self.fileNewAction.setShortcut(QKeySequence.New)
        self.fileNewAction.setToolTip("New Doodle")
        self.fileNewAction.setStatusTip("Create a new doodle")
        self.fileNewAction.triggered.connect(self.fileNew)

        self.fileOpenAction = QAction(QIcon("./icons/32x32/open.png"), "&Open Doodle...", self)
        self.fileOpenAction.setShortcut(QKeySequence.Open)
        self.fileOpenAction.setToolTip("Open Doodle")
        self.fileOpenAction.setStatusTip("Open existing doodle file")
        self.fileOpenAction.triggered.connect(self.fileOpen)

        self.fileSaveAction = QAction(QIcon("./icons/32x32/save.png"), "&Save Doodle", self)
        self.fileSaveAction.setShortcut(QKeySequence.Save)
        self.fileSaveAction.setToolTip("Save Doodle")
        self.fileSaveAction.setStatusTip("Save existing doodle file")
        self.fileSaveAction.triggered.connect(self.fileSave)

        self.fileSaveAsAction = QAction(QIcon("./icons/32x32/save_as.png"), "Save Doodle &as...", self)
        self.fileSaveAsAction.setShortcut(QKeySequence.SaveAs)
        self.fileSaveAsAction.setToolTip("Save Doodle As")
        self.fileSaveAsAction.setStatusTip("Save Doodle to another file")
        self.fileSaveAsAction.triggered.connect(self.fileSaveAs)

        self.exitAction = QAction("E&xit", self)
        self.exitAction.setToolTip("Exit Application")
        self.exitAction.setStatusTip("Save any pending changes & exit application")
        self.exitAction.triggered.connect(self.fileExit)

        self.penWidthAction = QAction(QIcon("./icons/32x32/line-width.png"), "&Choose Pen Thickness...", self)
        self.penWidthAction.setShortcut("Ctrl+T")
        self.penWidthAction.setToolTip("Pen Thickness")
        self.penWidthAction.setStatusTip("Choose Pen Thickness")
        self.penWidthAction.triggered.connect(self.changePenWidth)

        self.penColorAction = QAction(QIcon("./icons/32x32/pen-color.png"), "&Choose Pen Color...", self)
        self.penColorAction.setShortcut("Ctrl+L")
        self.penColorAction.setToolTip("Pen Color")
        self.penColorAction.setStatusTip("Choose Pen Color")
        self.penColorAction.triggered.connect(self.changePenColor)

        self.aboutAction = QAction("About...", self)
        self.aboutAction.setToolTip("About Doodle...")
        self.aboutAction.setStatusTip("Display Information about application")
        self.aboutAction.triggered.connect(self.helpAbout)


    def setupMenubar(self):
        fileMenu = QMenu("&File", self)
        fileMenu.addAction(self.fileNewAction)
        fileMenu.addAction(self.fileOpenAction)
        fileMenu.addAction(self.fileSaveAction)
        fileMenu.addAction(self.fileSaveAsAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)

        optionsMenu = QMenu("&Options", self)
        optionsMenu.addAction(self.penWidthAction)
        optionsMenu.addAction(self.penColorAction)

        helpMenu = QMenu("&Help", self)
        helpMenu.addAction(self.aboutAction)

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addMenu(optionsMenu)
        self.menuBar().addMenu(helpMenu)

    def setupToolbar(self):
        toolBar = QToolBar("Main", self)
        toolBar.addAction(self.fileNewAction)
        toolBar.addAction(self.fileOpenAction)
        toolBar.addAction(self.fileSaveAction)
        toolBar.addAction(self.fileSaveAsAction)
        toolBar.addSeparator()
        toolBar.addAction(self.penWidthAction)
        toolBar.addAction(self.penColorAction)

        self.addToolBar(toolBar)

    def fileNew(self):
        QMessageBox.information(self, "File New",
            "You selected the New Doodle option", QMessageBox.Ok)

    def fileOpen(self):
        currDir = os.getcwd()
        fname = QFileDialog.getOpenFileName(self, 'Open Doodle', currDir)
        if fname[0]:
            QMessageBox.information(self, "File Open",
                f"You selected {fname[0]}", QMessageBox.Ok)

    def fileSave(self):
        QMessageBox.information(self, "File Save",
            "You selected the File Save option", QMessageBox.Ok)

    def fileSaveAs(self):
        QMessageBox.information(self, "File Save As",
            "You selected the File Save As option", QMessageBox.Ok)

    def fileExit(self):
        qDebug("File + Exit selected....")
        #QApplication.instance().close()
        self.close()

    def changePenWidth(self):
        newWidth, ok = QInputDialog.getInt(self, "Pen Width",
                            "Enter new pen width (2-12):",
                            self.drawWindow.doodle.defPenWidth, 2, 12)
        if ok:  # user clicked Ok on QInputDialog
            self.drawWindow.doodle.defPenWidth = newWidth
            
    def changePenColor(self):
        newColor = QColorDialog.getColor(self.drawWindow.doodle.defPenColor, self)
        if newColor.isValid():
            self.drawWindow.doodle.defPenColor = newColor

    def helpAbout(self):
        about = QMessageBox.information(self, "About PyDoodle...",
            "PyQt Doodle - random doodles.\n" + "\n" +
            "Developed using PyQt5 GUI Library for Python\n" +
            "Created by Manish Bhobe",
            QMessageBox.Ok)
        #about.setIcon(QIcon("./icons/32x32/painting.png"))
        #about.show()

    # operating system Events
    def closeEvent(self, e):
        """ called just before the main window closes """
        qDebug("In mainWindow.closeEvent(...) handler")
        if self.drawWindow.doodle.modified:
            resp = QMessageBox.question(self, "Confirm Close",
                                        "This will close the application.\nOk to quit?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if resp == QMessageBox.Yes:
                e.accept()
            else:
                e.ignore()
        else:
            e.accept()