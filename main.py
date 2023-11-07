import atexit
import sys

from PyQt6.QtWidgets import QApplication

from modules.mainwindow.mainwindow_controllers import MainWindowController
from config.settings import LocalDatabaseManager

from utils import app_logging    # Setup logging for the entire application.



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window_controller_obj = MainWindowController()
    atexit.register(LocalDatabaseManager.close_connection)
    sys.exit(app.exec())
