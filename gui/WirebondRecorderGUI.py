# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WirebondRecorderGUI.ui'
#
# Created: Tue Aug 08 12:15:19 2017
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

class Ui_WirebondRecorder(object):
    def setupUi(self, WirebondRecorder):
        WirebondRecorder.setObjectName(_fromUtf8("WirebondRecorder"))
        WirebondRecorder.resize(708, 853)
        self.qButton = QtGui.QPushButton(WirebondRecorder)
        self.qButton.setGeometry(QtCore.QRect(620, 790, 71, 41))
        self.qButton.setObjectName(_fromUtf8("qButton"))
        self.label = QtGui.QLabel(WirebondRecorder)
        self.label.setGeometry(QtCore.QRect(10, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.moduleName = QtGui.QComboBox(WirebondRecorder)
        self.moduleName.setGeometry(QtCore.QRect(180, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.moduleName.setFont(font)
        self.moduleName.setObjectName(_fromUtf8("moduleName"))
        self.pushButton_5 = QtGui.QPushButton(WirebondRecorder)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 790, 71, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.hybridName = QtGui.QComboBox(WirebondRecorder)
        self.hybridName.setGeometry(QtCore.QRect(180, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hybridName.setFont(font)
        self.hybridName.setObjectName(_fromUtf8("hybridName"))
        self.label_2 = QtGui.QLabel(WirebondRecorder)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.imgSelect = QtGui.QLabel(WirebondRecorder)
        self.imgSelect.setGeometry(QtCore.QRect(10, 120, 687, 660))
        self.imgSelect.setAutoFillBackground(True)
        self.imgSelect.setFrameShape(QtGui.QFrame.Box)
        self.imgSelect.setFrameShadow(QtGui.QFrame.Plain)
        self.imgSelect.setText(_fromUtf8(""))
        self.imgSelect.setObjectName(_fromUtf8("imgSelect"))
        self.label_3 = QtGui.QLabel(WirebondRecorder)
        self.label_3.setGeometry(QtCore.QRect(580, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.levelLabel = QtGui.QLabel(WirebondRecorder)
        self.levelLabel.setGeometry(QtCore.QRect(640, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.levelLabel.setFont(font)
        self.levelLabel.setText(_fromUtf8(""))
        self.levelLabel.setObjectName(_fromUtf8("levelLabel"))
        self.btnBack = QtGui.QPushButton(WirebondRecorder)
        self.btnBack.setGeometry(QtCore.QRect(490, 70, 71, 41))
        self.btnBack.setObjectName(_fromUtf8("btnBack"))

        self.retranslateUi(WirebondRecorder)
        QtCore.QMetaObject.connectSlotsByName(WirebondRecorder)
        WirebondRecorder.setTabOrder(self.moduleName, self.qButton)

    def retranslateUi(self, WirebondRecorder):
        WirebondRecorder.setWindowTitle(_translate("WirebondRecorder", "Wirebond Recorder", None))
        self.qButton.setText(_translate("WirebondRecorder", "Exit", None))
        self.label.setText(_translate("WirebondRecorder", "Select the module:", None))
        self.pushButton_5.setText(_translate("WirebondRecorder", "Run", None))
        self.label_2.setText(_translate("WirebondRecorder", "Select the hybrid:", None))
        self.label_3.setText(_translate("WirebondRecorder", "Current level:", None))
        self.btnBack.setText(_translate("WirebondRecorder", "Back", None))

