#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ImageViewer.py: Image viewer application with PyQt
import sys
import os
import pathlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
# using qdarkstyle (@see: https://github.com/ColinDuquesnoy/QDarkStyleSheet)
import qdarkstyle
# to detect dark themes (@see: https://pypi.org/project/darkdetect/)
import darkdetect

# thisPath = pathlib.Path(__file__)
# print(thisPath.parents[0], thisPath.parents[1], os.path.join(thisPath.parents[1], 'common_files'))
sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common_files'))
import mypyqt5_utils as utils


class ImageViewer(QMainWindow):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.label = QLabel("")
        self.scrollArea = QScrollArea()
        self.image = None
        self.scaleFactor = 1.0
        self.firstDialog = True
        self.setupUi()

    def setupUi(self):
        self.label.setBackgroundRole(QPalette.Base)
        self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label.setScaledContents(True)

        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.label)
        self.scrollArea.setVisible(False)
        self.setCentralWidget(self.scrollArea)

        self.createActions()
        self.createMenu()
        self.createToolbar()
        # and status bar
        self.statusBar().showMessage(
            f"ImageViewer: developed with PyQt {PYQT_VERSION_STR} by Manish Bhobe")

        self.resize(QGuiApplication.primaryScreen().availableSize() * (3 / 5))
        self.setWindowIcon(self.iconFromName("ImageViewer-icon.png"))

    def iconFromName(self, imageName):
        p = pathlib.Path(__file__)
        iconPath = os.path.join(os.path.split(str(p))[0], "images", imageName)
        assert os.path.exists(iconPath), f"{iconPath} - icon does not exist!"
        return QIcon(iconPath)

    def createActions(self):
        # open image
        self.openAction = QAction("&Open...", self)
        self.openAction.setShortcut(QKeySequence.New)
        self.openAction.setIcon(self.iconFromName("open.png"))
        self.openAction.setStatusTip("Open a new image file to view")
        self.openAction.triggered.connect(self.open)

        # print image
        self.printAction = QAction("&Print...", self)
        self.printAction.setShortcut(QKeySequence.Print)
        self.printAction.setIcon(self.iconFromName("print.png"))
        self.printAction.setStatusTip("Print the current image")
        self.printAction.triggered.connect(self.print)
        self.printAction.setEnabled(False)

        # exit
        self.exitAction = QAction("E&xit", self)
        self.exitAction.setShortcut(QKeySequence("Ctrl+Q"))
        self.exitAction.setStatusTip("Exit the application")
        self.exitAction.triggered.connect(QApplication.instance().quit)

        # View category...
        self.zoomInAction = QAction("Zoom &in (25%)", self)
        self.zoomInAction.setShortcut(QKeySequence("Ctrl++"))
        self.zoomInAction.setIcon(self.iconFromName("zoom_in.png"))
        self.zoomInAction.setStatusTip("Zoom into the image by 25%")
        self.zoomInAction.triggered.connect(self.zoomIn)
        self.zoomInAction.setEnabled(False)

        self.zoomOutAction = QAction("Zoom &out (25%)", self)
        self.zoomOutAction.setShortcut(QKeySequence("Ctrl++"))
        self.zoomOutAction.setIcon(self.iconFromName("zoom_out.png"))
        self.zoomOutAction.setStatusTip("Zoom out of the image by 25%")
        self.zoomOutAction.triggered.connect(self.zoomOut)
        self.zoomOutAction.setEnabled(False)

        self.zoomNormalAction = QAction("&Normal size", self)
        self.zoomNormalAction.setShortcut(QKeySequence("Ctrl+0"))
        # self.zoomNormalAction.setIcon(QIcon("./images/zoom_out.png"))
        self.zoomNormalAction.setStatusTip("Zoom to normal size")
        self.zoomNormalAction.triggered.connect(self.zoomNormal)
        self.zoomNormalAction.setEnabled(False)

        self.fitToWindowAction = QAction("Fit to &window", self)
        self.fitToWindowAction.setShortcut(QKeySequence("Ctrl+1"))
        self.fitToWindowAction.setIcon(self.iconFromName("fit_to_size.png"))
        self.fitToWindowAction.setStatusTip("Fit image to size of window")
        self.fitToWindowAction.triggered.connect(self.fitToWindow)
        self.fitToWindowAction.setEnabled(False)
        self.fitToWindowAction.setCheckable(True)

        # Help category
        self.aboutAction = QAction("&About...", self)
        self.aboutAction.setStatusTip("Display about application information")
        self.aboutAction.triggered.connect(self.about)

        self.aboutQtAction = QAction("About &Qt...", self)
        self.aboutQtAction.setStatusTip(
            "Display information about Qt library being used")
        self.aboutQtAction.triggered.connect(QApplication.instance().aboutQt)

    def createMenu(self):
        # file menu
        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.printAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)

        # view menu
        viewMenu = self.menuBar().addMenu("View")
        viewMenu.addAction(self.zoomInAction)
        viewMenu.addAction(self.zoomOutAction)
        viewMenu.addAction(self.zoomNormalAction)
        viewMenu.addSeparator()
        viewMenu.addAction(self.fitToWindowAction)

        # help menu
        helpMenu = self.menuBar().addMenu("Help")
        helpMenu.addAction(self.aboutAction)
        helpMenu.addAction(self.aboutQtAction)

    def createToolbar(self):
        toolBar = self.addToolBar("Main")
        toolBar.addAction(self.openAction)
        toolBar.addAction(self.printAction)
        toolBar.addAction(self.zoomInAction)
        toolBar.addAction(self.zoomOutAction)
        toolBar.addAction(self.fitToWindowAction)

    def updateActions(self):
        self.fitToWindowAction.setEnabled(not (self.image is None))
        self.zoomInAction.setEnabled(not self.fitToWindowAction.isChecked())
        self.zoomOutAction.setEnabled(not self.fitToWindowAction.isChecked())
        self.zoomNormalAction.setEnabled(not self.fitToWindowAction.isChecked())

    def displayImageInfo(self):
        if self.image.isNull():
            return
        print(f"Image info -> width: {self.image.width()} - height: {self.image.height()} " +
              f"- bits/pixel: {self.image.depth()}")

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.label.resize(self.scaleFactor * self.label.pixmap().size())
        self.adjustScrollbar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollbar(self.scrollArea.verticalScrollBar(), factor)
        self.zoomInAction.setEnabled(self.scaleFactor < 5.0)
        self.zoomOutAction.setEnabled(self.scaleFactor > 0.10)
        print(f"Scalefactor = {self.scaleFactor}")

    def adjustScrollbar(self, scrollBar: QScrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value() +
                               ((factor - 1) * scrollBar.pageStep() / 2)))

    def initOpenDialog(self, dialog: QFileDialog, acceptMode: QFileDialog.AcceptMode):
        picLocations = QStandardPaths.standardLocations(QStandardPaths.PicturesLocation)
        # print(f"Standard pic locations: {picLocations}")
        dialog.setDirectory(QDir.currentPath if len(picLocations) == 0 else picLocations[-1])
        supportedMimeTypes = (QImageReader.supportedMimeTypes() if acceptMode == QFileDialog.AcceptMode.AcceptOpen
                              else QImageWriter.supportedMimeTypes())
        mimeTypeFilters = [str(mimeTypeName, 'utf-8') for mimeTypeName in supportedMimeTypes]
        mimeTypeFilters = sorted(mimeTypeFilters)
        dialog.setMimeTypeFilters(mimeTypeFilters)
        dialog.selectMimeTypeFilter("image/jpeg")
        dialog.setAcceptMode(acceptMode)
        if (acceptMode == QFileDialog.AcceptMode.AcceptSave):
            dialog.setDefaultSuffix("jpg")

    def loadImage(self, filePath):
        assert os.path.exists(filePath), f"FATAL: could not load file {filePath}"
        reader = QImageReader(filePath)
        reader.setAutoTransform(True)
        self.image = reader.read()
        if self.image is None:
            QMessageBox.error(self, "ImageViewer", f"Could not load {filePath}")
            return False

        self.scaleFactor = 1.0
        self.scrollArea.setVisible(True)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.adjustSize()
        self.setWindowTitle(f"PyQt {PYQT_VERSION_STR} Image Viewer: {filePath}")
        return True

    def open(self):
        openDialog = QFileDialog(self, "Open Image")
        self.initOpenDialog(openDialog, QFileDialog.AcceptMode.AcceptOpen)
        if openDialog.exec():
            filePath = list(openDialog.selectedFiles())[-1]
            if self.loadImage(filePath):
                self.updateActions()
                self.displayImageInfo()

    def print(self):
        QMessageBox.information(self, "ImageViewer",
                                "This is the 'print' action handler - yet to be implemented")

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.75)

    def zoomNormal(self):
        self.label.adjustSize()
        self.scaleFactor = 1.0

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAction.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.zoomNormal()
        self.updateActions()

    def about(self):
        QMessageBox.about(self, "About Image Viewer",
                          f"<p><b>Image Viewer</b> application to view images on desktop.</p>"
                          f"<p>Developed with PyQt {PYQT_VERSION_STR} by Manish Bhobe</p>"
                          f"<p>Free to use, but use at your own risk!!")


def setDarkPalette(app: QApplication) -> None:
    # Now use a palette to switch to dark colors:
    # @see for example: https://stackoverflow.com/questions/48256772/dark-theme-for-qt-widgets
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)


def main():
    app = QApplication(sys.argv)
    app.setFont(QApplication.font("QMenu"))
    app.setStyle("Fusion")
    if darkdetect.isDark():
        # apply dark stylesheet
        # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        utils.setDarkPalette(app)

    w = ImageViewer()
    w.setWindowTitle(f"PyQt {PYQT_VERSION_STR} Image Viewer")
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
