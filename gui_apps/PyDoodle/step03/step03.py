"""
// ============================================================================
// step03.py: drawing in the main window
//     application handles the left & right mouse click Events & close event
//       - left mouse click: displays the client co-ordinates where clicked
//       - right mouse click: clears the drawing canvas
//
// Tutorial - PyQt5 Doodle Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// @author: Manish Bhobe
// My experiments with the Qt Framework. Use at your own risk!!
// ============================================================================
"""
import sys
import os
import pathlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainWindow import *
import darkdetect

sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common'))
from mypyqt5_utils import PaletteSwitcher, PyQtApp


def main():
    app = PyQtApp(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
