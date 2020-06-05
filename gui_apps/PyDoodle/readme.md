# PyQt5 Doodle Tutorial

This is a step-by-step tutorial where we develop a rudimentary doodling application using PyQt5. The aim is to illustrate how easy it is to develop fairly rich GUI applications in Python using PyQt5.

Our application will include a standard menu bar & toolbar and will allow us to draw doodles using a mouse. A doodle is a collection of swiggles, each of which can have it's own color & thickness.

The final version will look somewhat like the image below.

<div style='background-color: yellow'>
[TODO: Insert Final Image]()
</div>

## Requirements
- Python 3.0+ (I used Python 3.7)
- PyQt5 framework.
- PyQt5 tools, like Designer to layout forms & dialogs.
- A text editor of your choice that provides syntax highlighting of Python code and allows you to run `*.py` files from the editor. I use the Atom editor with the script plugin.

### Installing PyQt5
It is assumed that you have Python installed. A full scientific Python stack (like the one available at Ananconda.com is highly recommended, but not required)

- On the command line (Unix/Linux or Mac terminal or Windows command prompt), run _either_ of the following:
    * If you have the Anaconda distribution
        ```bash
        $> conda install -c dsdale24 pyqt5
        ```
    * You can also use pip as below (refer [this link](https://pypi.org/project/PyQt5/))
        ```bash
        $> pip install PyQt5
        ```

## Code Organization
I have developed this code in several incremental _steps_. Each _step_ has it's own directory. The _main_ file is named `step0X.py` - where `X` designates the step number (e.g. `step01.py`). To _run the program_ for any step, change to the directory of that step (e.g. `step05`) and fun the following command:
```bash
$> python step05.py
```

## **NOTE**
I have written this tutorial on an Ubuntu Linux machine. All the screen-shots enclosed in the documentation are from the Ubuntu Linux platform. However, due to Python's cross-platform nature, the _same_ code can run on both Windows and Mac without any changes. Your Window's look and feel would then be native to the platform on which you code.
