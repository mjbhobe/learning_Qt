# first.py : Hello World with PyQt5
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
        super(CenterOnDesktopWidget, self).__init__(*args, **kwargs)

    def show(self):
        """
        shows the widget centered on desktop
        """
        super(CenteredOnDesktopWidget,self).show()
        screenSize = QApplication.desktop().screenGeometry()
        left = (screenSize.width() - self.width()) // 2
        top  = (screenSize.height() - self.height()) // 2
        self.move(left, top)

class First(CenteredOnDesktopWidget):
    def __init__(self, *args, **kwargs):
        super(CenteredOnDesktopWidget, self).__init__(*args, **kwargs)
        msg = f"This is a PyQt5 application!\n"
        msg = msg +  f"You are using Qt version {QT_VERSION_STR}"
        self.label = QLabel(msg)
        self.setWindowTitle("Hello PyQt")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    font = QFont("Segoe UI", 12)
    app.setFont(font)

    w = First()
    w.show()
    return app.exec_()

if __name__ == '__main__':
    main()
