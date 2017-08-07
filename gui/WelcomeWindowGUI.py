# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WelcomeWindowGUI.ui'
#
# Created: Mon Aug 07 12:43:57 2017
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

class Ui_WelcomeWindow(object):
    def setupUi(self, WelcomeWindow):
        WelcomeWindow.setObjectName(_fromUtf8("WelcomeWindow"))
        WelcomeWindow.setEnabled(True)
        WelcomeWindow.resize(258, 385)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WelcomeWindow.sizePolicy().hasHeightForWidth())
        WelcomeWindow.setSizePolicy(sizePolicy)
        WelcomeWindow.setMinimumSize(QtCore.QSize(258, 385))
        WelcomeWindow.setMaximumSize(QtCore.QSize(258, 385))
        self.verticalLayoutWidget = QtGui.QWidget(WelcomeWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 197, 351))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.btnWirebondRecorder = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnWirebondRecorder.sizePolicy().hasHeightForWidth())
        self.btnWirebondRecorder.setSizePolicy(sizePolicy)
        self.btnWirebondRecorder.setObjectName(_fromUtf8("btnWirebondRecorder"))
        self.verticalLayout.addWidget(self.btnWirebondRecorder)
        self.btnTools = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTools.sizePolicy().hasHeightForWidth())
        self.btnTools.setSizePolicy(sizePolicy)
        self.btnTools.setObjectName(_fromUtf8("btnTools"))
        self.verticalLayout.addWidget(self.btnTools)
        self.btnExit = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.verticalLayout.addWidget(self.btnExit)

        self.retranslateUi(WelcomeWindow)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWindow)

    def retranslateUi(self, WelcomeWindow):
        WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "Wirebonding QA Toolkit", None))
        self.label.setText(_translate("WelcomeWindow", "\n"
"Wirebonding\n"
" QA Toolkit\n"
"\n"
"", None))
        self.btnWirebondRecorder.setText(_translate("WelcomeWindow", "Wirebond Recorder", None))
        self.btnTools.setText(_translate("WelcomeWindow", "Tools", None))
        self.btnExit.setText(_translate("WelcomeWindow", "Exit", None))

