"""
// ============================================================================
// step01.py: creating the basic Doodle PyQt application
//
// Tutorial - PyQt5 Doodle Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// @author: Manish Bhobe
// My experiments with the Qt Framework. Use at your own risk!!
// ============================================================================
"""
import sys
from PyQt5.QtGui import *
from mainWindow import *

from chocolaf.palettes import ChocolafPalette
from chocolaf.utils.pyqtapp import PyQtApp


def main():
    app = PyQtApp(sys.argv)
    app.setStyle("Chocolaf")

    mainWindow = MainWindow()
    mainWindow.show()

    return app.exec()


if __name__ == "__main__":
    main()
