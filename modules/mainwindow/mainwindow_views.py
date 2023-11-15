# Only define GUIs in this file, and move the logic to the controllers.

from PyQt6 import QtCore, QtGui, QtWidgets

from utils.global_functions import get_primary_screen_geometry, get_custom_geometry_wrt_primary_screen
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
from config.constants import PERCENT_OF_APPLICATION_CONSUMING_MAIN_SCREEN


class MainWindowView(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")

        main_screen_resolution = get_primary_screen_geometry()
        application_window_size = main_screen_resolution.size() * PERCENT_OF_APPLICATION_CONSUMING_MAIN_SCREEN    # ? Dynamic size according to the main monitor size.
        self.setGeometry(0, 0, application_window_size.width(), application_window_size.height())    # Set the window size
        self.move(
                # floor((main_screen_resolution.width() - self.width()) / 2)
                # , floor((main_screen_resolution.height() - self.height()) / 2)
                (main_screen_resolution.width() - self.width()) // 2
                , (main_screen_resolution.height() - self.height()) // 2
        )    # Center the window on the screen

        # self.resize(715, 453)

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





class CustomExitDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exit")
        self.setWindowFlag(QtCore.Qt.WindowType.WindowContextHelpButtonHint, False)    # Remove the "?" button

        # Customize dialog size (e.g., 20% of the screen)
        custom_geometry = get_custom_geometry_wrt_primary_screen(0.2)
        self.setFixedSize(custom_geometry.width(), custom_geometry.height())

        layout = QtWidgets.QHBoxLayout()  # Use a horizontal layout

        label = QtWidgets.QLabel()
        label.setText("Are you sure you want to exit?")
        font = QtGui.QFont("Arial", 16)
        label.setFont(font)
        layout.addWidget(label)

        # Add an icon on top
        icon_label = QtWidgets.QLabel()
        icon_pixmap = QtGui.QPixmap("icon.png")  # Replace with your icon image file
        icon_label.setPixmap(icon_pixmap)
        layout.addWidget(icon_label)

        button_yes = QtWidgets.QPushButton("Yes")
        button_no = QtWidgets.QPushButton("No")
        font = QtGui.QFont("Arial", 13)
        button_yes.setFont(font)
        button_no.setFont(font)

        # Customize button styles
        button_yes.setStyleSheet(
            """
            QPushButton {
                background-color: red;
                border: 2px solid darkred;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: darkred;
            }
            """
        )

        button_no.setStyleSheet(
            """
            QPushButton {
                background-color: gray;
                border: 2px solid blue;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
            """
        )

        layout.addWidget(button_no)  # Add "No" button first
        layout.addWidget(button_yes)  # Add "Yes" button

        # Connect buttons to slots for handling user actions (e.g., exiting)
        button_yes.clicked.connect(self.accept)
        button_no.clicked.connect(self.reject)

        # Set the layout for the dialog
        self.setLayout(layout)

