# Only define GUIs in this file, and move the logic to the controllers.

from PyQt6 import QtCore, QtGui, QtWidgets

from config.ui_element_names import (
    APP_NAME
    , MENU_BAR_MENU_NAME
    , MENU_BAR_MENU_ITEM_HOME_NAME
    , MENU_BAR_MENU_ITEM_HOME_SHORTCUT
    , MENU_BAR_MENU_ITEM_EXIT_NAME
    , MENU_BAR_MENU_ITEM_EXIT_SHORTCUT
    , MENU_BAR_HELP_NAME
    , MENU_BAR_HELP_ITEM_ABOUT
)
from config.assets_path import APP_LOGO_PATH


class MainWindowView(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(715, 453)    # TODO: Dynamic size according to the main monitor size.

        # self.centralwidget = QtWidgets.QWidget(parent=self)
        self.stackedcentralwidget = QtWidgets.QStackedWidget(parent=self)
        self.stackedcentralwidget.setObjectName("stackedcentralwidget")
        self.setCentralWidget(self.stackedcentralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 22))    # TODO: Dynamic geometry size according to the main monitor size. Also font size of items.
        self.menubar.setObjectName("menubar")

        self.menuMenu = QtWidgets.QMenu(parent=self.menubar)
        self.menuMenu.setObjectName("menuMenu")

        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.setMenuBar(self.menubar)

        self.actionHome = QtGui.QAction(parent=self)
        self.actionHome.setObjectName("actionHome")

        self.actionExit = QtGui.QAction(parent=self)
        self.actionExit.setObjectName("actionExit")

        self.actionAbout = QtGui.QAction(parent=self)
        self.actionAbout.setObjectName("actionAbout")

        self.menuMenu.addAction(self.actionHome)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)

        self.menuHelp.addAction(self.actionAbout)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("MainWindow", APP_NAME))

        self.setWindowIcon(QtGui.QIcon(APP_LOGO_PATH))
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(APP_LOGO_PATH), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        # # icon.addPixmap(QtGui.QPixmap(APP_LOGO_PATH), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        # self.setWindowIcon(icon)

        self.menuMenu.setTitle(_translate("MainWindow", MENU_BAR_MENU_NAME))

        self.menuHelp.setTitle(_translate("MainWindow", MENU_BAR_HELP_NAME))

        self.actionHome.setText(_translate("MainWindow", MENU_BAR_MENU_ITEM_HOME_NAME))
        self.actionHome.setShortcut(_translate("MainWindow", MENU_BAR_MENU_ITEM_HOME_SHORTCUT))

        self.actionExit.setText(_translate("MainWindow", MENU_BAR_MENU_ITEM_EXIT_NAME))
        self.actionExit.setShortcut(_translate("MainWindow", MENU_BAR_MENU_ITEM_EXIT_SHORTCUT))

        self.actionAbout.setText(_translate("MainWindow", MENU_BAR_HELP_ITEM_ABOUT))
