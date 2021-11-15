# sigslot.py: illustrates signals & slots
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


class SigSlotWidget(utils.CenteredOnDesktopWidget):
    def __init__(self, *args, **kwargs):
        super(SigSlotWidget, self).__init__(*args, **kwargs)

        # setup Gui
        self.setWindowTitle("PyQt: Signals & Slots")
        self.label = QLabel("Click the button to quit application")
        self.btn = QPushButton("Quit!")
        self.btn.setDefault(True)
        self.btn.setToolTip("Close Application")
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout)
        self.setLayout(mainLayout)

        # connect signals & slots
        self.btn.clicked.connect(self.confirmQuit)

    def confirmQuit(self):
        # version1 - just quit
        # QApplication.instance().quit()

        # version 2 - ask & quit
        buttons = QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes \
            if USING_PYQT6 else QMessageBox.No | QMessageBox.Yes
        defButton = QMessageBox.StandardButton.No if USING_PYQT6 else \
            QMessageBox.No
        resp = QMessageBox.question(self, "Please Confirm",
                                    "This will quit the application\nOk to close?",
                                    buttons, defButton)
        if resp == (QMessageBox.StandardButton.Yes if USING_PYQT6 else QMessageBox.Yes):
            QApplication.instance().quit()


def main():
    app = QApplication(sys.argv)
    # font = QFont(app.font().family(), 12)
    # app.setFont(font)
    app.setFont(QApplication.font("QMenu"))

    w = SigSlotWidget()
    w.show()
    return app.exec()


if __name__ == '__main__':
    main()
