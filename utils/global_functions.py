import os
import sys

import requests
from PyQt6 import QtWidgets


def is_frozen_executable():
    return getattr(sys, 'frozen', False)


def get_primary_screen_geometry():
    return QtWidgets.QApplication.primaryScreen().availableGeometry()


def api_request(url: str, method: str, params: dict):
    response = requests.request(method, url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None    # TODO: Show error message to user. Where this function is called, handle the error.


# Some utility functions defined here.
'''

from config.app_logging import get_app_data_dir
_ = get_app_data_dir()


from config.app_logging import trigger_manual_exception_and_log_it
trigger_manual_exception_and_log_it("This is a test exception message.")

'''
