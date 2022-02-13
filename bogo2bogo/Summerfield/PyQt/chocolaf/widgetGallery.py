#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
* widgetGallery.py: demonstrates PyQt5 widget gallery
* @author: Manish Bhobe
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""
import os
import pathlib
import sys
import qdarkstyle

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from sklearn.manifold import trustworthiness

sys.path.append(os.path.join(pathlib.Path(__file__).absolute().parents[3], 'common_files'))
from pyqt5_utils import PyQtApp


class WidgetGallery(QWidget):
    def __init__(self, parent: QWidget = None):
        super(WidgetGallery, self).__init__(parent)
        self.buttonsGroupBox = self.createButtonsGroupBox()
        self.simpleWidgetsGroupBox = self.createSimpleWidgetsGroupBox()
        self.toolBox = self.createTextToolBox()

        closeBtn = QPushButton("Close")
        closeBtn.setToolTip("Close the application")
        closeLayout = QHBoxLayout()
        closeLayout.addStretch()
        closeLayout.addWidget(closeBtn)
        closeBtn.clicked.connect(qApp.exit)

        groupsLayout = QGridLayout()
        groupsLayout.addWidget(self.buttonsGroupBox, 0, 0)
        groupsLayout.addWidget(self.simpleWidgetsGroupBox, 0, 1)
        groupsLayout.addWidget(self.toolBox, 1, 1)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(closeLayout)
        mainLayout.addLayout(groupsLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle("Qt Widgets Demo")

    def createButtonsGroupBox(self) -> QGroupBox:
        buttonsGroupBox = QGroupBox("Buttons")
        buttonsGroupBox.setCheckable(True)
        buttonsGroupBox.setChecked(True)

        defPushButton = QPushButton("Default Push Button")
        defPushButton.setDefault(True)
        regPushButton = QPushButton("Regular Push Button")
        disPushButton = QPushButton("Disabled Push Button")
        disPushButton.setEnabled(False)
        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)
        flatPushButton = QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)

        toolButton = QToolButton()
        toolButton.setText("Tool Button")
        chkToolButton = QToolButton()
        chkToolButton.setText("Checkable TB")
        chkToolButton.setCheckable(True)
        menuToolButton = QToolButton()
        menuToolButton.setText("Menu Button")
        toolMenu = QMenu(menuToolButton)
        menuToolButton.setPopupMode(QToolButton.InstantPopup)
        action = QAction("Regular Option", self)
        action.setShortcut(QKeySequence.New)
        toolMenu.addAction(action)
        toolMenu.addSeparator()
        act = toolMenu.addAction("Checkable Option")
        act.setCheckable(True)
        menuToolButton.setMenu(toolMenu)

        toolLayout = QGridLayout()
        toolLayout.addWidget(toolButton, 0, 0)
        toolLayout.addWidget(chkToolButton, 0, 1)
        toolLayout.addWidget(menuToolButton, 1, 0, 1, 2)

        commandLinkButton = QCommandLinkButton("Command Link Button")
        commandLinkButton.setDescription("This is the description")

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(defPushButton)
        buttonLayout.addWidget(regPushButton)
        buttonLayout.addWidget(disPushButton)
        buttonLayout.addWidget(togglePushButton)
        buttonLayout.addWidget(flatPushButton)
        buttonLayout.addLayout(toolLayout)
        buttonLayout.addWidget(commandLinkButton)
        buttonLayout.addStretch(1)

        radioButton1 = QRadioButton("Radio Button 1")
        radioButton2 = QRadioButton("Radio Button 2")
        radioButton3 = QRadioButton("Radio Button 3")
        radioButton4 = QRadioButton("Disabled Radio")
        radioButton1.setChecked(True)
        radioButton4.setEnabled(False)
        checkBox1 = QCheckBox("Normal check box")
        checkBox1.setChecked(True)
        checkBox2 = QCheckBox("Disabled check box")
        checkBox2.setEnabled(False)
        checkBox3 = QCheckBox("Tri-state check box")
        checkBox3.setTristate(True)
        checkBox3.setCheckState(Qt.PartiallyChecked)

        checkableLayout = QVBoxLayout()
        checkableLayout.addWidget(radioButton1)
        checkableLayout.addWidget(radioButton2)
        checkableLayout.addWidget(radioButton3)
        checkableLayout.addWidget(radioButton4)
        checkableLayout.addWidget(checkBox1)
        checkableLayout.addWidget(checkBox2)
        checkableLayout.addWidget(checkBox3)
        checkableLayout.addStretch(1)

        groupLayout = QHBoxLayout()
        groupLayout.addLayout(buttonLayout)
        groupLayout.addLayout(checkableLayout)
        groupLayout.addStretch(1)

        buttonsGroupBox.setLayout(groupLayout)
        return buttonsGroupBox

    def createSimpleWidgetsGroupBox(self):
        simpleWidgetsGroupBox = QGroupBox("Simple Input Widgets")
        simpleWidgetsGroupBox.setCheckable(True)
        simpleWidgetsGroupBox.setChecked(True)

        lineEdit = QLineEdit("Single Line Edit")
        lineEdit.setClearButtonEnabled(True)
        pwdEdit = QLineEdit("s3cRe7")
        pwdEdit.setClearButtonEnabled(True)
        pwdEdit.setEchoMode(QLineEdit.Password)
        spinBox = QSpinBox()
        spinBox.setRange(-200, 200)
        spinBox.setValue(50)
        dateTimeEdit = QDateTimeEdit(simpleWidgetsGroupBox)
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        slider = QSlider()
        slider.setOrientation(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(40)
        scrollBar = QScrollBar()
        scrollBar.setOrientation(Qt.Horizontal)
        scrollBar.setRange(0, 100)
        scrollBar.setValue(60)
        dial = QDial()
        dial.setValue(30)
        dial.setNotchesVisible(True)
        combo = QComboBox()
        items = ['Apple iPhone', 'OnePlus 9T', 'Dell XPS', 'Apple MacBook Pro',
                 'Python', 'Java', 'Spring', 'C/C++', 'Visual Studio Code', 'GNU C/C++',
                 'Vim', 'Tensorflow', 'Keras', 'Pytorch', 'Keras', 'Coffee']
        combo.addItems(items)

        layout = QGridLayout()
        layout.addWidget(lineEdit, 0, 0, 1, 2)
        layout.addWidget(pwdEdit, 1, 0, 1, 2)
        layout.addWidget(spinBox, 2, 0, 1, 2)
        layout.addWidget(dateTimeEdit, 3, 0, 1, 2)
        layout.addWidget(slider, 4, 0)
        layout.addWidget(scrollBar, 5, 0)
        layout.addWidget(dial, 4, 1, 2, 1)
        layout.addWidget(combo, 6, 0, 1, 2)
        layout.setRowStretch(7, 1)
        simpleWidgetsGroupBox.setLayout(layout)

        return simpleWidgetsGroupBox

    def embedIntoHBoxLayout(self, widget: QWidget, margin: int = 5) -> QWidget:
        ret = QWidget()
        layout = QHBoxLayout(ret)
        layout.setContentsMargins(margin, margin, margin, margin)
        layout.addWidget(widget)
        return ret

    def createTextToolBox(self) -> QToolBox:
        textToolBox = QToolBox()

        plainText: str = ("Twinkle, twinkle, little star,\n" +
                          "How I wonder what you are.\n" +
                          "Up above the world so high,\n" +
                          "Like a diamond in the sky.\n" +
                          "Twinkle, twinkle, little star,\n" +
                          "How I wonder what you are!\n")

        richText = "<html><head/><body><i>"
        for line in plainText.split("\n"):
            richText += "<center>" + line + "</center>"
        richText += "</i></body></html>"
        print(richText)

        plainTextEdit = QPlainTextEdit(plainText)
        textEdit = QTextEdit(richText)
        self.systemInfoTextBrowser = QTextBrowser()
        self.updateSystemInfo()

        textToolBox.addItem(self.embedIntoHBoxLayout(plainTextEdit), "Plain Text Edit")
        textToolBox.addItem(self.embedIntoHBoxLayout(textEdit), "Text Edit")
        textToolBox.addItem(self.embedIntoHBoxLayout(self.systemInfoTextBrowser), "Text Browser")
        return textToolBox

    @staticmethod
    def highDpiScaleFactorRoundingPolicy():
        policy = QGuiApplication.highDpiScaleFactorRoundingPolicy()
        if policy[-1] == ')':
            policy = policy[:-1]
        lastSep = policy.rfind("::")
        if lastSep != -1:
            policy = policy[:lastSep + 2]
        return policy

    def updateSystemInfo(self):
        """
        str = (f"<html><head/><body><h3>Build</h3><p> {QLibraryInfo.build()}</p>" +
               f"<h3>Operating System</h3><p> {QSysInfo().prettyProductName()}</p>" +
               f"<h3>Screens</h3><p>High DPI scale factor rounding policy:{WidgetGallery.highDpiScaleFactorRoundingPolicy()}</p><ol>")
        for screen in QGuiApplication.screens():
            current: bool = (screen == self.screen())
            str = "<li>"
            if (current):
                str += "<i>"
            str += f"{screen.name()}\{screen.geometry()}, {screen.logicalDotsPerInchX()} DPI, DPR={screen.devicePixelRatio()}"
            if (current):
                str += "</i>"
            str += "</li>"
        str += "</ol></body></html>"
        self.systemInfoTextBrowser.setHtml(str)
        """
        pass


def loadStyleSheet() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    print(f"loadStyleSteet() -> You are {here}")
    darkss_dir = os.path.join(here, "styles", "dark")
    sys.path.append(darkss_dir)
    import stylesheet_rc

    darkss_path = os.path.join(darkss_dir, "stylesheet.css")
    assert os.path.exists(darkss_path)
    print(f"LoasStyleSheet() -> loading dark stylesheet from {darkss_path}")
    stylesheet = ""
    with open(darkss_path, "r") as f:
        stylesheet = f.read()
    return stylesheet


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = PyQtApp(sys.argv)

    w = WidgetGallery()
    w.setStyleSheet(app.getStylesheet("chocolaf"))
    w.move(20, 20)
    w.show()

    rect = w.geometry()
    w1 = WidgetGallery()
    w1.setStyleSheet(app.getStylesheet("qdarkstyle_dark"))
    w1.move(rect.left() + rect.width() + 50,
            rect.top() + rect.height() // 4 + 50)
    w1.show()

    return app.exec()


if __name__ == "__main__":
    main()
