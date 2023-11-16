from PyQt6 import QtWidgets, QtCore, QtGui

from utils.global_functions import get_custom_geometry_wrt_primary_screen
from config.ui_element_names import (
    MENU_BAR_HELP_ITEM_ABOUT
    , ABOUT_FONT_FAMILY
    , APP_NAME
    , APP_VERSION
    , APP_AUTHOR
    , APP_DESCRIPTION
    , CLOSE_BUTTON_NAME
)



class AboutDialogView(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle(MENU_BAR_HELP_ITEM_ABOUT)
        custom_about_geometry = get_custom_geometry_wrt_primary_screen(0.2)    # 20% of the main screen size.
        self.setFixedSize(custom_about_geometry.width(), custom_about_geometry.height())    # 400, 300
        self.setSizeGripEnabled(False)    # Allow resizing

        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)    # PIXELS: left, top, right, bottom

        # Add a vertical spacer at the top to push content down
        layout.addStretch(1)

        title_font = QtGui.QFont(ABOUT_FONT_FAMILY, 20, weight=QtGui.QFont.Weight.Bold)    # FONT SIZE
        label_font = QtGui.QFont(ABOUT_FONT_FAMILY, 13, weight=QtGui.QFont.Weight.Bold)    # FONT SIZE
        description_font = QtGui.QFont(ABOUT_FONT_FAMILY, 12)    # FONT SIZE

        app_name_label = QtWidgets.QLabel(APP_NAME)
        app_name_label.setFont(title_font)
        app_name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(app_name_label)

        version_label = QtWidgets.QLabel(f"Version {APP_VERSION}")
        version_label.setFont(description_font)
        version_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(version_label)

        author_label = QtWidgets.QLabel(f"Author: {APP_AUTHOR}")
        author_label.setFont(label_font)
        author_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(author_label)

        description_label = QtWidgets.QLabel(APP_DESCRIPTION)
        description_label.setFont(description_font)
        description_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        description_label.setWordWrap(True)
        layout.addWidget(description_label)

        # Add a vertical spacer in the middle to center the button
        layout.addStretch(1)

        self.close_button = QtWidgets.QPushButton(CLOSE_BUTTON_NAME)
        self.close_button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        # close_button.clicked.connect(self.close)
        # layout.addWidget(self.close_button, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        # Add the button with alignment to center it horizontally
        button_container = QtWidgets.QVBoxLayout()
        button_container.addWidget(self.close_button)
        button_container.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(button_container)

        self.setLayout(layout)

