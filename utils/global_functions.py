import sys
import requests


def is_frozen_executable():
    return getattr(sys, 'frozen', False)


def api_request(url: str, method: str, params: dict):
    response = requests.request(method, url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None    # TODO: Show error message to user. Where this function is called, handle the error.
