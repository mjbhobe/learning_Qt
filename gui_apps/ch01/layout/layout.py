# layout.py: illustrates layouts in PyQt
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

class LayoutWidget(CenteredOnDesktopWidget):
    def __init__(self, *args, **kwargs):
        super(CenteredOnDesktopWidget, self).__init__(*args, **kwargs)
        self.setWindowTitle("Qt Layouts Example")

        messages = ["PyQt5", "makes", "creating",
                    "GUI apps really easy!"]

        layout = QVBoxLayout()
        glayout = QGridLayout()
        glayout.horizontalSpacing = 5
        glayout.verticalSpacing = 5

        for i, msg in enumerate(messages):
            lbl = QLabel(msg)
            if i == len(messages) - 1:
                lbl.setAlignment(Qt.AlignCenter)
                glayout.addWidget(lbl, 1, 0, 1, i)
            else:
                glayout.addWidget(lbl, 0, i)
        layout.addLayout(glayout)
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    font = QFont("Segoe UI", 12)
    app.setFont(font)

    w = LayoutWidget()
    w.show()
    return app.exec_()

if __name__ == '__main__':
    main()
