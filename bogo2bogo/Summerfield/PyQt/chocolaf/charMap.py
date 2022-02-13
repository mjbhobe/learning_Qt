"""
* charMap.py - character map, uses QComboBox & checkboxes
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

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[3], 'common_files'))
from pyqt5_utils import PyQtApp


def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider


class CharacterWidget(QWidget):

    characterSelected = pyqtSignal(str)

    def __init__(self, parent=None):
        super(CharacterWidget, self).__init__(parent)

        self.displayFont = QFont()
        self.squareSize = 24
        self.columns = 16
        self.lastKey = -1
        self.setMouseTracking(True)

    def updateFont(self, fontFamily):
        self.displayFont.setFamily(fontFamily)
        self.squareSize = max(24, QFontMetrics(self.displayFont).xHeight() * 3)
        self.adjustSize()
        self.update()

    def updateSize(self, fontSize):
        fontSize = int(fontSize)
        self.displayFont.setPointSize(fontSize)
        self.squareSize = max(24, QFontMetrics(self.displayFont).xHeight() * 3)
        self.adjustSize()
        self.update()

    def updateStyle(self, fontStyle):
        fontDatabase = QFontDatabase()
        oldStrategy = self.displayFont.styleStrategy()
        self.displayFont = fontDatabase.font(self.displayFont.family(),
                                             fontStyle, self.displayFont.pointSize())
        self.displayFont.setStyleStrategy(oldStrategy)
        self.squareSize = max(24, QFontMetrics(self.displayFont).xHeight() * 3)
        self.adjustSize()
        self.update()

    def updateFontMerging(self, enable):
        if enable:
            self.displayFont.setStyleStrategy(QFont.PreferDefault)
        else:
            self.displayFont.setStyleStrategy(QFont.NoFontMerging)
        self.adjustSize()
        self.update()

    def sizeHint(self):
        return QSize(self.columns * self.squareSize,
                     (65536 // self.columns) * self.squareSize)

    def mouseMoveEvent(self, event):
        widgetPosition = self.mapFromGlobal(event.globalPos())
        key = (widgetPosition.y() // self.squareSize) * self.columns + widgetPosition.x() // self.squareSize

        text = '<p>Character: <span style="font-size: 24pt; font-family: %s">%s</span><p>Value: 0x%x' % (
            self.displayFont.family(), self._chr(key), key)
        QToolTip.showText(event.globalPos(), text, self)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastKey = (event.y() // self.squareSize) * self.columns + event.x() // self.squareSize
            key_ch = self._chr(self.lastKey)

            if unicodedata.category(key_ch) != 'Cn':
                self.characterSelected.emit(key_ch)
            self.update()
        else:
            super(CharacterWidget, self).mousePressEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(event.rect(), Qt.white)
        painter.setFont(self.displayFont)

        redrawRect = event.rect()
        beginRow = redrawRect.top() // self.squareSize
        endRow = redrawRect.bottom() // self.squareSize
        beginColumn = redrawRect.left() // self.squareSize
        endColumn = redrawRect.right() // self.squareSize

        painter.setPen(Qt.gray)
        for row in range(beginRow, endRow + 1):
            for column in range(beginColumn, endColumn + 1):
                painter.drawRect(column * self.squareSize,
                                 row * self.squareSize, self.squareSize,
                                 self.squareSize)

        fontMetrics = QFontMetrics(self.displayFont)
        painter.setPen(Qt.black)
        for row in range(beginRow, endRow + 1):
            for column in range(beginColumn, endColumn + 1):
                key = row * self.columns + column
                painter.setClipRect(column * self.squareSize,
                                    row * self.squareSize, self.squareSize,
                                    self.squareSize)

                if key == self.lastKey:
                    painter.fillRect(column * self.squareSize + 1,
                                     row * self.squareSize + 1, self.squareSize,
                                     self.squareSize, Qt.red)

                key_ch = self._chr(key)
                painter.drawText(column * self.squareSize + (self.squareSize // 2) - fontMetrics.width(key_ch) // 2,
                                 row * self.squareSize + 4 + fontMetrics.ascent(),
                                 key_ch)

    @staticmethod
    def _chr(codepoint):
        try:
            # Python v2.
            return unichr(codepoint)
        except NameError:
            # Python v3.
            return chr(codepoint)


class Window(QWidget):
    def __init__(self, parent: QWidget = None):
        super(Window, self).__init__(parent)
        self.setupUi()
        self.setWindowTitle("Character Map")

    def setupUi(self):
        filterLabel = QLabel("Filter:")
        self.filterCombo = QComboBox()
        self.filterCombo.addItem("All", QFontComboBox.AllFonts)
        self.filterCombo.addItem("Scalable", QFontComboBox.ScalableFonts)
        self.filterCombo.addItem("Monospaced", QFontComboBox.MonospacedFonts)
        self.filterCombo.addItem("Proportional", QFontComboBox.ProportionalFonts)
        self.filterCombo.setCurrentIndex(0)
        self.filterCombo.currentIndexChanged.connect(self.filterChanged)

        fontLabel = QLabel("Font:")
        self.fontCombo = QFontComboBox()
        sizeLabel = QLabel("Size:")
        self.sizeCombo = QComboBox()
        styleLabel = QLabel("Style:")
        self.styleCombo = QComboBox()
        fontMergeLabel = QLabel("Automatic font merging:")
        self.fontMergeCheckbox = QCheckBox()
        self.fontMergeCheckbox.setChecked(True)
        self.closeBtn = QPushButton("Close")
        self.closeBtn.clicked.connect(qApp.exit)

        self.scrollArea = QScrollArea()
        self.characterWidget = CharacterWidget()
        self.scrollArea.setWidget(self.characterWidget)

        self.findStyles(self.fontCombo.currentFont())
        self.findSizes(self.fontCombo.currentFont())

        self.lineEdit = QLineEdit()
        clipboardButton = QPushButton("&To clipboard")

        self.clipboard = QApplication.clipboard()

        self.fontCombo.currentFontChanged.connect(self.findStyles)
        self.fontCombo.currentFontChanged.connect(self.findSizes)
        self.styleCombo.activated[str].connect(self.characterWidget.updateStyle)
        self.sizeCombo.currentIndexChanged[str].connect(self.characterWidget.updateSize)
        self.characterWidget.characterSelected.connect(self.insertCharacter)

        filterLayout = QHBoxLayout()
        filterLayout.addWidget(filterLabel)
        filterLayout.addWidget(self.filterCombo, 1)
        filterLayout.addWidget(fontLabel)
        filterLayout.addWidget(self.fontCombo, 1)
        filterLayout.addWidget(sizeLabel)
        filterLayout.addWidget(self.sizeCombo, 1)
        filterLayout.addWidget(styleLabel)
        filterLayout.addWidget(self.styleCombo, 1)
        filterLayout.addWidget(fontMergeLabel)
        filterLayout.addWidget(self.fontMergeCheckbox, 1)
        filterLayout.addWidget(self.closeBtn,1)
        filterLayout.addStretch(1)

        lineLayout = QHBoxLayout()
        lineLayout.addWidget(self.lineEdit, 1)
        lineLayout.addSpacing(12)
        lineLayout.addWidget(clipboardButton)

        centralLayout = QVBoxLayout()
        centralLayout.addLayout(filterLayout)
        centralLayout.addWidget(self.scrollArea, 1)
        centralLayout.addSpacing(4)
        centralLayout.addLayout(lineLayout)
        self.setLayout(centralLayout)

    def filterChanged(self, index):
        filter: QFontComboBox.FontFilter = \
            QFontComboBox.FontFilter(self.filterCombo.itemData(index))
        self.fontCombo.setFontFilters(filter)

    def findStyles(self, font: QFont):
        fontDatabase = QFontDatabase()
        currentItem = self.styleCombo.currentText()
        self.styleCombo.clear()

        # get list of styles based on selection
        styles = fontDatabase.styles(font.family())
        for style in styles:
            self.styleCombo.addItem(style)

        styleIndex = self.styleCombo.findText(currentItem)
        if styleIndex == -1:
            self.styleCombo.setCurrentIndex(0)
        else:
            self.styleCombo.setCurrentIndex(styleIndex)

    def findSizes(self, font: QFont):
        fontDatabase = QFontDatabase()
        currentSize = self.sizeCombo.currentText()

        blocker = QSignalBlocker(self.sizeCombo)
        self.sizeCombo.clear()

        if fontDatabase.isSmoothlyScalable(font.family(), fontDatabase.styleString(font)):
            sizes = QFontDatabase.standardSizes()
            for size in sizes:
                self.sizeCombo.addItem(str(size))
                self.sizeCombo.setEditable(True)
        else:
            sizes = fontDatabase.smoothSizes(font.family(), fontDatabase.styleString(font))
            for size in sizes:
                self.sizeCombo.addItem(str(size))
                self.sizeCombo.setEditable(True)

        sizeIndex = self.sizeCombo.findText(currentSize)
        if (sizeIndex == -1):
            self.sizeCombo.setCurrentIndex(max(0, self.sizeCombo.count() // 3))
        else:
            self.sizeCombo.setCurrentIndex(sizeIndex)

    def insertCharacter(self, character):
        self.lineEdit.insert(character)

    def updateClipboard(self):
        self.clipboard.setText(self.lineEdit.text(), QClipboard.Clipboard)
        self.clipboard.setText(self.lineEdit.text(), QClipboard.Selection)


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = PyQtApp(sys.argv)

    win = Window()
    win.setStyleSheet(app.getStylesheet("chocolaf"))
    win.move(100, 100)
    win.show()

    rect = win.geometry()
    win1 = Window()
    win1.setStyleSheet(app.getStylesheet("qdarkstyle_dark"))
    win1.move(rect.left() + rect.width() // 4 + 20, rect.top() + rect.height() + 50)
    win1.show()

    return app.exec()


if __name__ == "__main__":
    main()
