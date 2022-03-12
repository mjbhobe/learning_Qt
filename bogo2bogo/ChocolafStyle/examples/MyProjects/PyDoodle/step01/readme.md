# PyQt5 Doodle Tutorial

## Step 1 - Creating the basic window
In this step, we will create the basic window within which the doodles will be drawn. Our main window will be a class derived from the `PyQt5.QtWidgets.QMainWindow` class.

In this step, the application does nothing else but display the main window, which can be minimized, maximized, resized and moved around. In the subsequent steps, we will gradually add more and more functionality to the application.

### Coding Steps
1. First create a **root directory** under which we will create sub-directories for each step of this tutorial. This folder could be created anywhere on your disk. For example, I have created a directory named `PyDoodle` under a `code` directory off my `home` directory in my Ubuntu Linux machine.<br/>
<span style="background-color:salmon; color:black">So my root directory is `~/code/PyDoodle`. **Henceforth, I'll refer to this directory as the `root directory`.**</span>
2. Next create a sub-folder `step01` under the `root directory`.
3. Fire up your favorite code editor (I use Atom) and create a new file, named `mainWindow.py`, in the `step01` directory. We will define our `QMainWindow` derived class in this file as below:

```python
# step01/mainWindow.py - main window of application
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("PyQt Doodle - Step01: Basic Window")
        self.setStyleSheet("background-color: white")
        self.setGeometry(QRect(100,100,640,480))


```

For this step, just the constructor `__init__()` method is enough. In this method, we define some customizations for the main window:
- We set the title of the main window using the `setWindowTitle()` method
- We also set the background color of the client area of the window using the `setStyleSheet()` function
- Finally, we set the initial size of the window using the `setGeometry()` call.

4. Next create the Python module that will call this class & initiate the event loop. Create another file `step01.py` in the `step01` directory. Here is the code for `step01/step01.py`

```python
# step01/step01.py: driver module
import sys
from PyQt5.QtGui import *
from mainWindow import *

def main():
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
```
We import our `MainWindow` class with the `from mainWindow import *` call.

5. Run `step01.py` - it will display the following window:

![Step01](./images/Step01.png)

This is a simple high level window which can be moved, resized, minimized, maximized and closed - but does nothing else.

<hr/>

<span style="color:blue">This completes Step1 of our tutorial.</span>  In the next step we will add code to handle operating system events.

__NOTE:__ I have written this tutorial on a Ubuntu Linux machine, so the window look & feel is specific to my OS. On a Windows machine, the look & feel will be native to Windows, and likewise on a Mac. However, you won't have to change your code - PyQt5 handles the low level stuff for you.
