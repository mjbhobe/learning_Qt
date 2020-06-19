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
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainWindow import *

def main():
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
