from PyQt6 import QtCore, QtGui, QtWidgets

from config.ui_element_names import (
    HOME_CALCULATE_TAXABLE_VALUE_BUTTON_NAME
    , HOME_CALCULATE_GST_PERCENT_BUTTON_NAME
    , HOME_CURRENCY_CONVERTER_BUTTON_NAME
    , HOME_BUTTONS_FONT_FAMILY
)


class HomeView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Home")
        # self.resize(500, 317)    # Not needed as the parent widget will handle the size.
        self.verticalLayout_home = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_home.setObjectName("verticalLayout_home")

        # horizontal_Layout_Calculate_Taxable_Value
        self.horizontal_Layout_Calculate_Taxable_Value = QtWidgets.QHBoxLayout()
        self.horizontal_Layout_Calculate_Taxable_Value.setObjectName("horizontal_Layout_Calculate_Taxable_Value")
        self.pushButton_Calculate_Taxable_Value = QtWidgets.QPushButton(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Calculate_Taxable_Value.sizePolicy().hasHeightForWidth())
        self.pushButton_Calculate_Taxable_Value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(HOME_BUTTONS_FONT_FAMILY)    # TODO: Test with this font after making an executable on another system.
        font.setPointSize(20)    # TODO: Dynamic font size according to the main monitor size.
        self.pushButton_Calculate_Taxable_Value.setFont(font)
        self.pushButton_Calculate_Taxable_Value.setObjectName("pushButton_Calculate_Taxable_Value")
        self.horizontal_Layout_Calculate_Taxable_Value.addWidget(self.pushButton_Calculate_Taxable_Value)
        self.verticalLayout_home.addLayout(self.horizontal_Layout_Calculate_Taxable_Value)

        # Spacer 1
        self.horizontalLayout_Spacer1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Spacer1.setObjectName("horizontalLayout_Spacer1")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)    # TODO: Dynamic 
        self.horizontalLayout_Spacer1.addItem(spacerItem)
        self.verticalLayout_home.addLayout(self.horizontalLayout_Spacer1)

        # horizontal_Layout_Calculate_GST_Percent
        self.horizontal_Layout_Calculate_GST_Percent = QtWidgets.QHBoxLayout()
        self.horizontal_Layout_Calculate_GST_Percent.setObjectName("horizontal_Layout_Calculate_GST_Percent")
        self.pushButton_Calculate_GST_Percent = QtWidgets.QPushButton(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Calculate_GST_Percent.sizePolicy().hasHeightForWidth())
        self.pushButton_Calculate_GST_Percent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(HOME_BUTTONS_FONT_FAMILY)    # TODO: Test with this font after making an executable on another system.
        font.setPointSize(20)    # TODO: Dynamic font size according to the main monitor size.
        self.pushButton_Calculate_GST_Percent.setFont(font)
        self.pushButton_Calculate_GST_Percent.setObjectName("pushButton_Calculate_GST_Percent")
        self.horizontal_Layout_Calculate_GST_Percent.addWidget(self.pushButton_Calculate_GST_Percent)
        self.verticalLayout_home.addLayout(self.horizontal_Layout_Calculate_GST_Percent)

        # Spacer 2
        self.horizontalLayout_Spacer2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Spacer2.setObjectName("horizontalLayout_Spacer2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)    # TODO: Dynamic 
        self.horizontalLayout_Spacer2.addItem(spacerItem1)
        self.verticalLayout_home.addLayout(self.horizontalLayout_Spacer2)

        # horizontal_Layout_Currency_Converter
        self.horizontal_Layout_Currency_Converter = QtWidgets.QHBoxLayout()
        self.horizontal_Layout_Currency_Converter.setObjectName("horizontal_Layout_Currency_Converter")
        self.pushButton_Currency_Converter = QtWidgets.QPushButton(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Currency_Converter.sizePolicy().hasHeightForWidth())
        self.pushButton_Currency_Converter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(HOME_BUTTONS_FONT_FAMILY)    # TODO: Test with this font after making an executable on another system.
        font.setPointSize(20)    # TODO: Dynamic font size according to the main monitor size.
        self.pushButton_Currency_Converter.setFont(font)
        self.pushButton_Currency_Converter.setObjectName("pushButton_Currency_Converter")
        self.horizontal_Layout_Currency_Converter.addWidget(self.pushButton_Currency_Converter)
        self.verticalLayout_home.addLayout(self.horizontal_Layout_Currency_Converter)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Calculate_Taxable_Value.setText(_translate("Form", HOME_CALCULATE_TAXABLE_VALUE_BUTTON_NAME))
        self.pushButton_Calculate_GST_Percent.setText(_translate("Form", HOME_CALCULATE_GST_PERCENT_BUTTON_NAME))
        self.pushButton_Currency_Converter.setText(_translate("Form", HOME_CURRENCY_CONVERTER_BUTTON_NAME))

