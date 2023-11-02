# Write the logic of the application here.

from PyQt6 import QtWidgets

from modules.mainwindow.mainwindow_views import MainWindowView
from modules.mainwindow.home.home_controllers import HomeController
from modules.mainwindow.about.about_controllers import AboutDialogController
from config.assets_path import initialize_assets

class MainWindowController(MainWindowView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.show()
        self.setupSignals()
        self.initializeAssets()
        self.setupViews()

    def setupSignals(self):
        self.actionHome.triggered.connect(self.onActionHomeTriggered)
        self.actionExit.triggered.connect(self.onActionExitTriggered)
        self.actionAbout.triggered.connect(self.onActionAboutTriggered)

    def initializeAssets(self):
        _ = initialize_assets()

    def setupViews(self):
        self.homeView = HomeController(parent=self)    # Pass a reference to self (MainWindowController)
        self.stackedcentralwidget.addWidget(self.homeView)
        self.stackedcentralwidget.setCurrentWidget(self.homeView)

        self.aboutView = AboutDialogController(parent=self)


    def onActionHomeTriggered(self):
        # print('Home Stack Widgets Count---> ', self.homeView.stackedWidget.count())
        # for i in range(self.homeView.stackedWidget.count()):
        #     print('Home Stack Widgets Names---> ', (self.homeView.stackedWidget.widget(i).objectName()))
        # self.homeView.stackedWidget.setCurrentIndex(0)
        self.homeView.stackedWidget.setCurrentWidget(self.homeView.buttonPage)
        self.homeView.backButton.setVisible(False)

    def onActionExitTriggered(self):
        self.close()

    def onActionAboutTriggered(self):
        self.aboutView.exec()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
                                        self,
                                        "Exit",
                                        "Are you sure you want to exit?",
                                        QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                                        QtWidgets.QMessageBox.StandardButton.No,
                                    )
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
