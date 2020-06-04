"""
// ============================================================================
// step05.py: drawing multiple lines in window, each with own attribute
//     application handles the left & right mouse click Events & close event
//         - traces a lines in the client window
//     left mouse double click - set pen width
//     right mouse double click - set pen color
//     (double clicks are a horrible way of designing a GUI - for now, please
//      bear with me. This flaw will be corrected in future steps)
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
