# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Data\_PROGETTI\APPS\PRJ_MANAGER_2021\windows\pages\comp_page\comp_editor\comp_editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CompEditor(object):
    def setupUi(self, CompEditor):
        CompEditor.setObjectName("CompEditor")
        CompEditor.resize(300, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CompEditor.sizePolicy().hasHeightForWidth())
        CompEditor.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(CompEditor)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiGeneralInfoFrame = QtWidgets.QFrame(CompEditor)
        self.uiGeneralInfoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uiGeneralInfoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uiGeneralInfoFrame.setObjectName("uiGeneralInfoFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.uiGeneralInfoFrame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.uiTagDisplay = QtWidgets.QLineEdit(self.uiGeneralInfoFrame)
        self.uiTagDisplay.setReadOnly(True)
        self.uiTagDisplay.setObjectName("uiTagDisplay")
        self.gridLayout.addWidget(self.uiTagDisplay, 0, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.uiGeneralInfoFrame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.uiNameEdit = QtWidgets.QLineEdit(self.uiGeneralInfoFrame)
        self.uiNameEdit.setObjectName("uiNameEdit")
        self.gridLayout.addWidget(self.uiNameEdit, 1, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.uiGeneralInfoFrame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.uiDescEdit = QtWidgets.QPlainTextEdit(self.uiGeneralInfoFrame)
        self.uiDescEdit.setObjectName("uiDescEdit")
        self.gridLayout.addWidget(self.uiDescEdit, 3, 0, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.uiGeneralInfoFrame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.uiCommentEdit = QtWidgets.QPlainTextEdit(self.uiGeneralInfoFrame)
        self.uiCommentEdit.setObjectName("uiCommentEdit")
        self.gridLayout.addWidget(self.uiCommentEdit, 5, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.uiGeneralInfoFrame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.uiTypeDisplay = QtWidgets.QLineEdit(self.uiGeneralInfoFrame)
        self.uiTypeDisplay.setReadOnly(True)
        self.uiTypeDisplay.setObjectName("uiTypeDisplay")
        self.gridLayout.addWidget(self.uiTypeDisplay, 6, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.uiGeneralInfoFrame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.uiGeneralInfoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.uiNonEditableManufacture = QtWidgets.QWidget()
        self.uiNonEditableManufacture.setObjectName("uiNonEditableManufacture")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.uiNonEditableManufacture)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiManufactureDisplay = QtWidgets.QLineEdit(self.uiNonEditableManufacture)
        self.uiManufactureDisplay.setReadOnly(True)
        self.uiManufactureDisplay.setObjectName("uiManufactureDisplay")
        self.horizontalLayout_2.addWidget(self.uiManufactureDisplay)
        self.stackedWidget.addWidget(self.uiNonEditableManufacture)
        self.uiEditableManufacture = QtWidgets.QWidget()
        self.uiEditableManufacture.setObjectName("uiEditableManufacture")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.uiEditableManufacture)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiManufactureEdit = QtWidgets.QComboBox(self.uiEditableManufacture)
        self.uiManufactureEdit.setObjectName("uiManufactureEdit")
        self.horizontalLayout_3.addWidget(self.uiManufactureEdit)
        self.stackedWidget.addWidget(self.uiEditableManufacture)
        self.gridLayout.addWidget(self.stackedWidget, 7, 1, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.uiGeneralInfoFrame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.uiGeneralInfoFrame)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.uiNonEditableStatus = QtWidgets.QWidget()
        self.uiNonEditableStatus.setObjectName("uiNonEditableStatus")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.uiNonEditableStatus)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiStatusDisplay = QtWidgets.QLineEdit(self.uiNonEditableStatus)
        self.uiStatusDisplay.setReadOnly(True)
        self.uiStatusDisplay.setObjectName("uiStatusDisplay")
        self.horizontalLayout.addWidget(self.uiStatusDisplay)
        self.stackedWidget_2.addWidget(self.uiNonEditableStatus)
        self.uiEditableStatus = QtWidgets.QWidget()
        self.uiEditableStatus.setObjectName("uiEditableStatus")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.uiEditableStatus)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiStatusEdit = QtWidgets.QComboBox(self.uiEditableStatus)
        self.uiStatusEdit.setObjectName("uiStatusEdit")
        self.horizontalLayout_4.addWidget(self.uiStatusEdit)
        self.stackedWidget_2.addWidget(self.uiEditableStatus)
        self.gridLayout.addWidget(self.stackedWidget_2, 8, 1, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.uiGeneralInfoFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.uiQtyEdit = QtWidgets.QSpinBox(self.uiGeneralInfoFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiQtyEdit.sizePolicy().hasHeightForWidth())
        self.uiQtyEdit.setSizePolicy(sizePolicy)
        self.uiQtyEdit.setObjectName("uiQtyEdit")
        self.gridLayout.addWidget(self.uiQtyEdit, 9, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.uiGeneralInfoFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 2, 1, 1)
        self.uiCostEdit = QtWidgets.QLineEdit(self.uiGeneralInfoFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiCostEdit.sizePolicy().hasHeightForWidth())
        self.uiCostEdit.setSizePolicy(sizePolicy)
        self.uiCostEdit.setObjectName("uiCostEdit")
        self.gridLayout.addWidget(self.uiCostEdit, 9, 3, 1, 1)
        self.verticalLayout.addWidget(self.uiGeneralInfoFrame)
        self.uiPurchasableFrame = QtWidgets.QFrame(CompEditor)
        self.uiPurchasableFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uiPurchasableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uiPurchasableFrame.setObjectName("uiPurchasableFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiPurchasableFrame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.uiPurchasableFrame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.uiQtyPkgDisplay = QtWidgets.QLineEdit(self.uiPurchasableFrame)
        self.uiQtyPkgDisplay.setReadOnly(True)
        self.uiQtyPkgDisplay.setObjectName("uiQtyPkgDisplay")
        self.gridLayout_2.addWidget(self.uiQtyPkgDisplay, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.uiPurchasableFrame)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.uiSellerDisplay = QtWidgets.QLineEdit(self.uiPurchasableFrame)
        self.uiSellerDisplay.setReadOnly(True)
        self.uiSellerDisplay.setObjectName("uiSellerDisplay")
        self.gridLayout_2.addWidget(self.uiSellerDisplay, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.uiPurchasableFrame)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.uiLinkDisplay = QtWidgets.QPlainTextEdit(self.uiPurchasableFrame)
        self.uiLinkDisplay.setReadOnly(True)
        self.uiLinkDisplay.setObjectName("uiLinkDisplay")
        self.gridLayout_2.addWidget(self.uiLinkDisplay, 3, 0, 1, 2)
        self.verticalLayout.addWidget(self.uiPurchasableFrame)

        self.retranslateUi(CompEditor)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CompEditor)

    def retranslateUi(self, CompEditor):
        _translate = QtCore.QCoreApplication.translate
        CompEditor.setWindowTitle(_translate("CompEditor", "Form"))
        self.label.setText(_translate("CompEditor", "Name:"))
        self.label_2.setText(_translate("CompEditor", "Description:"))
        self.label_3.setText(_translate("CompEditor", "Comment:"))
        self.label_4.setText(_translate("CompEditor", "Type:"))
        self.label_6.setText(_translate("CompEditor", "Manufacture:"))
        self.label_5.setText(_translate("CompEditor", "Status:"))
        self.label_8.setText(_translate("CompEditor", "Quantity:"))
        self.label_7.setText(_translate("CompEditor", "Cost:"))
        self.label_9.setText(_translate("CompEditor", "Per Package:"))
        self.label_10.setText(_translate("CompEditor", "Seller:"))
        self.label_11.setText(_translate("CompEditor", "Link:"))
