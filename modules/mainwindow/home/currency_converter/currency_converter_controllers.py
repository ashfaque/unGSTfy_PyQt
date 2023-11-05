import datetime
from decimal import Decimal, DecimalException

from modules.mainwindow.home.currency_converter.currency_converter_views import CurrencyConverterView
from modules.mainwindow.home.currency_converter.currency_converter_models import CurrencyConverterCurrenciesListModel, CurrencyConverterExchangeRatesModel
from config.api import API_CURRENCIES_LIST, API_LATEST_EXCHANGE_RATES
from utils.global_functions import api_request
from config.ui_element_names import (
    CURRENCY_CONVERT_CURRENCY_LIST_NOT_AVAILABLE_TEXT
    , CURRENCY_CONVERT_EXCHANGE_RATE_NOT_AVAILABLE_TEXT
)
from pprint import pprint


class CurrencyConverterController(CurrencyConverterView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupData()
        self.setupSignals()

    def setupData(self):
        # ? Preparing currencies list for users to select from.
        currencies_list_of_dicts = CurrencyConverterCurrenciesListModel().get_all()
        if not currencies_list_of_dicts:
            api_response = api_request(API_CURRENCIES_LIST["url"], API_CURRENCIES_LIST["method"], API_CURRENCIES_LIST["params"])
            currencies_list_of_dicts = CurrencyConverterCurrenciesListModel().serialize_response_data(api_response)
            # if not api_response or not currencies_list_of_dicts:
            if not currencies_list_of_dicts:
                self.label_Remaining_Monthly_Conversions_Text.setText(CURRENCY_CONVERT_CURRENCY_LIST_NOT_AVAILABLE_TEXT)
                self.lineEdit_Currency_From.setDisabled(True)
                self.lineEdit_Currency_To.setDisabled(True)
                self.comboBox_Currency_From.setDisabled(True)
                self.comboBox_Currency_To.setDisabled(True)

        # ? Inserting currencies list in ComboBoxes for users to select from.
        if currencies_list_of_dicts:
            self.currency_display_name_to_code_dict = {item["display_name"]: item["code"] for item in currencies_list_of_dicts}    # ? Caching currency display name to code dict for calculation purpose later on.
            self.comboBox_Currency_From.addItems([item["display_name"] for item in currencies_list_of_dicts])
            self.comboBox_Currency_To.addItems([item["display_name"] for item in currencies_list_of_dicts])
            self.comboBox_Currency_From.setCurrentIndex(0)
            self.comboBox_Currency_To.setCurrentIndex(0)

        # ? ------------------------------------------------------------------------------------------------------ ? #

        # ? Preparing exchange rates for users to convert currencies.
        exchange_rates_list_of_dicts = CurrencyConverterExchangeRatesModel().get(where={'data_date': datetime.date.today()})    # datetime.datetime.now().date().isoformat()
        if not exchange_rates_list_of_dicts:
            api_response = api_request(API_LATEST_EXCHANGE_RATES["url"], API_LATEST_EXCHANGE_RATES["method"], API_LATEST_EXCHANGE_RATES["params"])
            serialized_data = CurrencyConverterExchangeRatesModel().serialize_response_data(api_response)
            if not serialized_data:
                self.label_Remaining_Monthly_Conversions_Text.setText(CURRENCY_CONVERT_EXCHANGE_RATE_NOT_AVAILABLE_TEXT)
                self.lineEdit_Currency_From.setDisabled(True)
                self.lineEdit_Currency_To.setDisabled(True)
                self.comboBox_Currency_From.setDisabled(True)
                self.comboBox_Currency_To.setDisabled(True)
            else:
                exchange_rates_list_of_dicts = [serialized_data]
        exchange_rates_list_of_dicts[0]['data_json'] = eval(exchange_rates_list_of_dicts[0]['data_json'])
        self.today_exchange_rates_dict = exchange_rates_list_of_dicts[0]['data_json']    # ? Caching today's exchange rates in a dict var for calculation purpose later on.

    def setupSignals(self):
        self.lineEdit_Currency_From.textChanged.connect(self.validateInput)
        self.lineEdit_Currency_To.textChanged.connect(self.validateInput)

        self.lineEdit_Currency_From.textChanged.connect(self.showResult)
        self.lineEdit_Currency_To.textChanged.connect(self.showResult)

    def validateInput(self, text):
        cursor_position = self.sender().cursorPosition()
        text = text.replace(" ", "")
        if text == "" or text == ".":
            self.sender().setText(text)
            self.sender().setCursorPosition(cursor_position)
            return
        try:
            value = Decimal(text)
            if value < 0:
                raise ValueError
            # self.sender().setText("{:.2f}".format(value))
            if "." in text:
                integer_part, decimal_part = text.split(".")
                if decimal_part == "":
                    self.sender().setText(integer_part + ".")
                else:
                    self.sender().setText("{:.{}f}".format(value, len(decimal_part)))
            else:
                self.sender().setText("{:.0f}".format(value))
            self.sender().setCursorPosition(cursor_position)
        except (ValueError, DecimalException) as ex:
            self.sender().setText(self.sender().text()[:-1])
            self.sender().setCursorPosition(cursor_position - 1)

    # TODO : see logic.md for more details.
    def showResult(self, text):
        # TODO: Also handle logic where user haven't changed `ComboBox Convert From / To` and enters value in `LineEdit From / To` field.
        sender = self.sender()    # Get the sender (the lineEdit that emitted the signal)

        # TODO: Use, self.currency_display_name_to_code_dict, to get the currency code from the currency display name.
        # TODO: self.today_exchange_rates_dict for cached today data.
        if sender == self.lineEdit_Currency_From:
            # self.lineEdit_Currency_To.setText('123')
            ...
        elif sender == self.lineEdit_Currency_To:
            # self.lineEdit_Currency_From.setText('456')
            ...
