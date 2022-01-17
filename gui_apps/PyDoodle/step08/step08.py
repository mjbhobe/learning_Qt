# -*- coding: utf-8 -*-
"""
// ===================================================================================
// step08.py: drawing multiple squiggles in window, each with own attribute
//  application handles left mouse press & drag, right mouse press events
//   - draws a squiggle in the client window when left mouse is pressed & dragged
//   - if ctrl + left mouse press - display dialog to set new pen thickness
//   - if ctrl + right mouse press - display dialog to set new pen thickness
//     (NOTE: Ctrl + mouse clicks is perhaps not the best way to design a GUI.
//      We are using this method as we have not yet introduces menus & toolbars.
//      This flaw will be corrected in steps where these GUI elements are introduced)
//
// Tutorial - PyQt5 Doodle Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// @author: Manish Bhobe
// My experiments with the Qt Framework. Use at your own risk!!
// =====================================================================================
"""
import sys, os
import pathlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainWindow import MainWindow

sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common'))
from mypyqt5_utils import PyQtApp


def main():
    app = PyQtApp(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
