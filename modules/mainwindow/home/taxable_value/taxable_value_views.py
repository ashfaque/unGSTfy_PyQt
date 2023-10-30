from PyQt6 import QtCore, QtGui, QtWidgets

from config.ui_element_names import (
    TAXABLE_VALUE_LINEEDIT_FONT_FAMILY
    , TAXABLE_VALUE_LABEL_FONT_FAMILY
    , TAXABLE_VALUE_TOTAL_AMOUNT_PLACEHOLDER_TEXT
    , TAXABLE_VALUE_GST_PERCENT_PLACEHOLDER_TEXT
    , TAXABLE_VALUE_RESULT_TOOLTIP_TEXT
)


class TaxableValueView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Taxable_Value")
        # self.resize(594, 438)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        # Total Amount
        self.horizontalLayout_Total_Amount = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Total_Amount.setObjectName("horizontalLayout_Total_Amount")
        self.lineEdit_Total_Amount = QtWidgets.QLineEdit(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Total_Amount.sizePolicy().hasHeightForWidth())
        self.lineEdit_Total_Amount.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(TAXABLE_VALUE_LINEEDIT_FONT_FAMILY)
        font.setPointSize(16)    # TODO : Dynamic
        self.lineEdit_Total_Amount.setFont(font)
        self.lineEdit_Total_Amount.setObjectName("lineEdit_Total_Amount")
        self.horizontalLayout_Total_Amount.addWidget(self.lineEdit_Total_Amount)
        self.verticalLayout.addLayout(self.horizontalLayout_Total_Amount)

        # GST Percent
        self.horizontalLayout_GST_Percent = QtWidgets.QHBoxLayout()
        self.horizontalLayout_GST_Percent.setObjectName("horizontalLayout_GST_Percent")
        self.lineEdit_GST_Percent = QtWidgets.QLineEdit(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_GST_Percent.sizePolicy().hasHeightForWidth())
        self.lineEdit_GST_Percent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(TAXABLE_VALUE_LINEEDIT_FONT_FAMILY)
        font.setPointSize(16)    # TODO : Dynamic
        self.lineEdit_GST_Percent.setFont(font)
        self.lineEdit_GST_Percent.setObjectName("lineEdit_GST_Percent")
        self.horizontalLayout_GST_Percent.addWidget(self.lineEdit_GST_Percent)
        self.verticalLayout.addLayout(self.horizontalLayout_GST_Percent)

        # Result
        self.horizontalLayout_Result_Value = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Result_Value.setObjectName("horizontalLayout_Result_Value")
        self.label_Result_Value = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Result_Value.sizePolicy().hasHeightForWidth())
        self.label_Result_Value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(TAXABLE_VALUE_LABEL_FONT_FAMILY)
        font.setPointSize(20)    # TODO : Dynamic
        self.label_Result_Value.setFont(font)
        self.label_Result_Value.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.label_Result_Value.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.label_Result_Value.setWordWrap(True)
        self.label_Result_Value.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_Result_Value.setObjectName("label_Result_Value")
        self.horizontalLayout_Result_Value.addWidget(self.label_Result_Value)
        self.verticalLayout.addLayout(self.horizontalLayout_Result_Value)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_Total_Amount.setToolTip(_translate("Form", TAXABLE_VALUE_TOTAL_AMOUNT_PLACEHOLDER_TEXT))
        self.lineEdit_Total_Amount.setPlaceholderText(_translate("Form", TAXABLE_VALUE_TOTAL_AMOUNT_PLACEHOLDER_TEXT))
        self.lineEdit_GST_Percent.setToolTip(_translate("Form", TAXABLE_VALUE_GST_PERCENT_PLACEHOLDER_TEXT))
        self.lineEdit_GST_Percent.setPlaceholderText(_translate("Form", TAXABLE_VALUE_GST_PERCENT_PLACEHOLDER_TEXT))
        self.label_Result_Value.setToolTip(_translate("Form", TAXABLE_VALUE_RESULT_TOOLTIP_TEXT))
        self.label_Result_Value.setText(_translate("Form", "₹"))

