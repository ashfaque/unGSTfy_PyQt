import sys

from PyQt6.QtWidgets import QApplication

from modules.mainwindow.mainwindow_controllers import MainWindowController


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window_controller_obj = MainWindowController()
    sys.exit(app.exec())
