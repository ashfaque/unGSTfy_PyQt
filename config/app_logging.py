import os
import sys

from AshLogger import AshLogger
from PyQt6 import QtCore
from config.constants import (
    DEV_MODE_APP_DATA_DIR_NAME
    , LOG_FILE_NAME
    , LOG_FILE_DIR
    , LOG_FILE_SIZE
    , LOG_FILE_BACKUPS
)


# ? Get the writable location for application data, platform independent.
def get_app_data_dir():    # Declared this function here to avoid circular import with utils/global_functions.py
    if getattr(sys, 'frozen', False):
        return QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppDataLocation)
    else:    # If development environment.
        return os.getcwd() + f"/{DEV_MODE_APP_DATA_DIR_NAME}"



logger_obj = AshLogger(
                file_name=LOG_FILE_NAME
                , file_location=os.path.join(get_app_data_dir(), LOG_FILE_DIR)
                , max_bytes=LOG_FILE_SIZE * 1000 * 1000    # In bytes
                , max_backups=LOG_FILE_BACKUPS
            )
logger = logger_obj.setup_logger()


def custom_exception_handler(exc_type, exc_value, exc_traceback):
    print(f"Uncaught exception: {exc_type}, {exc_value}")

    logger.debug("Uncaught exception::: ", exc_info=(exc_type, exc_value, exc_traceback))


# Set the custom exception handler globally.
sys.excepthook = custom_exception_handler



# Utility function to trigger a manual exception and log it.
def trigger_manual_exception_and_log_it(exception_msg: str, close_app: bool = False):
    '''
    Usage:    trigger_manual_exception_and_log_it("Error: Failed to create table" + query.lastError().text(), close_app=True)
    '''
    try:
        raise Exception(str(exception_msg))
    except Exception as ex:
        custom_exception_handler(type(ex), ex, ex.__traceback__)
    finally:
        if close_app:
            sys.exit(1)



'''
# Setting up DEBUG level logging for the entire application.

import os
import logging
# Create a logger
logger = logging.getLogger(__name__)

# Create a file handler to log to a specific file
log_file = 'logs/debug.log'    # Set the desired log file path w.r.t the project root directory.

if not os.path.exists(os.path.dirname(log_file)):
    os.makedirs(os.path.dirname(log_file))

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

'''
