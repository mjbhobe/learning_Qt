# utils.py: common code across all projects
import globalvars

USING_PYQT6 = globalvars.USING_PYQT6

if USING_PYQT6:
    from PyQt6.QtCore import *
    from PyQt6.QtWidgets import *
else:
    from PyQt5.QtCore import *
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
        shows the widget centered on active desktop
        """
        super(CenteredOnDesktopWidget, self).show()
        screenSize = QApplication.instance().primaryScreen().size() \
            if USING_PYQT6 else QApplication.desktop().screenGeometry()
        left = (screenSize.width() - self.width()) // 2
        top = (screenSize.height() - self.height()) // 2
        self.move(left, top)

    def showCenteredOnDesktop(widget):
        """
        class function to center any widget on desktop
        """
        widget.show()
        screenSize = QApplication.instance().primaryScreen().size() \
            if USING_PYQT6 else QApplication.instance().desktop().screenGeometry()
        left = (screenSize.width() - widget.width()) // 2
        top = (screenSize.height() - widget.height()) // 2
        widget.move(left, top)
