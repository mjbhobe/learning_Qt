"""
* windowFlags.py: PyQt version of windowsFlags Qt widgets application using Chocolaf Theme
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


class PreviewWindow(QWidget):
    def __init__(self, parent=None):
        super(PreviewWindow, self).__init__(parent)

        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

        closeButton = QPushButton("&Close")
        closeButton.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(closeButton)
        self.setLayout(layout)

        self.setWindowTitle("Preview")

    def setWindowFlags(self, flags):
        super(PreviewWindow, self).setWindowFlags(flags)

        flag_type = (flags & Qt.WindowType_Mask)

        if flag_type == Qt.Window:
            text = "Qt.Window"
        elif flag_type == Qt.Dialog:
            text = "Qt.Dialog"
        elif flag_type == Qt.Sheet:
            text = "Qt.Sheet"
        elif flag_type == Qt.Drawer:
            text = "Qt.Drawer"
        elif flag_type == Qt.Popup:
            text = "Qt.Popup"
        elif flag_type == Qt.Tool:
            text = "Qt.Tool"
        elif flag_type == Qt.ToolTip:
            text = "Qt.ToolTip"
        elif flag_type == Qt.SplashScreen:
            text = "Qt.SplashScreen"
        else:
            text = ""

        if flags & Qt.MSWindowsFixedSizeDialogHint:
            text += "\n| Qt.MSWindowsFixedSizeDialogHint"
        if flags & Qt.X11BypassWindowManagerHint:
            text += "\n| Qt.X11BypassWindowManagerHint"
        if flags & Qt.FramelessWindowHint:
            text += "\n| Qt.FramelessWindowHint"
        if flags & Qt.WindowTitleHint:
            text += "\n| Qt.WindowTitleHint"
        if flags & Qt.WindowSystemMenuHint:
            text += "\n| Qt.WindowSystemMenuHint"
        if flags & Qt.WindowMinimizeButtonHint:
            text += "\n| Qt.WindowMinimizeButtonHint"
        if flags & Qt.WindowMaximizeButtonHint:
            text += "\n| Qt.WindowMaximizeButtonHint"
        if flags & Qt.WindowCloseButtonHint:
            text += "\n| Qt.WindowCloseButtonHint"
        if flags & Qt.WindowContextHelpButtonHint:
            text += "\n| Qt.WindowContextHelpButtonHint"
        if flags & Qt.WindowShadeButtonHint:
            text += "\n| Qt.WindowShadeButtonHint"
        if flags & Qt.WindowStaysOnTopHint:
            text += "\n| Qt.WindowStaysOnTopHint"
        if flags & Qt.WindowStaysOnBottomHint:
            text += "\n| Qt.WindowStaysOnBottomHint"
        if flags & Qt.CustomizeWindowHint:
            text += "\n| Qt.CustomizeWindowHint"

        self.textEdit.setPlainText(text)


class ControllerWindow(QWidget):
    def __init__(self):
        super(ControllerWindow, self).__init__()

        self.previewWindow = PreviewWindow(self)

        self.createTypeGroupBox()
        self.createHintsGroupBox()

        quitButton = QPushButton("&Quit")
        quitButton.clicked.connect(self.close)

        bottomLayout = QHBoxLayout()
        bottomLayout.addStretch()
        bottomLayout.addWidget(quitButton)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.typeGroupBox)
        mainLayout.addWidget(self.hintsGroupBox)
        mainLayout.addLayout(bottomLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle("Window Flags")
        self.updatePreview()

    def updatePreview(self):
        flags = Qt.WindowFlags()

        if self.windowRadioButton.isChecked():
            flags = Qt.Window
        elif self.dialogRadioButton.isChecked():
            flags = Qt.Dialog
        elif self.sheetRadioButton.isChecked():
            flags = Qt.Sheet
        elif self.drawerRadioButton.isChecked():
            flags = Qt.Drawer
        elif self.popupRadioButton.isChecked():
            flags = Qt.Popup
        elif self.toolRadioButton.isChecked():
            flags = Qt.Tool
        elif self.toolTipRadioButton.isChecked():
            flags = Qt.ToolTip
        elif self.splashScreenRadioButton.isChecked():
            flags = Qt.SplashScreen

        if self.msWindowsFixedSizeDialogCheckBox.isChecked():
            flags |= Qt.MSWindowsFixedSizeDialogHint
        if self.x11BypassWindowManagerCheckBox.isChecked():
            flags |= Qt.X11BypassWindowManagerHint
        if self.framelessWindowCheckBox.isChecked():
            flags |= Qt.FramelessWindowHint
        if self.windowTitleCheckBox.isChecked():
            flags |= Qt.WindowTitleHint
        if self.windowSystemMenuCheckBox.isChecked():
            flags |= Qt.WindowSystemMenuHint
        if self.windowMinimizeButtonCheckBox.isChecked():
            flags |= Qt.WindowMinimizeButtonHint
        if self.windowMaximizeButtonCheckBox.isChecked():
            flags |= Qt.WindowMaximizeButtonHint
        if self.windowCloseButtonCheckBox.isChecked():
            flags |= Qt.WindowCloseButtonHint
        if self.windowContextHelpButtonCheckBox.isChecked():
            flags |= Qt.WindowContextHelpButtonHint
        if self.windowShadeButtonCheckBox.isChecked():
            flags |= Qt.WindowShadeButtonHint
        if self.windowStaysOnTopCheckBox.isChecked():
            flags |= Qt.WindowStaysOnTopHint
        if self.windowStaysOnBottomCheckBox.isChecked():
            flags |= Qt.WindowStaysOnBottomHint
        if self.customizeWindowHintCheckBox.isChecked():
            flags |= Qt.CustomizeWindowHint

        self.previewWindow.setWindowFlags(flags)

        pos = self.previewWindow.pos()

        if pos.x() < 0:
            pos.setX(0)

        if pos.y() < 0:
            pos.setY(0)

        self.previewWindow.move(pos)
        self.previewWindow.show()

    def createTypeGroupBox(self):
        self.typeGroupBox = QGroupBox("Type")

        self.windowRadioButton = self.createRadioButton("Window")
        self.dialogRadioButton = self.createRadioButton("Dialog")
        self.sheetRadioButton = self.createRadioButton("Sheet")
        self.drawerRadioButton = self.createRadioButton("Drawer")
        self.popupRadioButton = self.createRadioButton("Popup")
        self.toolRadioButton = self.createRadioButton("Tool")
        self.toolTipRadioButton = self.createRadioButton("Tooltip")
        self.splashScreenRadioButton = self.createRadioButton("Splash screen")
        self.windowRadioButton.setChecked(True)

        layout = QGridLayout()
        layout.addWidget(self.windowRadioButton, 0, 0)
        layout.addWidget(self.dialogRadioButton, 1, 0)
        layout.addWidget(self.sheetRadioButton, 2, 0)
        layout.addWidget(self.drawerRadioButton, 3, 0)
        layout.addWidget(self.popupRadioButton, 0, 1)
        layout.addWidget(self.toolRadioButton, 1, 1)
        layout.addWidget(self.toolTipRadioButton, 2, 1)
        layout.addWidget(self.splashScreenRadioButton, 3, 1)
        self.typeGroupBox.setLayout(layout)

    def createHintsGroupBox(self):
        self.hintsGroupBox = QGroupBox("Hints")

        self.msWindowsFixedSizeDialogCheckBox = self.createCheckBox("MS Windows fixed size dialog")
        self.x11BypassWindowManagerCheckBox = self.createCheckBox("X11 bypass window manager")
        self.framelessWindowCheckBox = self.createCheckBox("Frameless window")
        self.windowTitleCheckBox = self.createCheckBox("Window title")
        self.windowSystemMenuCheckBox = self.createCheckBox("Window system menu")
        self.windowMinimizeButtonCheckBox = self.createCheckBox("Window minimize button")
        self.windowMaximizeButtonCheckBox = self.createCheckBox("Window maximize button")
        self.windowCloseButtonCheckBox = self.createCheckBox("Window close button")
        self.windowContextHelpButtonCheckBox = self.createCheckBox("Window context help button")
        self.windowShadeButtonCheckBox = self.createCheckBox("Window shade button")
        self.windowStaysOnTopCheckBox = self.createCheckBox("Window stays on top")
        self.windowStaysOnBottomCheckBox = self.createCheckBox("Window stays on bottom")
        self.customizeWindowHintCheckBox = self.createCheckBox("Customize window")

        layout = QGridLayout()
        layout.addWidget(self.msWindowsFixedSizeDialogCheckBox, 0, 0)
        layout.addWidget(self.x11BypassWindowManagerCheckBox, 1, 0)
        layout.addWidget(self.framelessWindowCheckBox, 2, 0)
        layout.addWidget(self.windowTitleCheckBox, 3, 0)
        layout.addWidget(self.windowSystemMenuCheckBox, 4, 0)
        layout.addWidget(self.windowMinimizeButtonCheckBox, 0, 1)
        layout.addWidget(self.windowMaximizeButtonCheckBox, 1, 1)
        layout.addWidget(self.windowCloseButtonCheckBox, 2, 1)
        layout.addWidget(self.windowContextHelpButtonCheckBox, 3, 1)
        layout.addWidget(self.windowShadeButtonCheckBox, 4, 1)
        layout.addWidget(self.windowStaysOnTopCheckBox, 5, 1)
        layout.addWidget(self.windowStaysOnBottomCheckBox, 6, 1)
        layout.addWidget(self.customizeWindowHintCheckBox, 5, 0)
        self.hintsGroupBox.setLayout(layout)

    def createCheckBox(self, text):
        checkBox = QCheckBox(text)
        checkBox.clicked.connect(self.updatePreview)
        return checkBox

    def createRadioButton(self, text):
        button = QRadioButton(text)
        button.clicked.connect(self.updatePreview)
        return button


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = PyQtApp(sys.argv)
    app.setStyle("Chocolaf")

    win = ControllerWindow()
    win.move(100, 100)
    win.show()

    return app.exec()


if __name__ == "__main__":
    main()
