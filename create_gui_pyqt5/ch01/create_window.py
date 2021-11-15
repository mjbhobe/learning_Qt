# create_window.py
import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget
)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt6: create basic window')
window.show()

# run your application
app.exec()
