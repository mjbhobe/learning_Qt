"""
// ================================================================================
// step04.py: drawing a squiggle in the main window
//  application handles left mouse press & drag, right mouse press events
//   - draws a squiggle in the client window when left mouse is pressed & dragged
//   - erases the squiggle when the right mouse is pressed
//
// Tutorial - PyQt5 Doodle Application
// Based on a similar tutorial for Borland ObjectWindows Library (OWL) 
// @author: Manish Bhobe
// My experiments with the Qt Framework. Use at your own risk!!
// =================================================================================
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
