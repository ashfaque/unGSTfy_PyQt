# Write the logic of the application here.

from PyQt6 import QtWidgets

from modules.mainwindow.mainwindow_views import MainWindowView, CustomExitDialog
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
        if event.spontaneous():  # ? If event is NOT triggered by the system (like clicking the close button)
            self.hide()    # * Hide the GUI.
            event.ignore()    # Ignore the event.
        else:    # If triggered by the user (like clicking the `Exit` option in the menu bar of the application or system tray context menu).
            reply = QtWidgets.QMessageBox.question(
                                            self,
                                            "Exit",
                                            "Are you sure you want to exit?",
                                            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                                            QtWidgets.QMessageBox.StandardButton.No,
                                        )
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                event.accept()    # Accept the event. This will close the application.
            else:
                event.ignore()    # Ignore the event.

    '''
    # ? Used for closing the application when the user clicks on the close button of the window title bar.
    # ? Or, when the user presses Alt+F4, or when the user presses Alt+Space and then clicks on the Close option in the system menu.
    # ? Or, when the user presses the close button of the taskbar icon.
    # ? Or, when the user presses the close button of the taskbar thumbnail preview.
    # ? Or, when the user presses the close button of the system tray icon.
    # ? Or, when user presses the Exit option in the menu bar of the application.
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
    '''

    '''
    # To change the style of the exit dialog.
    def closeEvent(self, event):
        custom_dialog = CustomExitDialog()
        response = custom_dialog.exec()

        if response == QtWidgets.QDialog.DialogCode.Accepted:
            event.accept()
        else:
            event.ignore()
    '''

    def showAndActivate(self):    # ? Custom method: Called when the system tray icon is clicked.
        # Ensure the window is always visible when it is shown.
        self.showNormal()
        self.activateWindow()
        self.raise_()    # Bring the window to the front of all the other windows (even if it is minimized).
