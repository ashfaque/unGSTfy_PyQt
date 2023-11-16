from PyQt6 import QtCore, QtGui, QtWidgets

from config.ui_element_names import (
    GST_PERCENT_LINEEDIT_FONT_FAMILY
    , GST_PERCENT_LABEL_FONT_FAMILY
    , GST_PERCENT_TOTAL_AMOUNT_PLACEHOLDER_TEXT
    , GST_PERCENT_TAXABLE_VALUE_PLACEHOLDER_TEXT
    , GST_PERCENT_RESULT_TOOLTIP_TEXT
)


class GSTPercentView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("GST_Percent")
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
        font.setFamily(GST_PERCENT_LINEEDIT_FONT_FAMILY)
        font.setPointSize(16)    # FONT SIZE
        self.lineEdit_Total_Amount.setFont(font)
        self.lineEdit_Total_Amount.setObjectName("lineEdit_Total_Amount")
        self.horizontalLayout_Total_Amount.addWidget(self.lineEdit_Total_Amount)
        self.verticalLayout.addLayout(self.horizontalLayout_Total_Amount)

        # Taxable Value
        self.horizontalLayout_Taxable_Value = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Taxable_Value.setObjectName("horizontalLayout_Taxable_Value")
        self.lineEdit_Taxable_Value = QtWidgets.QLineEdit(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Taxable_Value.sizePolicy().hasHeightForWidth())
        self.lineEdit_Taxable_Value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(GST_PERCENT_LINEEDIT_FONT_FAMILY)
        font.setPointSize(16)    # FONT SIZE
        self.lineEdit_Taxable_Value.setFont(font)
        self.lineEdit_Taxable_Value.setObjectName("lineEdit_Taxable_Value")
        self.horizontalLayout_Taxable_Value.addWidget(self.lineEdit_Taxable_Value)
        self.verticalLayout.addLayout(self.horizontalLayout_Taxable_Value)

        # Result: GST Percent
        self.horizontalLayout_Result_Value = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Result_Value.setObjectName("horizontalLayout_Result_Value")
        self.label_Result_Value = QtWidgets.QLabel(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Result_Value.sizePolicy().hasHeightForWidth())
        self.label_Result_Value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(GST_PERCENT_LABEL_FONT_FAMILY)
        font.setPointSize(20)    # FONT SIZE
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
        self.lineEdit_Total_Amount.setToolTip(_translate("Form", GST_PERCENT_TOTAL_AMOUNT_PLACEHOLDER_TEXT))
        self.lineEdit_Total_Amount.setPlaceholderText(_translate("Form", GST_PERCENT_TOTAL_AMOUNT_PLACEHOLDER_TEXT))
        self.lineEdit_Taxable_Value.setToolTip(_translate("Form", GST_PERCENT_TAXABLE_VALUE_PLACEHOLDER_TEXT))
        self.lineEdit_Taxable_Value.setPlaceholderText(_translate("Form", GST_PERCENT_TAXABLE_VALUE_PLACEHOLDER_TEXT))
        self.label_Result_Value.setToolTip(_translate("Form", GST_PERCENT_RESULT_TOOLTIP_TEXT))
        self.label_Result_Value.setText(_translate("Form", GST_PERCENT_RESULT_TOOLTIP_TEXT))

