
import os

from PyQt6 import QtCore

from config.ui_element_names import APP_NAME
from utils.global_functions import is_frozen_executable

class SettingsManager:
    def __init__(self):
        self.app_name = APP_NAME
        # self.settings_dir = os.path.join(os.getenv("APPDATA"), app_name)

        # ? Get the writable location for application data, platform independent.
        if is_frozen_executable():
            self.settings_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppDataLocation)
        else:    # If development environment.
            self.settings_dir = os.getcwd() + "/_temp"    # TODO: Global variable defined in config/constants.py

        # ? Create the directory if it doesn't exist.
        if not os.path.exists(self.settings_dir):
            os.makedirs(self.settings_dir)

        # ? Define the settings file path.
        self.settings_file_path = f"{self.settings_dir}/unGSTfy_data.ini"    # TODO: Global variable defined in config/constants.py

        # Initialize QSettings with the custom location
        self.settings = QtCore.QSettings(self.settings_file_path, QtCore.QSettings.Format.IniFormat)


    def save_data_in_settings(self, key:str , value):    # ? 'key' is a string, 'value' is of any Python3 data type.
        self.settings.setValue(key, value)
        # with open(os.path.join(self.settings_dir, "settings.json"), "w") as json_file:    # open in 'a' mode to append.
        #     json.dump(data, json_file)


    def load_data_from_settings(self, key: str):
        return self.settings.value(key, defaultValue=None)
        # settings_file = os.path.join(self.settings_dir, "settings.json")
        # if os.path.exists(settings_file):
        #     with open(settings_file, "r") as json_file:
        #         return json.load(json_file)
        # return {}


    def remove_data_from_settings(self, key: str):
        self.settings.remove(key)


### * Usage:-
# from config.settings import SettingsManager
# settings_manager = SettingsManager()
# settings_manager.save_data_in_settings('key1', 'value1')
# loaded_settings = settings_manager.load_data_from_settings()
# print('loaded_settings---> ', loaded_settings)





'''
import os
import json

from PyQt6 import QtCore

from config.ui_element_names import APP_NAME
from utils.global_functions import is_frozen_executable

class SettingsManager:
    def __init__(self):
        self.app_name = APP_NAME
        # self.settings_dir = os.path.join(os.getenv("APPDATA"), app_name)
        if is_frozen_executable():
            self.settings_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppDataLocation)
        else:
            self.settings_dir = os.getcwd() + "/_temp"

    def save_settings(self, data):
        if not os.path.exists(self.settings_dir):
            os.makedirs(self.settings_dir)

        with open(os.path.join(self.settings_dir, "settings.json"), "w") as json_file:    # open in 'a' mode to append.
            json.dump(data, json_file)

    def load_settings(self):
        settings_file = os.path.join(self.settings_dir, "settings.json")
        if os.path.exists(settings_file):
            with open(settings_file, "r") as json_file:
                return json.load(json_file)
        return {}

if __name__ == "__main__":
    settings_manager = SettingsManager()

    # Save settings
    settings_manager.save_settings({"key1": "value1", "key2": "value2"})

    # Load settings
    loaded_settings = settings_manager.load_settings()
    # print(loaded_settings)
'''

