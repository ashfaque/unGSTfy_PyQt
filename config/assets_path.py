# Images path mapped with a variable here. So only needs to change at one place if path changes.

from PyQt6 import QtGui

from utils.global_functions import assets_base_path_according_to_dev_or_exec

APP_LOGO_PATH = assets_base_path_according_to_dev_or_exec('assets/images/gst_logo.png')

FONTS = {
    'TF2_BUILD_PATH': assets_base_path_according_to_dev_or_exec('assets/fonts/TF2Build.ttf')
    , 'TF2_SECONDARY_PATH': assets_base_path_according_to_dev_or_exec('assets/fonts/TF2Secondary.ttf')
}



def initialize_assets():
    for each_font_key, each_font_value in FONTS.items():
        QtGui.QFontDwatabase.addApplicationFont(each_font_value)
