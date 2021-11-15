# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def main():
  app = QApplication(sys.argv)
  mainWindow = QMainWindow("Step01 - Scribble Tutorial with PyQt5")
  mainWindow.resize(640, 480)
  mainWindow.show()
  return app.exec_()

if __name__ == "__main__":
     main()


