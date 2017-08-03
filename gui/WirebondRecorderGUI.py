# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WirebondRecorderGUI.ui'
#
# Created: Thu Aug 03 13:35:42 2017
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
        WirebondRecorder.resize(805, 616)
        self.qButton = QtGui.QPushButton(WirebondRecorder)
        self.qButton.setGeometry(QtCore.QRect(720, 560, 71, 41))
        self.qButton.setObjectName(_fromUtf8("qButton"))
        self.label = QtGui.QLabel(WirebondRecorder)
        self.label.setGeometry(QtCore.QRect(10, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.moduleName = QtGui.QComboBox(WirebondRecorder)
        self.moduleName.setGeometry(QtCore.QRect(190, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.moduleName.setFont(font)
        self.moduleName.setObjectName(_fromUtf8("moduleName"))
        self.pushButton_5 = QtGui.QPushButton(WirebondRecorder)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 560, 71, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.hybridName = QtGui.QComboBox(WirebondRecorder)
        self.hybridName.setGeometry(QtCore.QRect(190, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hybridName.setFont(font)
        self.hybridName.setObjectName(_fromUtf8("hybridName"))
        self.label_2 = QtGui.QLabel(WirebondRecorder)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(WirebondRecorder)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(260, 20, 531, 115))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.R0jpg = QtGui.QLabel(self.horizontalLayoutWidget)
        self.R0jpg.setFrameShape(QtGui.QFrame.Box)
        self.R0jpg.setFrameShadow(QtGui.QFrame.Raised)
        self.R0jpg.setLineWidth(1)
        self.R0jpg.setText(_fromUtf8(""))
        self.R0jpg.setObjectName(_fromUtf8("R0jpg"))
        self.horizontalLayout.addWidget(self.R0jpg)
        self.R1jpg = QtGui.QLabel(self.horizontalLayoutWidget)
        self.R1jpg.setMinimumSize(QtCore.QSize(0, 0))
        self.R1jpg.setFrameShape(QtGui.QFrame.Box)
        self.R1jpg.setFrameShadow(QtGui.QFrame.Raised)
        self.R1jpg.setText(_fromUtf8(""))
        self.R1jpg.setObjectName(_fromUtf8("R1jpg"))
        self.horizontalLayout.addWidget(self.R1jpg)
        self.R2jpg = QtGui.QLabel(self.horizontalLayoutWidget)
        self.R2jpg.setFrameShape(QtGui.QFrame.Box)
        self.R2jpg.setFrameShadow(QtGui.QFrame.Raised)
        self.R2jpg.setText(_fromUtf8(""))
        self.R2jpg.setObjectName(_fromUtf8("R2jpg"))
        self.horizontalLayout.addWidget(self.R2jpg)
        self.R3jpg = QtGui.QLabel(self.horizontalLayoutWidget)
        self.R3jpg.setFrameShape(QtGui.QFrame.Box)
        self.R3jpg.setFrameShadow(QtGui.QFrame.Raised)
        self.R3jpg.setText(_fromUtf8(""))
        self.R3jpg.setObjectName(_fromUtf8("R3jpg"))
        self.horizontalLayout.addWidget(self.R3jpg)
        self.R4jpg = QtGui.QLabel(self.horizontalLayoutWidget)
        self.R4jpg.setFrameShape(QtGui.QFrame.Box)
        self.R4jpg.setFrameShadow(QtGui.QFrame.Raised)
        self.R4jpg.setText(_fromUtf8(""))
        self.R4jpg.setObjectName(_fromUtf8("R4jpg"))
        self.horizontalLayout.addWidget(self.R4jpg)
        self.R5jpg = QtGui.QLabel(self.horizontalLayoutWidget)
        self.R5jpg.setFrameShape(QtGui.QFrame.Box)
        self.R5jpg.setFrameShadow(QtGui.QFrame.Raised)
        self.R5jpg.setText(_fromUtf8(""))
        self.R5jpg.setObjectName(_fromUtf8("R5jpg"))
        self.horizontalLayout.addWidget(self.R5jpg)
        self.label_3 = QtGui.QLabel(WirebondRecorder)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 761, 381))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setFrameShape(QtGui.QFrame.Box)
        self.label_3.setFrameShadow(QtGui.QFrame.Raised)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(WirebondRecorder)
        QtCore.QMetaObject.connectSlotsByName(WirebondRecorder)
        WirebondRecorder.setTabOrder(self.moduleName, self.qButton)

    def retranslateUi(self, WirebondRecorder):
        WirebondRecorder.setWindowTitle(_translate("WirebondRecorder", "Wirebond Recorder", None))
        self.qButton.setText(_translate("WirebondRecorder", "Exit", None))
        self.label.setText(_translate("WirebondRecorder", "Select the module:", None))
        self.pushButton_5.setText(_translate("WirebondRecorder", "Run", None))
        self.label_2.setText(_translate("WirebondRecorder", "Select the hybrid:", None))

