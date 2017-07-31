# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QAgui.ui'
#
# Created: Mon Jul 31 12:47:37 2017
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
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 460, 71, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(210, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 460, 71, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 460, 71, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 90, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox, self.pushButton_3)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_3.setText(_translate("Dialog", "Exit", None))
        self.label.setText(_translate("Dialog", "Select the module:", None))
        self.comboBox.setItemText(0, _translate("Dialog", "R0", None))
        self.comboBox.setItemText(1, _translate("Dialog", "R1", None))
        self.comboBox.setItemText(2, _translate("Dialog", "R2", None))
        self.comboBox.setItemText(3, _translate("Dialog", "R3", None))
        self.comboBox.setItemText(4, _translate("Dialog", "R4", None))
        self.comboBox.setItemText(5, _translate("Dialog", "R5", None))
        self.pushButton_4.setText(_translate("Dialog", "Tools", None))
        self.pushButton_5.setText(_translate("Dialog", "Run", None))
        self.label_2.setText(_translate("Dialog", "Select the hybrid:", None))

