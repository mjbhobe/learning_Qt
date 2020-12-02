# sigslot.py: illustrates signals & slots
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
        self.setWindowTitle("PyQt: Signals & Slots")
        self.label = QLabel("Click the button to quit application")
        self.btn = QPushButton("Quit!")
        self.btn.setDefault(True)
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
        #QApplication.instance().quit()

        # version 2 - ask & quit
        resp = QMessageBox.question(self, "Please Confirm",
                "This will quit the application\nOk to close?",
                QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if resp == QMessageBox.Yes:
            QApplication.instance().quit()

def main():
    app = QApplication(sys.argv)
    font = QFont("Segoe UI", 12)
    app.setFont(font)

    w = SigSlotWidget()
    w.show()
    return app.exec_()

if __name__ == '__main__':
    main()
