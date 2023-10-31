from PyQt6 import QtCore, QtGui, QtWidgets

from config.ui_element_names import (
    CURRENCY_CONVERT_FROM_PLACEHOLDER_TEXT
    , CURRENCY_CONVERT_TO_PLACEHOLDER_TEXT
    , CURRENCY_CONVERT_REMAINING_MONTHLY_CONVERSIONS_TEXT
)


class CurrencyConverterView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Currency_Converter")

        # Page vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")


        # Top Spacer
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        # Convert from and to grouping
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Convert From
        self.verticalLayout_Currency_From = QtWidgets.QVBoxLayout()
        self.verticalLayout_Currency_From.setObjectName("verticalLayout_Currency_From")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_Currency_From.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_Currency_From.addItem(spacerItem2)
        self.lineEdit_Currency_From = QtWidgets.QLineEdit(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Currency_From.sizePolicy().hasHeightForWidth())
        self.lineEdit_Currency_From.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("TF2 Secondary")
        font.setPointSize(20)
        self.lineEdit_Currency_From.setFont(font)
        self.lineEdit_Currency_From.setObjectName("lineEdit_Currency_From")
        self.verticalLayout_Currency_From.addWidget(self.lineEdit_Currency_From)
        self.comboBox_Currency_From = QtWidgets.QComboBox(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Currency_From.sizePolicy().hasHeightForWidth())
        self.comboBox_Currency_From.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("TF2 Build")
        font.setPointSize(16)
        self.comboBox_Currency_From.setFont(font)
        self.comboBox_Currency_From.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox_Currency_From.setObjectName("comboBox_Currency_From")
        # self.comboBox_Currency_From.addItem("")
        # self.comboBox_Currency_From.addItem("")
        # self.comboBox_Currency_From.addItem("")
        self.verticalLayout_Currency_From.addWidget(self.comboBox_Currency_From)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_Currency_From.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_Currency_From.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_Currency_From)

        # Convert To
        self.verticalLayout_Currency_To = QtWidgets.QVBoxLayout()
        self.verticalLayout_Currency_To.setObjectName("verticalLayout_Currency_To")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_Currency_To.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_Currency_To.addItem(spacerItem6)
        self.lineEdit_Currency_To = QtWidgets.QLineEdit(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Currency_To.sizePolicy().hasHeightForWidth())
        self.lineEdit_Currency_To.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("TF2 Secondary")
        font.setPointSize(20)
        self.lineEdit_Currency_To.setFont(font)
        self.lineEdit_Currency_To.setObjectName("lineEdit_Currency_To")
        self.verticalLayout_Currency_To.addWidget(self.lineEdit_Currency_To)
        self.comboBox_Currency_To = QtWidgets.QComboBox(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Currency_To.sizePolicy().hasHeightForWidth())
        self.comboBox_Currency_To.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("TF2 Build")
        font.setPointSize(16)
        self.comboBox_Currency_To.setFont(font)
        self.comboBox_Currency_To.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox_Currency_To.setObjectName("comboBox_Currency_To")
        # self.comboBox_Currency_To.addItem("")
        # self.comboBox_Currency_To.addItem("")
        # self.comboBox_Currency_To.addItem("")
        self.verticalLayout_Currency_To.addWidget(self.comboBox_Currency_To)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_Currency_To.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_Currency_To.addItem(spacerItem8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_Currency_To)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Remaining Monthly Conversions
        self.label_Remaining_Monthly_Conversions_Text = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Remaining_Monthly_Conversions_Text.sizePolicy().hasHeightForWidth())
        self.label_Remaining_Monthly_Conversions_Text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("TF2 Secondary")
        font.setPointSize(14)
        self.label_Remaining_Monthly_Conversions_Text.setFont(font)
        self.label_Remaining_Monthly_Conversions_Text.setObjectName("label_Remaining_Monthly_Conversions_Text")
        self.horizontalLayout.addWidget(self.label_Remaining_Monthly_Conversions_Text)

        self.label_Remaining_Monthly_Conversions_Value = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Remaining_Monthly_Conversions_Value.sizePolicy().hasHeightForWidth())
        self.label_Remaining_Monthly_Conversions_Value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("TF2 Build")
        font.setPointSize(16)
        self.label_Remaining_Monthly_Conversions_Value.setFont(font)
        self.label_Remaining_Monthly_Conversions_Value.setObjectName("label_Remaining_Monthly_Conversions_Value")
        self.horizontalLayout.addWidget(self.label_Remaining_Monthly_Conversions_Value)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.comboBox_Currency_From.setToolTip(_translate("Form", CURRENCY_CONVERT_FROM_PLACEHOLDER_TEXT))
        self.comboBox_Currency_From.setPlaceholderText(_translate("Form", CURRENCY_CONVERT_FROM_PLACEHOLDER_TEXT))
        # self.comboBox_Currency_From.setItemText(0, _translate("Form", "USD"))
        # self.comboBox_Currency_From.setItemText(1, _translate("Form", "PND"))
        # self.comboBox_Currency_From.setItemText(2, _translate("Form", "INR"))
        self.comboBox_Currency_To.setToolTip(_translate("Form", CURRENCY_CONVERT_TO_PLACEHOLDER_TEXT))
        self.comboBox_Currency_To.setPlaceholderText(_translate("Form", CURRENCY_CONVERT_TO_PLACEHOLDER_TEXT))
        # self.comboBox_Currency_To.setItemText(0, _translate("Form", "INR"))
        # self.comboBox_Currency_To.setItemText(1, _translate("Form", "PKR"))
        # self.comboBox_Currency_To.setItemText(2, _translate("Form", "RUB"))
        self.label_Remaining_Monthly_Conversions_Text.setText(_translate("Form", CURRENCY_CONVERT_REMAINING_MONTHLY_CONVERSIONS_TEXT))
        self.label_Remaining_Monthly_Conversions_Value.setText(_translate("Form", ""))
