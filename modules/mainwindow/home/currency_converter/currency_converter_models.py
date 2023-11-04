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



class CurrencyConverterExchangeRatesModel(LocalDatabaseManager):
    # Define table name and columns as class attributes
    TABLE_NAME = "currency_converter_exchange_rates_tbl"
    COLUMNS = {    # Column `id` generated and set to auto-incremented by default. No need to define it here.
        # 'date': ['TEXT', 'NOT NULL', 'DEFAULT CURRENT_TIMESTAMP']
        # 'data_date': ['DATE', 'NULL', 'DEFAULT CURRENT_DATE']    # or, you can use: 'DEFAULT (date("now"))'
        'data_date': ['DATE', 'NULL']
        , 'data_json': ['TEXT', 'NOT NULL', 'DEFAULT "{}"']
    }

    def __init__(self):
        # Initialize the parent class (LocalDatabaseManager)
        super().__init__(self.TABLE_NAME, self.COLUMNS)
