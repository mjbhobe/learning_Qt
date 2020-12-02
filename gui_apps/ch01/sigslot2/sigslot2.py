# sigslot.py: a more realistic signals/slots demo
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CenteredOnDesktopWidget(QWidget):
    """
    custom widget that centers itself on screen when shown
    derive your widget (usually top window) from this widget
    """
    def __init__(self, *args, **kwargs):
        super(CenteredOnDesktopWidget, self).__init__(*args, **kwargs)

    def show(self):
        """
        shows the widget centered on desktop
        """
        super(CenteredOnDesktopWidget,self).show()
        screenSize = QApplication.desktop().screenGeometry()
        left = (screenSize.width() - self.width()) // 2
        top  = (screenSize.height() - self.height()) // 2
        self.move(left, top)

class SigSlotWidget(CenteredOnDesktopWidget):
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
    font = QFont("Segoe UI", 12)
    app.setFont(font)

    w = SigSlotWidget()
    w.show()
    return app.exec_()

if __name__ == '__main__':
    main()
