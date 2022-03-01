"""
* scribble.py: PyQt version of the Qt Scribble application using Chocolaf theme
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
import unicodedata

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[2], 'common_files'))
from pyqt5_utils import PyQtApp
import textEditor_rc
import scribble_rc


class ScribbleArea(QWidget):
    def __init__(self, parent=None):
        super(ScribbleArea, self).__init__(parent)

        self.setAttribute(Qt.WA_StaticContents)
        # self.palette().color(QPalette.Dark)  # qRgba(255, 255, 255, 20)
        self.imageFillColor: QColor = qRgb(42, 42, 42)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 5
        self.myPenColor = Qt.blue
        self.image = QImage()
        self.lastPoint = QPoint()

    def openImage(self, fileName):
        loadedImage = QImage()
        if not loadedImage.load(fileName):
            return False

        newSize = loadedImage.size().expandedTo(self.size())
        self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            self.modified = False
            return True
        else:
            return False

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.image.fill(self.imageFillColor)
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
            self.scribbling = False

    def paintEvent(self, event):
        painter = QPainter(self)
        dirtyRect = event.rect()
        painter.drawImage(dirtyRect, self.image, dirtyRect)

    def resizeEvent(self, event):
        if self.width() > self.image.width() or self.height() > self.image.height():
            newWidth = max(self.width() + 128, self.image.width())
            newHeight = max(self.height() + 128, self.image.height())
            self.resizeImage(self.image, QSize(newWidth, newHeight))
            self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        painter = QPainter(self.image)
        drawPen = QPen(QBrush(self.myPenColor), self.myPenWidth, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        painter.setPen(drawPen)
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        rad = self.myPenWidth / 2 + 2
        self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.lastPoint = QPoint(endPoint)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        newImage = QImage(newSize, QImage.Format_RGB32)
        newImage.fill(self.imageFillColor)
        painter = QPainter(newImage)
        painter.drawImage(QPoint(0, 0), image)
        self.image = newImage

    def print_(self):
        printer = QPrinter(QPrinter.HighResolution)

        printDialog = QPrintDialog(printer, self)
        if printDialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.saveAsActs = []

        self.scribbleArea = ScribbleArea()
        self.setCentralWidget(self.scribbleArea)

        self.createActions()
        self.createMenus()
        self.createToolBar()

        self.setWindowTitle("Scribble")
        self.setWindowIcon(QIcon(":/painter_icon.png"))
        self.resize(640, 480)
        self.statusBar()
        self.readSettings()

    def readSettings(self):
        settings = QSettings("ChocoApps", "Chocolaf-Scribble")
        pos = settings.value("pos", QPoint(200, 200))
        size = settings.value("size", QSize(640, 480))
        # penWidth = settings.value("penWidth", 5)
        # self.scribbleArea.setPenWidth(penWidth)
        # penColor = settings.value("penColor", Qt.blue)
        # self.scribbleArea.setPenColor(penColor)
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        settings = QSettings("ChocoApps", "Chocolaf-Scribble")
        settings.setValue("pos", self.pos())
        settings.setValue("size", self.size())
        # settings.setValue("penWidth", self.scribbleArea.myPenWidth)
        # settings.setValue("penColor", self.scribbleArea.myPenColor)

    def closeEvent(self, event):
        if self.maybeSave():
            self.writeSettings()
            event.accept()
        else:
            event.ignore()

    def open(self):
        if self.maybeSave():
            fileName, _ = QFileDialog.getOpenFileName(self, "Open File",
                                                      QDir.currentPath())
            if fileName:
                self.scribbleArea.openImage(fileName)

    def save(self):
        action = self.sender()
        fileFormat = action.data()
        self.saveFile(fileFormat)

    def penColor(self):
        newColor = QColorDialog.getColor(self.scribbleArea.penColor())
        if newColor.isValid():
            self.scribbleArea.setPenColor(newColor)

    def penWidth(self):
        newWidth, ok = QInputDialog.getInt(self, "Scribble",
                                           "Select pen width:", self.scribbleArea.penWidth(), 1, 50, 1)
        if ok:
            self.scribbleArea.setPenWidth(newWidth)

    def about(self):
        QMessageBox.about(self, "About Scribble",
                          "<p>The <b>Scribble</b> example shows how to use "
                          "QMainWindow as the base widget for an application, and how "
                          "to reimplement some of QWidget's event handlers to receive "
                          "the events generated for the application's widgets:</p>"
                          "<p> We reimplement the mouse event handlers to facilitate "
                          "drawing, the paint event handler to update the application "
                          "and the resize event handler to optimize the application's "
                          "appearance. In addition we reimplement the close event "
                          "handler to intercept the close events before terminating "
                          "the application.</p>"
                          "<p> The example also demonstrates how to use QPainter to "
                          "draw an image in real time, as well as to repaint "
                          "widgets.</p>")

    def createActions(self):
        self.openAct = QAction(QIcon(":/file_open.png"), "&Open...", self, shortcut="Ctrl+O",
                               statusTip="Open scribble file", triggered=self.open)

        for format in QImageWriter.supportedImageFormats():
            format = str(format)

            text = format.upper() + "..."

            action = QAction(text, self, triggered=self.save)
            action.setData(format)
            self.saveAsActs.append(action)

        self.printAct = QAction(QIcon(":/file_print.png"), "&Print...", self,
                                statusTip="Print scribble file", triggered=self.scribbleArea.print_)

        self.exitAct = QAction(QIcon(":/on-off.png"), "E&xit", self, shortcut="Ctrl+Q",
                               statusTip="Quit application", triggered=self.close)

        self.penColorAct = QAction(QIcon(":/palette.png"), "&Pen Color...", self,
                                   statusTip="Choose pen color", triggered=self.penColor)

        self.penWidthAct = QAction(QIcon(":/pen.png"), "Pen &Width...", self,
                                   statusTip="Choose pen width", triggered=self.penWidth)

        self.clearScreenAct = QAction(QIcon(":/edit_delete.png"), "&Clear Screen", self, shortcut="Ctrl+L",
                                      statusTip="Clear the doodle & start over", triggered=self.scribbleArea.clearImage)

        self.aboutAct = QAction(
            "&About", self, statusTip="Display information about application", triggered=self.about)

        self.aboutQtAct = QAction(QIcon(":/qt_logo.png"), "About &Qt", self,
                                  statusTip="Display information about Qt framework used",
                                  triggered=QApplication.instance().aboutQt)

    def createMenus(self):
        self.saveAsMenu = QMenu("&Save As", self)
        for action in self.saveAsActs:
            self.saveAsMenu.addAction(action)

        fileMenu = QMenu("&File", self)
        fileMenu.addAction(self.openAct)
        fileMenu.addMenu(self.saveAsMenu)
        fileMenu.addAction(self.printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        optionMenu = QMenu("&Options", self)
        optionMenu.addAction(self.penColorAct)
        optionMenu.addAction(self.penWidthAct)
        optionMenu.addSeparator()
        optionMenu.addAction(self.clearScreenAct)

        helpMenu = QMenu("&Help", self)
        helpMenu.addAction(self.aboutAct)
        helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addMenu(optionMenu)
        self.menuBar().addMenu(helpMenu)

    def createToolBar(self):
        toolBar = self.addToolBar("Main")
        toolBar.addAction(self.openAct)
        toolBar.addAction(self.printAct)
        toolBar.addAction(self.penColorAct)
        toolBar.addAction(self.penWidthAct)
        toolBar.addAction(self.clearScreenAct)

    def maybeSave(self):
        if self.scribbleArea.isModified():
            ret = QMessageBox.warning(self, "Scribble",
                                      "The image has been modified.\n"
                                      "Do you want to save your changes?",
                                      QMessageBox.Save | QMessageBox.Discard |
                                      QMessageBox.Cancel)
            if ret == QMessageBox.Save:
                return self.saveFile('png')
            elif ret == QMessageBox.Cancel:
                return False

        return True

    def saveFile(self, fileFormat):
        initialPath = QDir.currentPath() + '/untitled.' + fileFormat

        fileName, _ = QFileDialog.getSaveFileName(self, "Save As", initialPath,
                                                  "%s Files (*.%s);;All Files (*)" % (fileFormat.upper(), fileFormat))
        if fileName:
            return self.scribbleArea.saveImage(fileName, fileFormat)

        return False


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = PyQtApp(sys.argv)
    app.setStyle("Chocolaf")

    win = MainWindow()
    win.move(100, 100)
    win.show()

    return app.exec()


if __name__ == "__main__":
    main()
