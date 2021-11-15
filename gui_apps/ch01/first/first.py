# first.py : Hello World with PyQt5
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


class First(utils.CenteredOnDesktopWidget):
    def __init__(self, *args, **kwargs):
        super(utils.CenteredOnDesktopWidget, self).__init__(*args, **kwargs)
        msg = f"This is a PyQt{PYQT_VERSION_STR[0]} application!\n"
        msg = msg + f"You are using Qt version {QT_VERSION_STR}"
        self.label = QLabel(msg)
        self.setWindowTitle("Hello PyQt")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    app.setFont(QApplication.font("QMenu"))

    w = First()
    w.show()
    return app.exec()


if __name__ == '__main__':
    main()
