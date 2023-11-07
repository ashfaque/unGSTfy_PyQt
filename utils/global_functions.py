import os
import sys

import requests
from PyQt6 import QtWidgets, QtCore


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


# ? Get the writable location for application data, platform independent.
def get_app_data_dir():
    if is_frozen_executable():
        return QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppDataLocation)
    else:    # If development environment.
        return os.getcwd() + "/_temp"    # TODO: Global variable defined in config/constants.py

