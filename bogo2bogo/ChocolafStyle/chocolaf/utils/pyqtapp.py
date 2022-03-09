#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
* pyqt5_utils.py - utility functions for PyQt5 GUI programming
* @author: Manish Bhobe
* My experiments with Python, PyQt, Data Science & Deep Learning
* The code is made available for illustration purposes only.
* Use at your own risk!!
"""

import sys
import os
import chocolaf

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

__version__ = "1.0"
__author__ = "Manish Bhobe"


class PyQtApp(QApplication):
    def __init__(self, *args, **kwargs):
        super(PyQtApp, self).__init__(*args, **kwargs)
        # self.setStyle("Fusion")
        # map of stylesheets
        self.styles = {}
        self.palettes = {}
        # self.font: QFont = QFont("Segoe UI", 11) if sys.platform == "win32" \
        #     else QApplication.font("QMenu")

        self.setFont(QApplication.font("QMenu"))
        self.loadStyleSheets()

    # def loadChocoLaf(self) -> str:
    #     """ loads the chocolaf stylesheet from ./styes/chocolaf """
    #     here = os.path.dirname(os.path.abspath(__file__))
    #     chocolaf_dir = os.path.join(here, "styles", "chocolaf")
    #     sys.path.append(chocolaf_dir)
    #     import stylesheet_rc

    #     chocolaf_ss_path = os.path.join(chocolaf_dir, "stylesheet.css")
    #     assert os.path.exists(chocolaf_ss_path)
    #     print(f"loadChocoLaf() -> loading stylesheet from {chocolaf_ss_path}")
    #     stylesheet = ""
    #     with open(chocolaf_ss_path, "r") as f:
    #         stylesheet = f.read()
    #     return stylesheet

    def getPalette(self) -> QPalette:
        palette = QPalette()
        # @see: https://doc.qt.io/qt-5/qpalette.html
        palette.setColor(QPalette.Window, QColor(qRgb(42, 42, 42)))         # general background color
        palette.setColor(QPalette.WindowText, QColor(qRgb(220, 220, 220)))  # general foreground color
        palette.setColor(QPalette.Base, QColor(qRgb(52, 52, 52)))           # background for text entry widgets
        # background color for views with alternating colors
        palette.setColor(QPalette.AlternateBase, QColor(qRgb(62, 62, 62)))
        palette.setColor(QPalette.ToolTipBase, QColor(qRgb(224, 227, 176)))  # background for tooltips
        palette.setColor(QPalette.ToolTipText, QColor(qRgb(0, 0, 0)))
        palette.setColor(QPalette.Text, QColor(qRgb(220, 220, 220)))        # foreground color to use with Base
        palette.setColor(QPalette.Button, QColor(qRgb(62, 62, 62)))         # pushbutton colors
        palette.setColor(QPalette.ButtonText, QColor(qRgb(220, 220, 220)))  # pushbutton's text color
        palette.setColor(QPalette.Link, Qt.blue)
        palette.setColor(QPalette.LinkVisited, Qt.magenta)
        palette.setColor(QPalette.Highlight, QColor(qRgb(0, 114, 198)))     # highlight color
        palette.setColor(QPalette.HighlightedText, QColor(qRgb(220, 220, 220)))

        palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(qRgb(127, 127, 127)))
        palette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(qRgb(127, 127, 127)))
        palette.setColor(QPalette.Disabled, QPalette.Text, QColor(qRgb(127, 127, 127)))
        palette.setColor(QPalette.Disabled, QPalette.Light, QColor(qRgb(102, 102, 102)))

        return palette

    def loadStyleSheets(self):
        # load chocolaf
        chocolaf_ss = chocolaf.loadStyleSheet()  # self.loadChocoLaf()
        self.styles["Chocolaf"] = chocolaf_ss
        # self.palettes["Chocolaf"] = self.getPalette()

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
            # if user has not install QDarkStyle, these stylesheets will not be available!
            pass

    def availableStyles(self, subset='all') -> list:
        assert subset in ['all', 'mine']
        availableStyles = []
        for key in self.styles.keys():
            availableStyles.append(key)
        if subset == 'all':
            # add styles included with PyQt
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
            if style == "Chocolaf":
                self.setPalette(self.getPalette())
        elif style in QStyleFactory.keys():
            super(PyQtApp, self).setStyle(style)
        else:
            availableStyles = self.availableStyles('all')
            msg = f"\"{style}\" is not recognized as a valid style!\nValid options are: [{availableStyles}]"
            raise ValueError(msg)
