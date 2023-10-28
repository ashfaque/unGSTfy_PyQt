# unGSTfy_PyQt

### [main.py](main.py)
This is the entry point of the application. Create an instance of `QApplication` here and launch main window.

### Development Flow
- In views.py of `mainwindow` module create a class `MainWindowView` and inherit the `QMainWindow` class of PyQt6.QtWidgets.
- In controller.py of `mainwindow` module create a class `MainWindowController` and inherit the class `MainWindowView` importing from views.py.
- In another class create object of this controller.py class `MainWindowController` and invoke that screen to display.
- If invoking for the first time in main.py invoke the mainwindow class, `MainWindowController` in it.

