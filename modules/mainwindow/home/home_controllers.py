from modules.mainwindow.home.home_views import HomeView
from modules.mainwindow.home.taxable_value.taxable_value_controllers import TaxableValueController
from modules.mainwindow.home.gst_percent.gst_percent_controllers import GSTPercentController
from modules.mainwindow.home.currency_converter.currency_converter_controllers import CurrencyConverterController

class HomeController(HomeView):
    def __init__(self, parent=None):    # ? You can take the main_window_controller as an argument and use it to connect the signals to the slots in the main_window_controller. This way you can avoid the use of the self.parent() method. Just assign self.main_window_controller = parent or main_window_controller in the __init__ method.
    # ? def __init__(self, main_window_controller, parent=None):
        # ? self.main_window_controller = main_window_controller  # Store a reference to the MainWindowController
        super().__init__(parent=parent)
        self.setupSignals()
        '''self.setupViews()'''    # * Disabled these lines as they are initializing all the views at once. Causing the app to slow down at startup.

    def setupSignals(self):
        self.pushButton_Calculate_Taxable_Value.clicked.connect(self.onPushButtonCalculateTaxableValueClicked)
        self.pushButton_Calculate_GST_Percent.clicked.connect(self.onPushButtonCalculateGSTPercentClicked)
        self.pushButton_Currency_Converter.clicked.connect(self.onPushButtonCurrencyConverterClicked)
        self.backButton.clicked.connect(self.backButtonClicked)
    
    '''    # * Disabled these lines as they are initializing all the views at once. Causing the app to slow down at startup.
    def setupViews(self):
        self.taxableValueView = TaxableValueController(parent=self)
        self.stackedWidget.addWidget(self.taxableValueView)

        self.gstPercentView = GSTPercentController(parent=self)
        self.stackedWidget.addWidget(self.gstPercentView)

        self.currencyConverterView = CurrencyConverterController(parent=self)
        self.stackedWidget.addWidget(self.currencyConverterView)
    '''
    # * NB: We are registering all the Controllers here at once. Therefore all their constructors `__init__()` are being called. Now all the controllers inherits their views class. Therefore, all the views are being initialized at once when the application loads. This is causing the app to slow down at startup. Therefore, we are disabling the above lines of code and initializing the views only when the user clicks on the respective buttons. This way, the views will be initialized only when the user clicks on the respective buttons. This will improve the startup time of the application.


    def onPushButtonCalculateTaxableValueClicked(self):
        self.taxableValueView = TaxableValueController(parent=self)    # * Registered individual Controllers to stackedWidget when user clicks on their specified buttons. Causing the page to load when needed. Not like it used to all at a time and cauing slower startup when applicaiton launches.
        self.stackedWidget.addWidget(self.taxableValueView)    # * Registered individual Controllers to stackedWidget when user clicks on their specified buttons. Causing the page to load when needed. Not like it used to all at a time and cauing slower startup when applicaiton launches.

        self.stackedWidget.setCurrentWidget(self.taxableValueView)
        self.backButton.setVisible(True)    # Show the "Back" button

    def onPushButtonCalculateGSTPercentClicked(self):
        self.gstPercentView = GSTPercentController(parent=self)    # * Registered individual Controllers to stackedWidget when user clicks on their specified buttons. Causing the page to load when needed. Not like it used to all at a time and cauing slower startup when applicaiton launches.
        self.stackedWidget.addWidget(self.gstPercentView)    # * Registered individual Controllers to stackedWidget when user clicks on their specified buttons. Causing the page to load when needed. Not like it used to all at a time and cauing slower startup when applicaiton launches.

        self.stackedWidget.setCurrentWidget(self.gstPercentView)
        self.backButton.setVisible(True)    # Show the "Back" button
        
    def onPushButtonCurrencyConverterClicked(self):
        self.currencyConverterView = CurrencyConverterController(parent=self)    # * Registered individual Controllers to stackedWidget when user clicks on their specified buttons. Causing the page to load when needed. Not like it used to all at a time and cauing slower startup when applicaiton launches.
        self.stackedWidget.addWidget(self.currencyConverterView)    # * Registered individual Controllers to stackedWidget when user clicks on their specified buttons. Causing the page to load when needed. Not like it used to all at a time and cauing slower startup when applicaiton launches.

        self.stackedWidget.setCurrentWidget(self.currencyConverterView)
        self.backButton.setVisible(True)    # Show the "Back" button

    def backButtonClicked(self):
        self.stackedWidget.setCurrentWidget(self.buttonPage)
        self.stackedWidget.setCurrentIndex(0)
        self.backButton.setVisible(False)    # Show/hide the "Back" button as needed

        '''
        current_index = self.stackedWidget.currentIndex()
        if current_index > 0:
            self.stackedWidget.setCurrentIndex(current_index - 1)
        self.backButton.setVisible(current_index > 1)    # Show/hide the "Back" button as needed
        '''

