import sys

from PyQt6.QtWidgets import QApplication

from modules.mainwindow.mainwindow_controllers import MainWindowController

# TODO: Setup better DEBUG logging
''' Logging Starts '''

import logging
# Create a logger
logger = logging.getLogger(__name__)

# Create a file handler to log to a specific file
log_file = 'debug.log'    # Set the desired log file path
file_handler = logging.FileHandler(log_file)

# Create a formatter to specify the log message format
formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
file_handler.setFormatter(formatter)

# Set the logger level (adjust as needed)
logger.setLevel(logging.DEBUG)

# Add the file handler to the logger
logger.addHandler(file_handler)


def custom_exception_handler(exc_type, exc_value, exc_traceback):
    logger = logging.getLogger(__name__)    # You can customize the logger name.
    print(f"Uncaught exception: {exc_type}, {exc_value}")
    logger.error("Uncaught exception: ", exc_info=(exc_type, exc_value, exc_traceback))

# Set the custom exception handler globally.
sys.excepthook = custom_exception_handler

''' Logging Ends '''



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window_controller_obj = MainWindowController()
    sys.exit(app.exec())
