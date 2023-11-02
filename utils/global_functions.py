import os
import sys

def is_frozen_executable():
    return getattr(sys, 'frozen', False)


def assets_base_path_according_to_dev_or_exec(assets_path: str):
    if getattr(sys, 'frozen', False):
        final_assets_path = os.path.join(sys._MEIPASS, assets_path)
    else:
        final_assets_path = assets_path
    return final_assets_path
