#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
* pyqt5_utils.py - utility functions for PyQt5 GUI programmings
* @author: Manish Bhobe
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""

import sys
import os

# to detect dark themes (@see: https://pypi.org/project/darkdetect/)
import darkdetect
# using qdarkstyle (@see: https://github.com/ColinDuquesnoy/QDarkStyleSheet)
# import qdarkstyle
# from qdarkstyle.dark.palette import DarkPalette
# from qdarkstyle.light.palette import LightPalette
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

__version__ = "1.0"
__author__ = "Manish Bhobe"


class ThemeSetter(QObject):
    @staticmethod
    def _getDarkPalette() -> QPalette:
        """ static function - returns a dark palette similar to Windows """
        darkPalette = QPalette()
        darkPalette.setColor(QPalette.Window, QColor(36, 36, 36))  # QColor(53, 53, 53))
        darkPalette.setColor(QPalette.WindowText, Qt.white)
        darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
        darkPalette.setColor(QPalette.Base, QColor(46, 46, 46))  # QColor(42, 42, 42))
        darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
        darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
        darkPalette.setColor(QPalette.ToolTipText, QColor(53, 53, 53))
        darkPalette.setColor(QPalette.Text, Qt.white)
        darkPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
        darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
        darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
        darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
        darkPalette.setColor(QPalette.ButtonText, Qt.white)
        darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
        darkPalette.setColor(QPalette.BrightText, Qt.red)
        darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        darkPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))
        darkPalette.setColor(QPalette.HighlightedText, Qt.white)
        darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))
        return darkPalette

    @staticmethod
    def _getLightPalette() -> QPalette:
        """ static function - returns a light palette similar to Windows """
        lightPalette = QPalette()
        lightPalette.setColor(QPalette.Window, Qt.white)  # QColor(240, 240, 240))
        lightPalette.setColor(QPalette.WindowText, Qt.black)
        lightPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(240, 240, 240))
        lightPalette.setColor(QPalette.Base, QColor(235, 235, 235))  # Qt.white)
        lightPalette.setColor(QPalette.AlternateBase, QColor(245, 245, 245))
        lightPalette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
        lightPalette.setColor(QPalette.ToolTipText, Qt.black)
        lightPalette.setColor(QPalette.Text, Qt.black)
        lightPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(120, 120, 120))
        lightPalette.setColor(QPalette.Dark, QColor(160, 160, 160))
        lightPalette.setColor(QPalette.Shadow, QColor(105, 105, 105))
        lightPalette.setColor(QPalette.Button, QColor(240, 240, 240))
        lightPalette.setColor(QPalette.ButtonText, Qt.black)
        lightPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(78, 78, 78))
        lightPalette.setColor(QPalette.BrightText, Qt.white)
        lightPalette.setColor(QPalette.Link, QColor(0, 0, 255))
        lightPalette.setColor(QPalette.Highlight, QColor(0, 120, 215))
        lightPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(0, 120, 215))
        lightPalette.setColor(QPalette.HighlightedText, Qt.white)
        lightPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, Qt.white)
        return lightPalette

    @staticmethod
    def setDarkTheme(app: QApplication) -> None:
        """ sets dark palette """
        app.setPalette(ThemeSetter._getDarkPalette())

    @staticmethod
    def setLightTheme(app: QApplication) -> None:
        """ sets light palette """
        app.setPalette(ThemeSetter._getLightPalette())


class PaletteSwitcher(QObject):
    def __init__(self, appInstance: QApplication, parent: QObject = None):
        super(PaletteSwitcher, self).__init__(parent)
        self.appInstance = appInstance
        self.darkPalette = None
        self.lightPalette = None
        self.darkPaletteInUse = False
        self.__initializePalettes()

    def __initializePalettes(self):
        """ initialize colors for light & dark palettes on Windows - does NOTHING on other platforms """
        self.darkPalette = QPalette()
        self.darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.darkPalette.setColor(QPalette.WindowText, Qt.white)
        self.darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
        self.darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
        self.darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
        self.darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
        self.darkPalette.setColor(QPalette.ToolTipText, QColor(53, 53, 53))
        self.darkPalette.setColor(QPalette.Text, Qt.white)
        self.darkPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
        self.darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
        self.darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
        self.darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.darkPalette.setColor(QPalette.ButtonText, Qt.white)
        self.darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
        self.darkPalette.setColor(QPalette.BrightText, Qt.red)
        self.darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
        self.darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        self.darkPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))
        self.darkPalette.setColor(QPalette.HighlightedText, Qt.white)
        self.darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))

        self.lightPalette = QPalette()
        self.lightPalette.setColor(QPalette.Window, QColor(240, 240, 240))
        self.lightPalette.setColor(QPalette.WindowText, Qt.black)
        self.lightPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(240, 240, 240))
        self.lightPalette.setColor(QPalette.Base, Qt.white)
        self.lightPalette.setColor(QPalette.AlternateBase, QColor(233, 231, 227))
        self.lightPalette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
        self.lightPalette.setColor(QPalette.ToolTipText, Qt.black)
        self.lightPalette.setColor(QPalette.Text, Qt.black)
        self.lightPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(120, 120, 120))
        self.lightPalette.setColor(QPalette.Dark, QColor(160, 160, 160))
        self.lightPalette.setColor(QPalette.Shadow, QColor(105, 105, 105))
        self.lightPalette.setColor(QPalette.Button, QColor(240, 240, 240))
        self.lightPalette.setColor(QPalette.ButtonText, Qt.black)
        self.lightPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(78, 78, 78))
        self.lightPalette.setColor(QPalette.BrightText, Qt.white)
        self.lightPalette.setColor(QPalette.Link, QColor(0, 0, 255))
        self.lightPalette.setColor(QPalette.Highlight, QColor(0, 120, 215))
        self.lightPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(0, 120, 215))
        self.lightPalette.setColor(QPalette.HighlightedText, Qt.white)
        self.lightPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, Qt.white)

    def setDarkPalette(self) -> None:
        """ sets dark palette """
        self.appInstance.setPalette(self.darkPalette)
        self.darkPaletteInUse = True

    def setLightPalette(self) -> None:
        """ sets light palette """
        self.appInstance.setPalette(self.lightPalette)
        self.darkPaletteInUse = False

    def isDarkPaletteInUse(self) -> bool:
        """ checks if dark or light palette is in use """
        return (self.darkPaletteInUse == True)

    def swapPalettes(self) -> None:
        """ swaps palettes - light to dark or vice-versa """
        if self.darkPaletteInUse:
            self.appInstance.setPalette(self.lightPalette)
        else:
            self.appInstance.setPalette(self.darkPalette)
        self.darkPaletteInUse = not self.darkPaletteInUse


class PyQtApp(QApplication):
    def __init__(self, *args, **kwargs):
        super(PyQtApp, self).__init__(*args, **kwargs)
        # self.setStyle("Fusion")
        # map of stylesheets
        self.styles = {}
        self.font: QFont = QFont("Segoe UI", 11) if sys.platform == "win32" \
            else QApplication.font("QMenu")
        self.setFont(self.font)
        self.loadStyleSheets()

    def loadChocoLaf(self) -> str:
        """ loads the chocolaf stylesheet from ./styes/chocolaf """
        here = os.path.dirname(os.path.abspath(__file__))
        chocolaf_dir = os.path.join(here, "styles", "chocolaf")
        sys.path.append(chocolaf_dir)
        import stylesheet_rc

        chocolaf_ss_path = os.path.join(chocolaf_dir, "stylesheet.css")
        assert os.path.exists(chocolaf_ss_path)
        print(f"loadChocoLaf() -> loading stylesheet from {chocolaf_ss_path}")
        stylesheet = ""
        with open(chocolaf_ss_path, "r") as f:
            stylesheet = f.read()
        return stylesheet

    def loadStyleSheets(self):
        # load chocolaf
        chocolaf_ss = self.loadChocoLaf()
        self.styles["Chocolaf"] = chocolaf_ss

        try:
            import qdarkstyle
            from qdarkstyle.dark.palette import DarkPalette
            from qdarkstyle.light.palette import LightPalette

            qdarkstyle_darkss = qdarkstyle.load_stylesheet(palette=DarkPalette)
            qdarkstyle_darkss += "\nQPushButton{min-height:1.2em; min-width:3em}"
            self.styles["QDarkStyle-dark"] = qdarkstyle_darkss

            qdarkstyle_lightss = qdarkstyle.load_stylesheet(palette=LightPalette)
            qdarkstyle_lightss += "\nQPushButton{min-height:1.2em; min-width:3em}"
            self.styles["QDarkStyle-light"] = qdarkstyle_lightss

            # NOTE: following styles do not have supporting custom stylesheets
            # self.styles["fusion"] = ""
            # self.styles["windows"] = ""

        except ImportError:
            pass

    def availableStyles(self, subset='all') -> list:
        assert subset in ['all', 'mine']
        availableStyles = []
        for key in self.styles.keys():
            availableStyles.append(key)
        if subset == 'all':
            for key in QStyleFactory.keys():
                availableStyles.append(key)
        return availableStyles

    def getStyleSheet(self, style: str):
        if style in self.availableStyles('mine'):
            return self.styles[style]
        else:
            availableStyles = self.availableStyles('mine')
            msg = f"\"{style}\" is not recognized as a valid stylesheet!\nValid options are: {availableStyles}"
            raise ValueError(msg)

    def setStyle(self, style: str) -> None:
        """ NOTE: style is case sensitive! """
        if style in self.styles.keys():
            stylesheet = self.styles[style]
            # return self.styles[style]
            self.setStyleSheet(stylesheet)
        elif style in QStyleFactory.keys():
            super(PyQtApp, self).setStyle(style)
        else:
            availableStyles = self.availableStyles('all')
            msg = f"\"{style}\" is not recognized as a valid style!\nValid options are: [{availableStyles}]"
            raise ValueError(msg)


# class PyQtApp2(QApplication):
#     def __init__(self, *args, **kwargs):
#         super(PyQtApp, self).__init__(*args, **kwargs)
#         # self.setStyle("Fusion")
#         self.font: QFont = QFont("Segoe UI", 11) if sys.platform == "win32" \
#             else QApplication.font("QMenu")
#         self.setFont(self.font)
#         # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
#         # QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

#         # load the stylesheets
#         self.darkStyle = qdarkstyle.load_stylesheet(palette=DarkPalette)
#         self.darkStyle += "\nQPushButton{min-height:1.2em; min-width:3em}"
#         self.lightStyle = qdarkstyle.load_stylesheet(palette=LightPalette)
#         self.lightStyle += "\nQPushButton{min-height:1.2em; min-width:3em}"
#         # set style depending on which theme is in Use
#         if darkdetect.isDark():
#             self.setStyleSheet(self.darkStyle)
#             self.darkMode = True
#         else:
#             self.setStyleSheet(self.lightStyle)
#             self.darkMode = False

#     def getFont(self) -> QFont:
#         return self.font

#     def setDarkStyle(self):
#         self.setStyleSheet(self.darkStyle)
#         self.darkMode = True

#     def setLightStyle(self):
#         self.setStyleSheet(self.lightStyle)
#         self.darkMode = False

#     def swapStyle(self):
#         ss = self.lightStyle if self.darkMode else self.darkStyle
#         self.setStyleSheet(ss)


# def getPaletteColor(colorRole: QPalette.ColorRole,
#                     colorGroup: QPalette.ColorGroup = QPalette.Active) -> QColor:
#     pal = qApp.palette()
#     color = pal.color(colorGroup, colorRole)
#     return color


# def _getWinDarkPalette() -> QPalette:
#     darkPalette = QPalette()
#     darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
#     darkPalette.setColor(QPalette.WindowText, Qt.white)
#     darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
#     darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
#     darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
#     darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
#     darkPalette.setColor(QPalette.ToolTipText, QColor(53, 53, 53))
#     darkPalette.setColor(QPalette.Text, Qt.white)
#     darkPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
#     darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
#     darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
#     darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
#     darkPalette.setColor(QPalette.ButtonText, Qt.white)
#     darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
#     darkPalette.setColor(QPalette.BrightText, Qt.red)
#     darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
#     darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
#     darkPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))
#     darkPalette.setColor(QPalette.HighlightedText, Qt.white)
#     darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))
#     return darkPalette


# def _getWinLightPalette() -> QPalette:
#     lightPalette = QPalette()
#     lightPalette.setColor(QPalette.Window, QColor(240, 240, 240))
#     lightPalette.setColor(QPalette.WindowText, Qt.black)
#     lightPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(240, 240, 240))
#     lightPalette.setColor(QPalette.Base, Qt.white)
#     lightPalette.setColor(QPalette.AlternateBase, QColor(233, 231, 227))
#     lightPalette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
#     lightPalette.setColor(QPalette.ToolTipText, Qt.black)
#     lightPalette.setColor(QPalette.Text, Qt.black)
#     lightPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(120, 120, 120))
#     lightPalette.setColor(QPalette.Dark, QColor(160, 160, 160))
#     lightPalette.setColor(QPalette.Shadow, QColor(105, 105, 105))
#     lightPalette.setColor(QPalette.Button, QColor(240, 240, 240))
#     lightPalette.setColor(QPalette.ButtonText, Qt.black)
#     lightPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(78, 78, 78))
#     lightPalette.setColor(QPalette.BrightText, Qt.white)
#     lightPalette.setColor(QPalette.Link, QColor(0, 0, 255))
#     lightPalette.setColor(QPalette.Highlight, QColor(0, 120, 215))
#     lightPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(0, 120, 215))
#     lightPalette.setColor(QPalette.HighlightedText, Qt.white)
#     lightPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, Qt.white)
#     return lightPalette


# def setDarkPalette(app: QApplication) -> None:
#     app.setPalette(_getWinDarkPalette())


# def setLightPalette(app: QApplication) -> None:
#     app.setPalette(_getWinLightPalette())


# class PalMainWindow(QMainWindow):
#     def __init__(self, palSwitcher: PaletteSwitcher):
#         super(PalMainWindow, self).__init__()
#         self.palSwitcher = palSwitcher
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.switchPalette)
#         self.timer.start(1000)

#     def switchPalette(self):
#         if (darkdetect.isDark() and (not self.palSwitcher.isDarkPaletteInUse()))
#                 or ((not darkdetect.isDark()) and self.palSwitcher.isDarkPaletteInUse()):
#             self.palSwitcher.swapPalettes()


# class PalWidget(QWidget):
#     def __init__(self, palSwitcher: PaletteSwitcher):
#         super(PalWidget, self).__init__()
#         self.palSwitcher=palSwitcher
#         self.timer=QTimer()
#         self.timer.timeout.connect(self.switchPalette)
#         self.timer.start(1000)

#     def switchPalette(self):
#         if (darkdetect.isDark() and (not self.palSwitcher.isDarkPaletteInUse()))
#                 or ((not darkdetect.isDark()) and self.palSwitcher.isDarkPaletteInUse()):
#             self.palSwitcher.swapPalettes()
