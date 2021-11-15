import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ByteConverterDialog

# @see: https://stackoverflow.com/questions/59262975/how-to-determine-an-active-screen-monitor-of-my-application-window-using-pyt
# fire up a temporary QApplication
def get_resolution(app):
    print(app.primaryScreen())
    d = app.desktop()

    print(f"Screen Geom = {d.screenGeometry()}")
    print(f"Available Geom = {d.availableGeometry()}")
    print(f"Available screen count = {d.screenCount()}")

    g = d.screenGeometry()
    return (g.width(), g.height())

def isHDDisplay(app):
    x, y = get_resolution(app)
    isHD = False
    if (x >= 1920) and (y >= 1080): isHD = True
    print(f"You {'have' if isHD else 'dont have'} an HD display!")
    return isHD

class QHelperDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
    def setupDialog():
        pass

class ByteConverterDlgFromUi(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ByteConverterDialog.Ui_Dialog()
        self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)
    HD_FONT = QFont(app.font().family(), 12) if isHDDisplay(app) else None

    if isHDDisplay(app):
        # HD display
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    else:
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, False)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, False)

    if (sys.platform == "win32") and isHDDisplay(app) and (HD_FONT is not None):
        app.setFont(HD_FONT)

    # call up the ByteConverterDialog
    dialog = ByteConverterDlgFromUi()
    if (sys.platform == "win32") and isHDDisplay(app) and (HD_FONT is not None):
        dialog.setFont(HD_FONT)
    dialog.exec()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
