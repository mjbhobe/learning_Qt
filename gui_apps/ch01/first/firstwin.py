# firstwin.py: Hello PyQt with a QMainWindow
import sys
import pathlib
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

USING_PYQT6 = True if PYQT_VERSION_STR.startswith('6') else False

p = pathlib.Path(__file__)
print(f"Current file's path is {str(p)}")
p.parents[2]
print(f"p.parents[2] = {str(p.parents[2])}")
sys.path.append(str(p.parents[2]))
import globalvars
globalvars.USING_PYQT6 = USING_PYQT6
import utils


class FirstWin(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        msg = f"This is a PyQt5 QMainWindow!\n"
        msg = msg + f"You are using Qt version {QT_VERSION_STR}"
        self.label = QLabel(msg)
        alignment = Qt.AlignmentFlag.AlignCenter if USING_PYQT6 else Qt.AlignCenter
        self.label.setAlignment(alignment)
        self.setWindowTitle("Hello PyQt")
        self.centralWidget = QWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)


def main():
    app = QApplication(sys.argv)
    font = QFont(app.font('QMenu'))
    app.setFont(font)

    w = FirstWin()
    utils.CenteredOnDesktopWidget.showCenteredOnDesktop(w)
    return app.exec()


if __name__ == '__main__':
    main()
