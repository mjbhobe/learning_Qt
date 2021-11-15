# sigslot.py: a more realistic signals/slots demo
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


class SigSlotWidget(utils.CenteredOnDesktopWidget):
    def __init__(self, *args, **kwargs):
        super(SigSlotWidget, self).__init__(*args, **kwargs)

        # setup Gui
        self.setWindowTitle("PyQt: Signals & Slots - 2")

        # build the layout
        # top row - just the prompt
        self.prompt_label = QLabel("Spin the spinbox below & see the " +
                                   "slider and label getting updated")
        # middle row: spinner - slider - label
        self.spinner = QSpinBox()
        self.spinner.setRange(-50, 50)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(-50, 50)
        self.val_label = QLabel("")
        # bottom row - hgap - push button
        self.btnQuit = QPushButton("Quit")

        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(self.spinner)
        h_layout1.addWidget(self.slider)
        h_layout1.addWidget(self.val_label)

        h_layout2 = QHBoxLayout()
        h_layout2.addStretch()
        h_layout2.addWidget(self.btnQuit)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.prompt_label)
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        self.setLayout(v_layout)

        # setup signals & slots
        self.spinner.valueChanged.connect(self.val_label.setNum)
        self.spinner.valueChanged.connect(self.slider.setValue)
        self.btnQuit.clicked.connect(QApplication.instance().quit)

        # kick-off all the signals & slots
        self.spinner.setValue(5)
        self.spinner.setValue(0)


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
