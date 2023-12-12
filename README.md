# unGSTfy_PyQt

### [main.py](main.py)
This is the entry point of the application. Create an instance of `QApplication` here and launch main window.

### Development Flow
- In views.py of `mainwindow` module create a class `MainWindowView` and inherit the `QMainWindow` class of PyQt6.QtWidgets.
- In controller.py of `mainwindow` module create a class `MainWindowController` and inherit the class `MainWindowView` importing from views.py.
- In another class create object of this controller.py class `MainWindowController` and invoke that screen to display.
- If invoking for the first time in main.py invoke the mainwindow class, `MainWindowController` in it.

- **IMPORTANT:** Never ever import any of your custom python modules in any of your [config/](config/) dir files.

- Using Python Version: 3.10.11, then switched to 3.11.5.
    - conda create -n gstenv python 3.11.5
    - conda activate gstenv

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


#### Use QThread for long running task without freezing GUI: https://realpython.com/python-pyqt-qthread/


'''
os.path.expanduser
Used to expand an initial path component ~( tilde symbol) or ~user in the given path to user's home directory.
On Unix platforms, an initial ~ is replaced by the value of HOME environment variable, if it is set. Otherwise, os.path.expanduser() method search for user’s home directory in password directory using an in-built module pwd. Path containing an initial ~user component is looked up directly in the password directory.
On Windows platform, an initial ~ is replaced by the value of HOME and USERPROFILE environment variable, if it is set. Otherwise, HOMEPATH and HOMEDRIVE environment variable will be used. While Path containing an initial ~user component is handled by replacing the last directory component with ~user from the path derived above.
'''

Multi resolution .ico file from png file [https://www.aconvert.com/icon/png-to-ico/](https://www.aconvert.com/icon/png-to-ico/)
