import os
import sys

from AshLogger import AshLogger
from utils.global_functions import get_app_data_dir
from config.constants import LOG_FILE_SIZE



logger_obj = AshLogger(
                file_name='unGSTfy_DEBUG.log'    # TODO: DEFINE IT IN A VARIABLE.
                , file_location=os.path.join(get_app_data_dir(), 'logs')    # TODO: DEFINE IT IN A VARIABLE.
                , max_bytes=LOG_FILE_SIZE * 1000 * 1000    # In bytes
                , max_backups=1    # TODO: DEFINE IT IN A VARIABLE.
            )
logger = logger_obj.setup_logger()


def custom_exception_handler(exc_type, exc_value, exc_traceback):
    print(f"Uncaught exception: {exc_type}, {exc_value}")

    logger.debug("Uncaught exception::: ", exc_info=(exc_type, exc_value, exc_traceback))


# Set the custom exception handler globally.
sys.excepthook = custom_exception_handler





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
