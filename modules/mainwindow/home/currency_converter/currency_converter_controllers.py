from decimal import Decimal, DecimalException

from modules.mainwindow.home.currency_converter.currency_converter_views import CurrencyConverterView

class CurrencyConverterController(CurrencyConverterView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupSignals()

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
        sender = self.sender()    # Get the sender (the lineEdit that emitted the signal)
        
        if sender == self.lineEdit_Currency_From:
            # self.lineEdit_Currency_To.setText('123')
            ...
        elif sender == self.lineEdit_Currency_To:
            # self.lineEdit_Currency_From.setText('456')
            ...
