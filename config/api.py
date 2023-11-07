import urllib.request as urllib_request

BASE_URL = 'http://api.exchangeratesapi.io/'
API_KEY_URL = 'https://pastebin.com/raw/euRCxULz'
ACCESS_KEY = urllib_request.urlopen(API_KEY_URL).read().decode('utf-8')

API_CURRENCIES_LIST = {
    'url': BASE_URL+'v1/symbols?'
    , 'method': 'GET'
    , 'params': {
        'access_key': ACCESS_KEY
    }
}

API_LATEST_EXCHANGE_RATES = {
    'url': BASE_URL+'v1/latest?'
    , 'method': 'GET'
    , 'params': {
        'base': 'EUR'
        , 'access_key': ACCESS_KEY
    }
}
