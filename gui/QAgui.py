# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QAgui.ui'
#
# Created: Mon Jul 31 13:36:35 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(713, 513)
        self.qButton = QtGui.QPushButton(Dialog)
        self.qButton.setGeometry(QtCore.QRect(630, 460, 71, 41))
        self.qButton.setObjectName(_fromUtf8("qButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.moduleName = QtGui.QComboBox(Dialog)
        self.moduleName.setGeometry(QtCore.QRect(210, 20, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.moduleName.setFont(font)
        self.moduleName.setObjectName(_fromUtf8("moduleName"))
        self.moduleName.addItem(_fromUtf8(""))
        self.moduleName.setItemText(0, _fromUtf8(""))
        self.moduleName.addItem(_fromUtf8(""))
        self.moduleName.addItem(_fromUtf8(""))
        self.moduleName.addItem(_fromUtf8(""))
        self.moduleName.addItem(_fromUtf8(""))
        self.moduleName.addItem(_fromUtf8(""))
        self.moduleName.addItem(_fromUtf8(""))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 460, 71, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 460, 71, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.hybridName = QtGui.QComboBox(Dialog)
        self.hybridName.setGeometry(QtCore.QRect(210, 90, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hybridName.setFont(font)
        self.hybridName.setObjectName(_fromUtf8("hybridName"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.moduleName, self.qButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.qButton.setText(_translate("Dialog", "Exit", None))
        self.label.setText(_translate("Dialog", "Select the module:", None))
        self.moduleName.setItemText(1, _translate("Dialog", "R0", None))
        self.moduleName.setItemText(2, _translate("Dialog", "R1", None))
        self.moduleName.setItemText(3, _translate("Dialog", "R2", None))
        self.moduleName.setItemText(4, _translate("Dialog", "R3", None))
        self.moduleName.setItemText(5, _translate("Dialog", "R4", None))
        self.moduleName.setItemText(6, _translate("Dialog", "R5", None))
        self.pushButton_4.setText(_translate("Dialog", "Tools", None))
        self.pushButton_5.setText(_translate("Dialog", "Run", None))
        self.label_2.setText(_translate("Dialog", "Select the hybrid:", None))

