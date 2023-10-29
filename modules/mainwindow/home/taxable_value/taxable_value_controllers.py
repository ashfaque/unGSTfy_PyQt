from modules.mainwindow.home.taxable_value.taxable_value_views import TaxableValueView

class TaxableValueController(TaxableValueView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setupSignals()

# TODO: Add the logic here. Also setup input validation of only possitive integers. And setup realtime calculation of the result.
