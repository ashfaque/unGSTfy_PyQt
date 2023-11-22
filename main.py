import atexit
from pdb import set_trace as bp
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QFile, QLockFile

from modules.mainwindow.mainwindow_controllers import MainWindowController
from config.settings import LocalDatabaseManager
from config.ui_element_names import APP_NAME
from config import app_logging    # ? Setup logging for the entire application. By just importing this module, logging is setup for the entire application.



def remove_lock_file():
    if lock_file.isLocked():    # As lock_file is defined in global scope, it can be accessed here.
        lock_file.unlock()    # Removes the lock file, when the application is about to close.
    QFile(lock_file_path).remove()    # * If execution reaches here, it auto removes that lock file if any dangling lock files are present in the file system, which is unremoved after the application closed. Due to user killing the process or tampering with the lock file, etc.


if __name__ == "__main__":
    app = QApplication(sys.argv)

    lock_file_path = f"{app_logging.get_app_data_dir()}/.{APP_NAME}.lock"
    lock_file = QLockFile(QFile(lock_file_path).fileName())

    if lock_file.tryLock():    # If able to lock the file, it means no other instance of the application is running.
        main_window_controller_obj = MainWindowController()
        atexit.register(LocalDatabaseManager.close_connection)
        atexit.register(remove_lock_file)
        sys.exit(app.exec())
    else:
        # * If user is facing any problem launching the application, like it crashes when launched, then it might be due to the dangling lock file present in the file system. So, reboot the system & remove the lock file and try again.
        remove_lock_file()
        # from PyQt6.QtWidgets import QMessageBox
        # error_message = QMessageBox()
        # error_message.setIcon(QMessageBox.Warning)
        # error_message.setWindowTitle("Error")
        # error_message.setText("The application is already running!")
        # error_message.setStandardButtons(QMessageBox.Ok)
        # error_message.exec()
        app_logging.trigger_manual_exception_and_log_it("The application is already running!", close_app=True)
