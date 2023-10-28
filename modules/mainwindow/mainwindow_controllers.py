# Write the logic of the application here.

from PyQt6 import QtWidgets

from modules.mainwindow.mainwindow_views import MainWindowView
from modules.mainwindow.home.home_controllers import HomeController
from modules.mainwindow.about.about_controllers import AboutDialogController


class MainWindowController(MainWindowView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.show()
        self.setupSignals()
        self.setupViews()

    def setupSignals(self):
        self.actionHome.triggered.connect(self.onActionHomeTriggered)
        self.actionExit.triggered.connect(self.onActionExitTriggered)
        self.actionAbout.triggered.connect(self.onActionAboutTriggered)

    def setupViews(self):
        # self.homeView = HomeController(parent=self)    # TODO: Do it after setting up stacked widget in views.py
        # self.stackedcentralwidget.addWidget(self.homeView)    # TODO: Do it after setting up stacked widget in views.py
        
        self.aboutView = AboutDialogController(parent=self)


    def onActionHomeTriggered(self):
        # self.stackedcentralwidget.setCurrentWidget(self.homeView)    # TODO: AttributeError: 'MainWindowController' object has no attribute 'stackedWidget'. Do it after setting up stacked widget in views.py
        pass

    def onActionExitTriggered(self):
        self.close()

    def onActionAboutTriggered(self):    # TODO: Create a about module parallel to home dir in mainwindow, register it in __init__.py of modules. Also register it in setupViews() method of this file.
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