import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ByteConverterDialog

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

class ByteConverterDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ByteConverterDialog.Ui_Dialog()
        self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)
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


    # call up the ByteConverterDialog
    dialog = ByteConverterDlg()
    if sys.platform == "win32":
        font = QFont("Segoe UI", 12)
        dialog.setFont(font)
    dialog.exec()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
