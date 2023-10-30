from decimal import Decimal, DecimalException

from modules.mainwindow.home.gst_percent.gst_percent_views import GSTPercentView

class GSTPercentController(GSTPercentView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupSignals()

    def setupSignals(self):
        self.lineEdit_Total_Amount.textChanged.connect(self.validateInputAndShowResult)
        self.lineEdit_Taxable_Value.textChanged.connect(self.validateInputAndShowResult)

    def validateInputAndShowResult(self, text):
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
        
        # Result Calculation
        total_amount = float(self.lineEdit_Total_Amount.text() or '0.0')
        taxable_value = float(self.lineEdit_Taxable_Value.text() or '0.0')

        result = ((float(total_amount) / float(taxable_value)) - 1) * 100 if float(total_amount) != 0.0 and float(taxable_value) != 0.0 else 0.0
        self.label_Result_Value.setText(f'{result:.1f} %')
