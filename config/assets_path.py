# Assets path mapped with a variable here. So only needs to change at one place if path changes.

import os
import sys

from PyQt6 import QtGui


def assets_base_path_according_to_dev_or_exec(assets_path: str):
    if getattr(sys, 'frozen', False):
        final_assets_path = os.path.join(sys._MEIPASS, assets_path)
    else:
        final_assets_path = assets_path
    return final_assets_path



# ******************** Assets Path Declarations ******************** #


APP_LOGO_PATH = assets_base_path_according_to_dev_or_exec('assets/images/gst_logo.png')

FONTS = {
    'TF2 Build': assets_base_path_according_to_dev_or_exec('assets/fonts/TF2Build.ttf')
    , 'TF2 Secondary': assets_base_path_according_to_dev_or_exec('assets/fonts/TF2Secondary.ttf')
}






# ******************** Initialize Assets ******************** #

def initialize_assets():
    for each_font_key, each_font_value in FONTS.items():
        QtGui.QFontDatabase.addApplicationFont(each_font_value)
