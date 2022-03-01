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
        # self.font: QFont = QFont("Segoe UI", 11) if sys.platform == "win32" \
        #     else QApplication.font("QMenu")
        self.setFont(QApplication.font("QMenu"))
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
        elif style in QStyleFactory.keys():
            super(PyQtApp, self).setStyle(style)
        else:
            availableStyles = self.availableStyles('all')
            msg = f"\"{style}\" is not recognized as a valid style!\nValid options are: [{availableStyles}]"
            raise ValueError(msg)
