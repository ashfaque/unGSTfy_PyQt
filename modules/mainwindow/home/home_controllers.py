from modules.mainwindow.home.home_views import HomeView
from modules.mainwindow.home.taxable_value.taxable_value_controllers import TaxableValueController
from modules.mainwindow.home.gst_percent.gst_percent_controllers import GSTPercentController
from modules.mainwindow.home.currency_converter.currency_converter_controllers import CurrencyConverterController

class HomeController(HomeView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupSignals()
        self.setupViews()

    def setupSignals(self):
        self.pushButton_Calculate_Taxable_Value.clicked.connect(self.onPushButtonCalculateTaxableValueClicked)
        self.pushButton_Calculate_GST_Percent.clicked.connect(self.onPushButtonCalculateGSTPercentClicked)
        self.pushButton_Currency_Converter.clicked.connect(self.onPushButtonCurrencyConverterClicked)
    
    def setupViews(self):
        self.taxableValueView = TaxableValueController(parent=self)
        self.stackedcentralwidget.addWidget(self.taxableValueView)

        self.gstPercentView = GSTPercentController(parent=self)
        self.stackedcentralwidget.addWidget(self.gstPercentView)

        self.currencyConverterView = CurrencyConverterController(parent=self)
        self.stackedcentralwidget.addWidget(self.currencyConverterView)


    def onPushButtonCalculateTaxableValueClicked(self):
        self.stackedcentralwidget.setCurrentWidget(self.taxableValueView)

    def onPushButtonCalculateGSTPercentClicked(self):
        self.stackedcentralwidget.setCurrentWidget(self.gstPercentView)
        
    def onPushButtonCurrencyConverterClicked(self):
        self.stackedcentralwidget.setCurrentWidget(self.currencyConverterView)
