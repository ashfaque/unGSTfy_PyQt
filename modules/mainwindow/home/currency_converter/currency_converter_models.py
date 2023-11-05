import datetime
import json

from config.settings import LocalDatabaseManager


class CurrencyConverterCurrenciesListModel(LocalDatabaseManager):
    # Define table name and columns as class attributes
    TABLE_NAME = "currency_converter_currencies_list_tbl"
    COLUMNS = {    # Column `id` generated and set to auto-incremented by default. No need to define it here.
        'name': ['TEXT', 'NULL']
        , 'code': ['TEXT', 'NULL', 'UNIQUE']
        , 'display_name': ['TEXT', 'NULL']
    }

    def __init__(self):
        # Initialize the parent class (LocalDatabaseManager)
        super().__init__(self.TABLE_NAME, self.COLUMNS)

    def serialize_response_data(self, data):
        if not data:
            return
        elif not (success := data["success"]):    # If success is False in response.
            return
        data = data["symbols"]
        data = list(data.items())
        # data = [dict(zip(["code", "name", "display_name"], [item[0], item[1], f"{item[0]} ({item[1]})"])) for item in data]
        # self.create(data)
        for item in data:
            self.create(dict(zip(["code", "name", "display_name"], [item[0], item[1], f"{item[0]} ({item[1]})"])))
        return data



class CurrencyConverterExchangeRatesModel(LocalDatabaseManager):
    # Define table name and columns as class attributes
    TABLE_NAME = "currency_converter_exchange_rates_tbl"
    COLUMNS = {    # Column `id` generated and set to auto-incremented by default. No need to define it here.
        # 'date': ['TEXT', 'NOT NULL', 'DEFAULT CURRENT_TIMESTAMP']
        # 'data_date': ['DATE', 'NULL', 'DEFAULT CURRENT_DATE']    # or, you can use: 'DEFAULT (date("now"))'
        'data_date': ['DATE', 'NULL']    # ? One data per day.
        , 'data_json': ['TEXT', 'NOT NULL', 'DEFAULT "{}"']
    }

    def __init__(self):
        # Initialize the parent class (LocalDatabaseManager)
        super().__init__(self.TABLE_NAME, self.COLUMNS)

    def serialize_response_data(self, data):
        if not data:
            return
        elif not (success := data["success"]):    # If success is False in response.
            return
        data_date = data["date"]
        data_json = json.dumps(data["rates"])
        self.create(data := {
            'data_date': data_date
            , 'data_json': data_json
        })
        return data
