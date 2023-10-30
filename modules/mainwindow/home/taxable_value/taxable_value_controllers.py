import re
from decimal import Decimal, DecimalException

from modules.mainwindow.home.taxable_value.taxable_value_views import TaxableValueView

class TaxableValueController(TaxableValueView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupSignals()

    def setupSignals(self):
        self.lineEdit_Total_Amount.textChanged.connect(self.validateInputAndShowResult)
        self.lineEdit_GST_Percent.textChanged.connect(self.validateInputAndShowResult)

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
        gst_percent = float(self.lineEdit_GST_Percent.text() or '0.0')

        # result = gst_percent / 100 * total_amount + total_amount    # Copilot Generated
        result = (100 * float(total_amount)) / (100 + float(gst_percent))
        self.label_Result_Value.setText(f'₹ {result:.10f}')

    # def validatePositiveInteger(self, text):
    #     if not text.isdigit() or int(text) < 0:
    #         cursor = self.sender().cursorPosition()
    #         self.sender().setText(text[:-1])
    #         self.sender().setCursorPosition(cursor - 1)

