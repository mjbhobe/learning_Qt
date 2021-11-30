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
import os
import pathlib
from PyQt5.QtGui import *
from mainWindow import *
import darkdetect

sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common'))
import mypyqt5_utils as utils


def main():
    app = QApplication(sys.argv)
    app.setFont(QApplication.font("QMenu"))
    app.setStyle("Fusion")
    palSwitcher = utils.PaletteSwitcher(app)

    if darkdetect.isDark():
        palSwitcher.setDarkPalette()

    mainWindow = MainWindow(palSwitcher)
    mainWindow.show()

    return app.exec_()


if __name__ == "__main__":
    main()
