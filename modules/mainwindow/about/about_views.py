from PyQt6 import QtWidgets, QtCore

from config.ui_element_names import (
    MENU_BAR_HELP_ITEM_ABOUT
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
        self.setFixedSize(400, 300)    # Set an initial fixed size, can be adjusted    # TODO: Dynamic size according to the main monitor size.
        self.setSizeGripEnabled(True)    # Allow resizing

        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()

        # Add a vertical spacer at the top to push content down
        layout.addStretch(1)

        label = QtWidgets.QLabel(APP_NAME)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        version_label = QtWidgets.QLabel(f"Version {APP_VERSION}")
        version_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(version_label)

        author_label = QtWidgets.QLabel(f"Author: {APP_AUTHOR}")
        author_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(author_label)

        description_label = QtWidgets.QLabel(APP_DESCRIPTION)
        description_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(description_label)

        # Add a vertical spacer in the middle to center the button
        layout.addStretch(1)

        close_button = QtWidgets.QPushButton(CLOSE_BUTTON_NAME)
        close_button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        close_button.clicked.connect(self.close)

        # Add the button with alignment to center it horizontally
        button_container = QtWidgets.QVBoxLayout()
        button_container.addWidget(close_button)
        button_container.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(button_container)

        self.setLayout(layout)

