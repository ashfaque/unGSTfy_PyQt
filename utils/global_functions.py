import os
import sys
import requests

def is_frozen_executable():
    return getattr(sys, 'frozen', False)


def assets_base_path_according_to_dev_or_exec(assets_path: str):
    if getattr(sys, 'frozen', False):
        final_assets_path = os.path.join(sys._MEIPASS, assets_path)
    else:
        final_assets_path = assets_path
    return final_assets_path


def api_request(url: str, method: str, params: dict):
    response = requests.request(method, url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None    # TODO: Show error message to user. Where this function is called, handle the error.
