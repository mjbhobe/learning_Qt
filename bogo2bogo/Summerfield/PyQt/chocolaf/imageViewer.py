"""
* imageViewer.py - simple image viewer application with Chocolaf
* @author: Manish Bhobe
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import os
import pathlib
import sys
import unicodedata

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[3], 'common_files'))
from pyqt5_utils import PyQtApp
import textEditor_rc


class ImageViewer(QMainWindow):
    def __init__(self):
        super(ImageViewer, self).__init__()

        self.printer = QPrinter()
        self.scaleFactor = 0.0

        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.setCentralWidget(self.scrollArea)

        self.createActions()
        self.createMenus()

        self.statusBar()

        self.setWindowTitle("Image Viewer")
        self.setWindowIcon(QIcon(":/image_viewer_icon.png"))
        self.readSettings()

    def open(self):
        picsPath = QStandardPaths.standardLocations(QStandardPaths.PicturesLocation)
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image", picsPath[-1],
                                                  "Image Files (*.png *.tiff *.jpg *.jpeg *.svg *.bmp)")
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer", f"Cannot load {fileName}.")
                return

            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0

            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.updateActions()

            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()

    def print_(self):
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.imageLabel.pixmap().size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabel.pixmap().rect())
            painter.drawPixmap(0, 0, self.imageLabel.pixmap())

    def readSettings(self):
        settings = QSettings("ChocoApps", "Chocolaf-ImageViewer")
        pos = settings.value("pos", QPoint(200, 200))
        size = settings.value("size", QSize(640, 480))
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        settings = QSettings("ChocoApps", "Chocolaf-ImageViewer")
        settings.setValue("pos", self.pos())
        settings.setValue("size", self.size())

    def closeEvent(self, event):
        self.writeSettings()
        event.accept()

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()
        self.updateActions()

    def about(self):
        QMessageBox.about(self, "About Image Viewer",
                          "<p>The <b>Image Viewer</b> example shows how to combine "
                          "QLabel and QScrollArea to display an image. QLabel is "
                          "typically used for displaying text, but it can also display "
                          "an image. QScrollArea provides a scrolling view around "
                          "another widget. If the child widget exceeds the size of the "
                          "frame, QScrollArea automatically provides scroll bars.</p>"
                          "<p>The example demonstrates how QLabel's ability to scale "
                          "its contents (QLabel.scaledContents), and QScrollArea's "
                          "ability to automatically resize its contents "
                          "(QScrollArea.widgetResizable), can be used to implement "
                          "zooming and scaling features.</p>"
                          "<p>In addition the example shows how to use QPainter to "
                          "print an image.</p>")

    def createActions(self):
        self.openAct = QAction(QIcon(":/file_open.png"), "&Open...", self, shortcut="Ctrl+O",
                               statusTip="Open an image file to view",
                               triggered=self.open)

        self.printAct = QAction(QIcon(":/file_print.png"), "&Print...", self, shortcut="Ctrl+P",
                                statusTip="Print the displayed image",
                                enabled=False, triggered=self.print_)

        self.exitAct = QAction(QIcon(":/on-off.png"), "E&xit", self, shortcut="Ctrl+Q",
                               statusTip="Quit the application",
                               triggered=self.close)

        self.zoomInAct = QAction(QIcon(":/zoomin.png"), "Zoom &In (25%)", self, shortcut="Ctrl++",
                                 statusTip="Zoom into the image by 25%",
                                 enabled=False, triggered=self.zoomIn)

        self.zoomOutAct = QAction(QIcon(":/zoomout.png"), "Zoom &Out (25%)", self, shortcut="Ctrl+-",
                                  statusTip="Zoom out of the image by 25%",
                                  enabled=False, triggered=self.zoomOut)

        self.normalSizeAct = QAction("&Normal Size", self, shortcut="Ctrl+0",
                                     statusTip="Zoom image to normal size",
                                     enabled=False, triggered=self.normalSize)

        self.fitToWindowAct = QAction(QIcon(":/zoom_to_fill.png"), "&Fit to Window", self, enabled=False,
                                      statusTip="Zoom image to fit the size of viewer",
                                      checkable=True, shortcut="Ctrl+F", triggered=self.fitToWindow)

        self.aboutAct = QAction(
            "&About", self, statusTip="Display information about application", triggered=self.about)

        self.aboutQtAct = QAction(QIcon(":/qt_logo.png"), "About &Qt", self,
                                  statusTip="Display information about Qt Framework used",
                                  triggered=QApplication.instance().aboutQt)

    def createMenus(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)

        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.viewMenu)
        self.menuBar().addMenu(self.helpMenu)

    def updateActions(self):
        self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                               + ((factor - 1) * scrollBar.pageStep() / 2)))


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = PyQtApp(sys.argv)
    app.setStyle("Chocolaf")

    win = ImageViewer()
    # win.setStyleSheet(app.getStyleSheet("Chocolaf"))
    win.move(100, 100)
    win.show()

    # rect = win.geometry()
    # win1 = Window()
    # win1.setStyleSheet(app.getStyleSheet("QDarkStyle-dark"))
    # win1.move(rect.left() + rect.width() // 4 + 20, rect.top() + rect.height() + 50)
    # win1.show()

    return app.exec()


if __name__ == "__main__":
    main()