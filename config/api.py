BASE_URL = 'http://api.exchangeratesapi.io/'
ACCESS_KEY = '012432093fd9fd5a4f33393fee22c95b'    # TODO: Change API key later at somewhere outside this application.

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
