"""
// ============================================================================
// step04.py: drawing in the main window
//     application handles the left & right mouse click Events & close event
//         - traces a line in the client window
//
// Tutorial - Qt Scribble Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL)
// Created by Manish Bhobe.
// My experiments with the Qt Framework. Use at your own risk!!
// ============================================================================
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from drawWindow import *

def main():
    app = QApplication(sys.argv)

    mainWindow = DrawWindow()
    mainWindow.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
