# tempConverter.py: temperature converter app
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import tempConverterDialog as tc

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

class TempConverter(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = tc.Ui_TempConverterDialog()
        self.ui.setupUi(self)
        # setup correct range
        self.ui.slideFahren.setRange(
            self.c2f(self.ui.spinCelcius.minimum()),
            self.c2f(self.ui.spinCelcius.maximum())
        )
        #self.ui.slideFahren.setDisabled(True)
        # setup some signals & slots
        self.ui.spinCelcius.valueChanged.connect(self.convertTemp)
        self.ui.btnQuit.clicked.connect(QApplication.instance().quit)
        # kick-off the signals & slots
        self.ui.spinCelcius.setValue(35)

    def c2f(self, celcius):
        fahrenheit = int((int(celcius) * 1.8) + 32.0)
        return fahrenheit

    def convertTemp(self):
        celcius = self.ui.spinCelcius.value()
        fahrenheit = self.c2f(celcius)
        self.ui.slideFahren.setValue(fahrenheit)
        self.ui.lblFahren.setText(f"{fahrenheit}")

def main():
    app = QApplication(sys.argv)

    w = TempConverter()
    w.show()
    return app.exec_()

if __name__ == '__main__':
    main()
