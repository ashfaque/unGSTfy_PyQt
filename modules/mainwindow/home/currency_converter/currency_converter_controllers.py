from modules.mainwindow.home.currency_converter.currency_converter_views import CurrencyConverterView

class CurrencyConverterController(CurrencyConverterView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setupSignals()

# TODO: make a function to validate the user input for decimal numbers for taxable, gst and currency convert. And user it.
