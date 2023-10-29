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
        # self.pushButton_Calculate_GST_Percent.clicked.connect(self.onPushButtonCalculateGSTPercentClicked)    # TODO
        # self.pushButton_Currency_Converter.clicked.connect(self.onPushButtonCurrencyConverterClicked)    # TODO
        self.backButton.clicked.connect(self.backButtonClicked)
    
    def setupViews(self):
        self.taxableValueView = TaxableValueController(parent=self)
        self.stackedWidget.addWidget(self.taxableValueView)

        # self.gstPercentView = GSTPercentController(parent=self)    # TODO
        # self.stackedWidget.addWidget(self.gstPercentView)

        # self.currencyConverterView = CurrencyConverterController(parent=self)    # TODO
        # self.stackedWidget.addWidget(self.currencyConverterView)


    def onPushButtonCalculateTaxableValueClicked(self):
        self.stackedWidget.setCurrentWidget(self.taxableValueView)
        self.backButton.setVisible(True)    # Show the "Back" button

    def onPushButtonCalculateGSTPercentClicked(self):
        self.stackedWidget.setCurrentWidget(self.gstPercentView)
        
    def onPushButtonCurrencyConverterClicked(self):
        self.stackedWidget.setCurrentWidget(self.currencyConverterView)

    def backButtonClicked(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index > 0:
            self.stackedWidget.setCurrentIndex(current_index - 1)
        self.backButton.setVisible(current_index > 1)    # Show/hide the "Back" button as needed
