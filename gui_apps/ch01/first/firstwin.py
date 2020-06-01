# firstwin.py: Hello PyQt with a QMainWindow
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

    def centerShow(widget):
        """
        class function to center any widget on desktop
        """
        widget.show()
        screenSize = QApplication.desktop().screenGeometry()
        left = (screenSize.width() - widget.width()) // 2
        top  = (screenSize.height() - widget.height()) // 2
        widget.move(left, top)

class FirstWin(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        msg = f"This is a PyQt5 QMainWindow!\n"
        msg = msg +  f"You are using Qt version {QT_VERSION_STR}"
        self.label = QLabel(msg)
        self.label.setAlignment(Qt.AlignCenter)
        self.setWindowTitle("Hello PyQt")
        self.setCentralWidget(self.label)

def main():
    app = QApplication(sys.argv)

    w = FirstWin()
    CenteredOnDesktopWidget.centerShow(w)
    return app.exec_()

if __name__ == '__main__':
    main()
