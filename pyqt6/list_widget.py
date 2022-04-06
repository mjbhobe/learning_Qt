#!/usr/bin/env python
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setMinimumSize(400, 200)
        self.setWindowTitle("QListWidget Example")
        self.setupWindow()

    def setupWindow(self):
        self.list_widget = QListWidget()
        self.list_widget.setAlternatingRowColors(True)

        grocery_list = ["grapes", "broccoli", "garlic", "cheese", 
                        "bacon", "eggs", "waffles", "rice", "soda"]

        for item in grocery_list:
            list_item = QListWidgetItem()
            list_item.setText(item)
            self.list_widget.addItem(list_item)

        # create the buttons list
        add_button = QPushButton("Add")
        add_button.clicked.connect(self.addItem)

        insert_button = QPushButton("Insert")
        insert_button.clicked.connect(self.insertItem)

        remove_button = QPushButton("Remove")
        remove_button.clicked.connect(self.removeItem)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.list_widget.clear)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(QApplication.instance().quit)

        # create layouts
        rbox = QVBoxLayout()
        rbox.addWidget(add_button)
        rbox.addWidget(insert_button)
        rbox.addWidget(remove_button)
        rbox.addWidget(clear_button)
        rbox.addWidget(exit_button)

        layout = QHBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addLayout(rbox)
        self.setLayout(layout)

    def addItem(self):
        text, ok = QInputDialog.getText(self, "New Item", "Add Item:")
        if ok and text != "":
            list_item = QListWidgetItem()
            list_item.setText(text)
            self.list_widget.addItem(list_item)

    def insertItem(self):
        pass

    def removeItem(self):
        pass

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()


