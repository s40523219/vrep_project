# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\vrep_project\vrep_test\vrep\VT_v01.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(625, 269)
        Dialog.setMinimumSize(QtCore.QSize(625, 269))
        Dialog.setMaximumSize(QtCore.QSize(625, 269))
        Dialog.setSizeGripEnabled(False)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_ItemName = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_ItemName.setFont(font)
        self.label_ItemName.setObjectName("label_ItemName")
        self.horizontalLayout_2.addWidget(self.label_ItemName)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setInputMask("")
        self.lineEdit.setMaxLength(16)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.print = QtWidgets.QPushButton(Dialog)
        self.print.setObjectName("print")
        self.horizontalLayout_2.addWidget(self.print)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3d = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3d.setFont(font)
        self.label_3d.setObjectName("label_3d")
        self.verticalLayout.addWidget(self.label_3d)
        self.form_3d = QtWidgets.QFormLayout()
        self.form_3d.setObjectName("form_3d")
        self.label_x = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.label_x.setFont(font)
        self.label_x.setObjectName("label_x")
        self.form_3d.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_x)
        self.value_x = QtWidgets.QDoubleSpinBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.value_x.setFont(font)
        self.value_x.setSuffix("")
        self.value_x.setDecimals(1)
        self.value_x.setMinimum(-1000.0)
        self.value_x.setMaximum(1000.0)
        self.value_x.setSingleStep(1.0)
        self.value_x.setObjectName("value_x")
        self.form_3d.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.value_x)
        self.label_y = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.label_y.setFont(font)
        self.label_y.setObjectName("label_y")
        self.form_3d.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_y)
        self.value_y = QtWidgets.QDoubleSpinBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.value_y.setFont(font)
        self.value_y.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.value_y.setMouseTracking(False)
        self.value_y.setTabletTracking(False)
        self.value_y.setAcceptDrops(False)
        self.value_y.setAutoFillBackground(False)
        self.value_y.setWrapping(False)
        self.value_y.setAccelerated(False)
        self.value_y.setProperty("showGroupSeparator", False)
        self.value_y.setPrefix("")
        self.value_y.setSuffix("")
        self.value_y.setDecimals(1)
        self.value_y.setMinimum(-1000.0)
        self.value_y.setMaximum(1000.0)
        self.value_y.setSingleStep(1.0)
        self.value_y.setObjectName("value_y")
        self.form_3d.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.value_y)
        self.label_z = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.label_z.setFont(font)
        self.label_z.setObjectName("label_z")
        self.form_3d.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_z)
        self.value_z = QtWidgets.QDoubleSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_z.sizePolicy().hasHeightForWidth())
        self.value_z.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.value_z.setFont(font)
        self.value_z.setPrefix("")
        self.value_z.setSuffix("")
        self.value_z.setDecimals(1)
        self.value_z.setMinimum(-1000.0)
        self.value_z.setMaximum(1000.0)
        self.value_z.setSingleStep(1.0)
        self.value_z.setProperty("value", 0.0)
        self.value_z.setObjectName("value_z")
        self.form_3d.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.value_z)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.form_3d.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.verticalLayout.addLayout(self.form_3d)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_button = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_button.setFont(font)
        self.label_button.setObjectName("label_button")
        self.horizontalLayout_3.addWidget(self.label_button)
        self.with_start = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.with_start.setFont(font)
        self.with_start.setObjectName("with_start")
        self.horizontalLayout_3.addWidget(self.with_start)
        self.with_open = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.with_open.setFont(font)
        self.with_open.setObjectName("with_open")
        self.horizontalLayout_3.addWidget(self.with_open)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_results_window = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_results_window.setFont(font)
        self.label_results_window.setObjectName("label_results_window")
        self.verticalLayout_2.addWidget(self.label_results_window)
        self.listWidget_results_window = QtWidgets.QListWidget(Dialog)
        self.listWidget_results_window.setObjectName("listWidget_results_window")
        self.verticalLayout_2.addWidget(self.listWidget_results_window)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_ItemName.setText(_translate("Dialog", "物件名稱 :"))
        self.lineEdit.setText(_translate("Dialog", "box"))
        self.print.setText(_translate("Dialog", "Print"))
        self.label_3d.setText(_translate("Dialog", "移動座標 :"))
        self.label_x.setText(_translate("Dialog", " X (mm)"))
        self.label_y.setText(_translate("Dialog", " Y (mm)"))
        self.label_z.setText(_translate("Dialog", " Z (mm)"))
        self.value_z.setToolTip(_translate("Dialog", "x"))
        self.label_button.setText(_translate("Dialog", " 點擊按鈕 :"))
        self.with_start.setText(_translate("Dialog", "Start"))
        self.with_open.setText(_translate("Dialog", "Open"))
        self.label_results_window.setText(_translate("Dialog", " 輸出結果 :"))

