from PyQt6 import QtWidgets, QtCore, QtGui
from config.assets_path import APP_LOGO_PATH
from config.ui_element_names import (
    SYSTEM_TRAY_ICON_TOOLTIP_TEXT
    , SYSTEM_TRAY_ICON_SHOW_ACTION_NAME
    , SYSTEM_TRAY_ICON_EXIT_ACTION_NAME
)


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, main_win_controller_obj, parent=None):
        icon = QtGui.QIcon(APP_LOGO_PATH)
        super(__class__, self).__init__(icon, parent)
        self.setVisible(True)
        # self.activated.connect(main_window_controller_obj.showAndActivate)    # ? Show the main window when the system tray icon is clicked (both LMB & RMB).
        self.setToolTip(SYSTEM_TRAY_ICON_TOOLTIP_TEXT)
        self.main_win_obj = main_win_controller_obj  # <----- name it whatever you want ie self.abc will also work

        # Create a context menu for the system tray icon
        tray_context_menu = QtWidgets.QMenu()

        # Add actions to the context menu
        show_action = tray_context_menu.addAction(SYSTEM_TRAY_ICON_SHOW_ACTION_NAME)
        exit_action = tray_context_menu.addAction(SYSTEM_TRAY_ICON_EXIT_ACTION_NAME)

        # Connect the actions to their respective slots
        show_action.triggered.connect(self.main_win_obj.showAndActivate)    # ? Show the main window when `show_action` menu item is clicked.
        exit_action.triggered.connect(parent.quit)    # parent is the QApplication instance.

        # Set the context menu for the system tray icon.
        self.setContextMenu(tray_context_menu)

        # Show the system tray icon.
        self.show()





'''
def setup_system_tray_icon(app_obj, main_window_controller_obj):
    # Create a system tray icon
    system_tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon(APP_LOGO_PATH), parent=app_obj)
    system_tray_icon.setVisible(True)
    # system_tray_icon.activated.connect(main_window_controller_obj.showAndActivate)    # ? Show the main window when the system tray icon is clicked (both LMB & RMB).
    system_tray_icon.setToolTip(SYSTEM_TRAY_ICON_TOOLTIP_TEXT)

    # Create a context menu for the system tray icon
    tray_context_menu = QtWidgets.QMenu()

    # Add actions to the context menu
    show_action = tray_context_menu.addAction(SYSTEM_TRAY_ICON_SHOW_ACTION_NAME)
    exit_action = tray_context_menu.addAction(SYSTEM_TRAY_ICON_EXIT_ACTION_NAME)

    # Connect the actions to their respective slots
    show_action.triggered.connect(main_window_controller_obj.showAndActivate)    # ? Show the main window when `show_action` menu item is clicked.
    exit_action.triggered.connect(app_obj.quit)

    # Set the context menu for the system tray icon
    system_tray_icon.setContextMenu(tray_context_menu)

    # Show the system tray icon
    system_tray_icon.show()
'''

