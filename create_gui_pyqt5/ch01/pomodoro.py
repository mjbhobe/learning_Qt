# pomodoro.py: pomodoro technique
import sys, platform

from PyQt5.QtCore import Qt, QTimer, PYQT_VERSION_STR
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLCDNumber, QPushButton, QLabel, QLineEdit,
    QGroupBox, QTabWidget, QVBoxLayout, QHBoxLayout
)

# globals
POMODORO_TIME = 25 * 60 * 60    # 25 mins as millisecs
SHORT_BREAK_TIME = 5 * 60 * 60  # 5 mins as millisecs
LONG_BREAK_TIME = 15 * 60 * 60        # 15 mins as millisecs

class PomodoroTimerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """initialize the GUI & widgets"""
        self.setMinimumSize(500,400)
        self.setWindowTitle("1.1 - Pomodoro Timer")
        self.setWindowIcon(QIcon("images/pomodoro.png"))
        self.pomodoro_limit = POMODORO_TIME
        self.short_break_limit = SHORT_BREAK_TIME
        self.long_break_limit = LONG_BREAK_TIME
        self.setupTabsAndWidgets()

        # variables for current tabs & widgets
        self.current_tab_selected = 0
        self.current_start_button = self.pomodoro_start_button
        self.current_stop_button = self.pomodoro_stop_button
        self.current_reset_button = self.pomodoro_reset_button
        self.current_time_limit = self.pomodoro_limit
        self.current_lcd = self.pomodoro_lcd

        # variables for user's current tasks
        self.task_is_set = False
        self.number_of_tasks = 0
        self.task_complete_counter = 0

        # create timer object
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)

    def setupTabsAndWidgets(self):
        """setup tab bar for different pomodoro stages: pomodoro, short break
           and long break"""
        self.tab_bar = QTabWidget(self)
        self.pomodoro_tab = QWidget()
        self.pomodoro_tab.setObjectName("Pomodoro")
        self.short_break_tab = QWidget()
        self.short_break_tab.setObjectName("ShortBreak")
        self.long_break_tab = QWidget()
        self.long_break_tab.setObjectName("LongBreak")

        self.tab_bar.addTab(self.pomodoro_tab, "Pomodoro")
        self.tab_bar.addTab(self.short_break_tab, "Short Break")
        self.tab_bar.addTab(self.long_break_tab, "Long Break")

        # setup signal & slot
        self.tab_bar.currentChanged.connect(self.tabSwitched)

        # setup individual tabs
        self.setupPomodoroTab()
        self.setupShortBreakTab()
        self.setupLongBreakTab()

        self.enter_task_lineEdit = QLineEdit()
        self.enter_task_lineEdit.setClearButtonEnabled(True)
        self.enter_task_lineEdit.setPlaceholderText("Enter you current task")

        confirm_task_button = QPushButton(QIcon('images/plus.png'), None)
        confirm_task_button.setObjectName('ConfirmButton')
        confirm_task_button.clicked.connect(self.addTaskToTaskbar)

        task_entry_h_box = QHBoxLayout()
        task_entry_h_box.addWidget(self.enter_task_lineEdit)
        task_entry_h_box.addWidget(confirm_task_button)

        self.task_v_box = QVBoxLayout()

        task_v_box = QVBoxLayout()
        task_v_box.addLayout(task_entry_h_box)
        task_v_box.addLayout(self.task_v_box)

        # Container for taskbar
        task_bar_gb = QGroupBox("Tasks")
        task_bar_gb.setLayout(task_v_box)

        # Create and set layout for the main window
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.tab_bar)
        main_v_box.addWidget(task_bar_gb)

        # small text showing PyQt version used
        pyqt_layout = QHBoxLayout()
        python_ver = f"{platform.python_version()}"
        pyqt_ver_str = f"Build with Python {python_ver} and PyQt {PYQT_VERSION_STR}"
        pyqt_ver_label = QLabel(pyqt_ver_str)
        pyqt_layout.addWidget(pyqt_ver_label)
        pyqt_layout.addStretch()
        main_v_box.addLayout(pyqt_layout)

        self.setLayout(main_v_box)

    def setupPomodoroTab(self):
        """Set up the Pomodoro tab, widgets and layout."""
        # Convert starting time to display on timer
        start_time = self.calculateDisplayTime(self.pomodoro_limit)
        self.pomodoro_lcd = QLCDNumber()
        self.pomodoro_lcd.setObjectName("PomodoroLCD")
        self.pomodoro_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.pomodoro_lcd.display(start_time)
        self.pomodoro_start_button = QPushButton("Start")
        self.pomodoro_start_button.clicked.connect(self.startCountDown)
        self.pomodoro_stop_button = QPushButton("Stop")
        self.pomodoro_stop_button.clicked.connect(self.stopCountDown)
        self.pomodoro_reset_button = QPushButton("Reset")
        self.pomodoro_reset_button.clicked.connect(self.resetCountDown)
        # Horizontal layout for buttons
        button_h_box = QHBoxLayout()
        button_h_box.addWidget(self.pomodoro_start_button)
        button_h_box.addWidget(self.pomodoro_stop_button)
        button_h_box.addWidget(self.pomodoro_reset_button)
        # Create and set layout for the pomodoro tab
        v_box = QVBoxLayout()
        v_box.addWidget(self.pomodoro_lcd)
        v_box.addLayout(button_h_box)
        self.pomodoro_tab.setLayout(v_box)

    def setupShortBreakTab(self):
        """Set up the short break tab, widgets and layout."""
        # Convert starting time to display on timer
        start_time = self.calculateDisplayTime(self.short_break_limit)
        self.short_break_lcd = QLCDNumber()
        self.short_break_lcd.setObjectName("ShortLCD")
        self.short_break_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.short_break_lcd.display(start_time)
        self.short_start_button = QPushButton("Start")
        self.short_start_button.clicked.connect(self.startCountDown)
        self.short_stop_button = QPushButton("Stop")
        self.short_stop_button.clicked.connect(self.stopCountDown)
        self.short_reset_button = QPushButton("Reset")
        self.short_reset_button.clicked.connect(self.resetCountDown)
        # Horizontal layout for buttons
        button_h_box = QHBoxLayout()
        button_h_box.addWidget(self.short_start_button)
        button_h_box.addWidget(self.short_stop_button)
        button_h_box.addWidget(self.short_reset_button)
        # Create and set layout for the short break tab
        v_box = QVBoxLayout()
        v_box.addWidget(self.short_break_lcd)
        v_box.addLayout(button_h_box)
        self.short_break_tab.setLayout(v_box)

    def setupLongBreakTab(self):
        """Set up the long break tab, widgets and layout."""
        # Convert starting time to display on timer
        start_time = self.calculateDisplayTime(self.long_break_limit)
        self.long_break_lcd = QLCDNumber()
        self.long_break_lcd.setObjectName("LongLCD")
        self.long_break_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.long_break_lcd.display(start_time)
        self.long_start_button = QPushButton("Start")
        self.long_start_button.clicked.connect(self.startCountDown)
        self.long_stop_button = QPushButton("Stop")
        self.long_stop_button.clicked.connect(self.stopCountDown)
        self.long_reset_button = QPushButton("Reset")
        self.long_reset_button.clicked.connect(self.resetCountDown)
        # Horizontal layout for buttons
        button_h_box = QHBoxLayout()
        button_h_box.addWidget(self.long_start_button)
        button_h_box.addWidget(self.long_stop_button)
        button_h_box.addWidget(self.long_reset_button)
        # Create and set layout for the long break tab
        v_box = QVBoxLayout()
        v_box.addWidget(self.long_break_lcd)
        v_box.addLayout(button_h_box)
        self.long_break_tab.setLayout(v_box)

    def startCountDown(self):
        """Starts the timer. If the current tab's time is 00:00, reset the
        time if user pushes the start button."""
        self.current_start_button.setEnabled(False)
        # Used to reset counter_label if user has already has completed four
        # pomodoro cycles
        if (self.task_is_set is True) and (self.task_complete_counter == 0):
            self.counter_label.setText("{}/4".format(self.task_complete_counter))
        remaining_time = self.calculateDisplayTime(self.current_time_limit)
        if remaining_time == "00:00":
            self.resetCountDown()
            self.timer.start(1000)
        else:
            self.timer.start(1000)

    def stopCountDown(self):
        """If the timer is already running, then stop the timer."""
        if (self.timer.isActive() is not False):
            self.timer.stop()
            self.current_start_button.setEnabled(True)

    def resetCountDown(self):
        """Resets the time for the current tab when the reset button is
        selected."""
        # Stop countdown if timer is running
        self.stopCountDown()
        # Reset time for currently selected tab
        if self.current_tab_selected == 0:
            # Pomodoro tab
            self.pomodoro_limit = POMODORO_TIME
            self.current_time_limit = self.pomodoro_limit
            reset_time = self.calculateDisplayTime(self.current_time_limit)
        elif self.current_tab_selected == 1:
            # Short break tab
            self.short_break_limit = SHORT_BREAK_TIME
            self.current_time_limit = self.short_break_limit
            reset_time = self.calculateDisplayTime(self.current_time_limit)
        elif self.current_tab_selected == 2:
            # Long break tab
            self.long_break_limit = LONG_BREAK_TIME
            self.current_time_limit = self.long_break_limit
            reset_time = self.calculateDisplayTime(self.current_time_limit)

        self.current_lcd.display(reset_time)

    def updateTimer(self):
        """Updates the timer and the current QLCDNumber widget. Also,
        update the task counter if a task is set."""
        remaining_time = self.calculateDisplayTime(self.current_time_limit)
        if remaining_time == "00:00":
            self.stopCountDown()
            self.current_lcd.display(remaining_time)

            if (self.current_tab_selected == 0) and (self.task_is_set is True):
                self.task_complete_counter += 1
                if self.task_complete_counter == 4:
                    self.counter_label.setText(
                        f"Time for a long break.{self.task_complete_counter}/4")
                    self.task_complete_counter = 0
            elif self.task_complete_counter < 4:
                self.counter_label.setText(f"{self.task_complete_counter}/4")
        else:
            # Update the current timer by decreasing the current running
            # time by one second
            self.current_time_limit -= 1000
            self.current_lcd.display(remaining_time)

    def tabSwitched(self, index):
        """Depending upon which tab the user is currently looking at, the
        information for that tab needs to be updated. This function updates
        the different variables that keep track of the timer, buttons, lcds
        and other widgets, and update them accordingly."""
        self.current_tab_selected = index
        self.stopCountDown()
        # Reset variables, time and widgets depending upon which tab is the
        # current_tab_selected
        if self.current_tab_selected == 0:
            # Pomodoro tab
            self.current_start_button = self.pomodoro_start_button
            self.current_stop_button = self.pomodoro_stop_button
            self.current_reset_button = self.pomodoro_reset_button
            self.pomodoro_limit = POMODORO_TIME
            self.current_time_limit = self.pomodoro_limit
            reset_time = self.calculateDisplayTime(self.current_time_limit)
            self.current_lcd = self.pomodoro_lcd
            self.current_lcd.display(reset_time)
        elif self.current_tab_selected == 1:
            # Short break tab
            self.current_start_button = self.short_start_button
            self.current_stop_button = self.short_stop_button
            self.current_reset_button = self.short_reset_button
            self.short_break_limit = SHORT_BREAK_TIME
            self.current_time_limit = self.short_break_limit
            reset_time = self.calculateDisplayTime(self.current_time_limit)
            self.current_lcd = self.short_break_lcd
            self.current_lcd.display(reset_time)
        elif self.current_tab_selected == 2:
            # Long break tab
            self.current_start_button = self.long_start_button
            self.current_stop_button = self.long_stop_button
            self.current_reset_button = self.long_reset_button
            self.long_break_limit = LONG_BREAK_TIME
            self.current_time_limit = self.long_break_limit
            reset_time = self.calculateDisplayTime(self.current_time_limit)
            self.current_lcd = self.long_break_lcd
            self.current_lcd.display(reset_time)

    def addTaskToTaskbar(self):
        """When the user clicks the plus button, the widgets for the new
        task will be added to the task bar. Only one task is allowed to be
        entered at a time."""
        text = self.enter_task_lineedit.text()
        self.enter_task_lineedit.clear()

        # Change number_of_tasks if you want to ask more tasks to the task bar
        if (text != "") and (self.number_of_tasks != 1):
            self.enter_task_lineedit.setReadOnly(True)
            self.task_is_set = True
            new_task = QLabel(text)
            self.counter_label = QLabel("{}/4".format(self.task_complete_counter))
            self.counter_label.setAlignment(Qt.AlignRight)

            cancel_task_button = QPushButton(QIcon("images/minus.png"), None)
            cancel_task_button.setMaximumWidth(24)
            cancel_task_button.clicked.connect(self.clearCurrentTask)
            self.new_task_h_box = QHBoxLayout()
            self.new_task_h_box.addWidget(new_task)
            self.new_task_h_box.addWidget(self.counter_label)
            self.new_task_h_box.addWidget(cancel_task_button)
            self.tasks_v_box.addLayout(self.new_task_h_box)
            self.number_of_tasks += 1

    def clearCurrentTask(self):
        """Delete the current task, and reset variables and widgets related
        to tasks."""
        # Remove items from parent widget by setting the argument value in
        # setParent() to None
        self.new_task.setParent(None)
        self.counter_label.setParent(None)
        self.cancel_task_button.setParent(None)
        self.number_of_tasks -= 1
        self.task_is_set = False
        self.task_complete_counter = 0
        self.enter_task_lineedit.setReadOnly(False)

    def convertTotalTime(self, time_in_milli):
        """Convert time to milliseconds."""
        minutes = (time_in_milli / (1000 * 60)) % 60
        seconds = (time_in_milli / 1000) % 60
        return int(minutes), int(seconds)

    def calculateDisplayTime(self, time):
        """Calculate the time that should be displayed in the QLCDNumber
        widget."""
        minutes, seconds = self.convertTotalTime(time)
        amount_of_time = "{:02d}:{:02d}".format(minutes, seconds)
        return amount_of_time

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setFont(QApplication.font("QMenu"))

    window = PomodoroTimerWidget()
    window.show()

    # run your application
    sys.exit(app.exec())
