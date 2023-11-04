# unGSTfy_PyQt

### [main.py](main.py)
This is the entry point of the application. Create an instance of `QApplication` here and launch main window.

### Development Flow
- In views.py of `mainwindow` module create a class `MainWindowView` and inherit the `QMainWindow` class of PyQt6.QtWidgets.
- In controller.py of `mainwindow` module create a class `MainWindowController` and inherit the class `MainWindowView` importing from views.py.
- In another class create object of this controller.py class `MainWindowController` and invoke that screen to display.
- If invoking for the first time in main.py invoke the mainwindow class, `MainWindowController` in it.

- Never ever import any of your custom python modules in any of your [config/](config/) dir files.

Using Python Version: 3.10.11

### Pyinstaller

#### Command to build single executable file
```sh
pyinstaller --noconfirm --onefile --windowed --clean --name "unGSTfy" --icon "D:/FULL_PATH/unGSTfy_PyQt/assets/icons/gst_logo.ico" --log-level "INFO" --add-data "D:/FULL_PATH/unGSTfy_PyQt/assets;assets/"  "D:/FULL_PATH/unGSTfy_PyQt/main.py"
```

#### Command for debugging with console based executable and directory bulid.
```sh
pyinstaller --noconfirm --onedir --console --clean --name "unGSTfy" --icon "D:/FULL_PATH/unGSTfy_PyQt/assets/icons/gst_logo.ico" --log-level "INFO" --add-data "D:/FULL_PATH/unGSTfy_PyQt/assets;assets/"  "D:/FULL_PATH/unGSTfy_PyQt/main.py"
```


### AppData Paths:
- Windows : `C:/Users/USERNAME/AppData/Roaming/unGSTfy/`
- macOS : 
- LINUX : 
