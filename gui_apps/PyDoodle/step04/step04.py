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
import os
import pathlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainWindow import *
import darkdetect

sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common'))
import mypyqt5_utils as utils

# @see: https://stackoverflow.com/questions/59262975/how-to-determine-an-active-screen-monitor-of-my-application-window-using-pyt
# fire up a temporary QApplication


def get_resolution(app):

    #app = QApplication(sys.argv)

    print(app.primaryScreen())

    d = app.desktop()

    print(f"Screen Geom = {d.screenGeometry()}")
    print(f"Available Geom = {d.availableGeometry()}")
    print(f"Available screen count = {d.screenCount()}")

    g = d.screenGeometry()
    return (g.width(), g.height())


def main():
    app = QApplication(sys.argv)
    app.setFont(QApplication.font("QMenu"))
    app.setStyle("Fusion")

    sys.path.append(os.path.join(pathlib.Path(__file__).parents[1], 'common'))
    import mypyqt5_utils as utils

    if darkdetect.isDark():
        utils.setDarkPalette(app)

    x, y = get_resolution(app)

    if x > 1920 and y > 1080:
        # HD display
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
        if sys.platform == "win32":
            font = QFont("Segoe UI", 12)
            app.setFont(font)
    else:
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, False)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, False)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
