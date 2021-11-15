# layout.py: illustrates layouts in PyQt
import sys
import pathlib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

USING_PYQT6 = True if PYQT_VERSION_STR.startswith('6') else False

p = pathlib.Path(__file__)
print(f"Current file's path is {str(p)}")
p.parents[2]
print(f"p.parents[2] = {str(p.parents[2])}")
sys.path.append(str(p.parents[2]))
import globalvars
globalvars.USING_PYQT6 = USING_PYQT6
import utils


class LayoutWidget(utils.CenteredOnDesktopWidget):
    def __init__(self, *args, **kwargs):
        super(utils.CenteredOnDesktopWidget, self).__init__(*args, **kwargs)
        self.setWindowTitle("Qt Layouts Example")

        messages = ["PyQt5", "makes", "creating",
                    "GUI apps really easy!"]

        layout = QVBoxLayout()
        lblLayout = QHBoxLayout()
        glayout = QGridLayout()
        glayout.horizontalSpacing = 5
        glayout.verticalSpacing = 5

        for i, msg in enumerate(messages):
            #lbl = QLabel(msg)
            btn = QPushButton(msg)
            if i == len(messages) - 1:
                # lbl.setAlignment(Qt.AlignCenter)
                glayout.addWidget(btn, 1, 0, 1, i)
            else:
                glayout.addWidget(btn, 0, i)
        lbl = QLabel("")  # will display
        layout.addLayout(glayout)
        layout.addLayout(lblLayout)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    #font = QFont(app.font().family(), 11)
    # app.setFont(font)
    app.setFont(QApplication.font("QMenu"))

    w = LayoutWidget()
    w.show()
    return app.exec()


if __name__ == '__main__':
    main()
