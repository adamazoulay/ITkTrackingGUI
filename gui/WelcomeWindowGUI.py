# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WelcomeWindowGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WelcomeWindow(object):
    def setupUi(self, WelcomeWindow):
        WelcomeWindow.setObjectName("WelcomeWindow")
        WelcomeWindow.setEnabled(True)
        WelcomeWindow.resize(258, 385)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WelcomeWindow.sizePolicy().hasHeightForWidth())
        WelcomeWindow.setSizePolicy(sizePolicy)
        WelcomeWindow.setMinimumSize(QtCore.QSize(258, 385))
        WelcomeWindow.setMaximumSize(QtCore.QSize(258, 385))
        self.verticalLayoutWidget = QtWidgets.QWidget(WelcomeWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 197, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btnWirebondRecorder = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnWirebondRecorder.sizePolicy().hasHeightForWidth())
        self.btnWirebondRecorder.setSizePolicy(sizePolicy)
        self.btnWirebondRecorder.setObjectName("btnWirebondRecorder")
        self.verticalLayout.addWidget(self.btnWirebondRecorder)
        self.btnTools = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTools.sizePolicy().hasHeightForWidth())
        self.btnTools.setSizePolicy(sizePolicy)
        self.btnTools.setObjectName("btnTools")
        self.verticalLayout.addWidget(self.btnTools)
        self.btnExit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout.addWidget(self.btnExit)

        self.retranslateUi(WelcomeWindow)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWindow)

    def retranslateUi(self, WelcomeWindow):
        _translate = QtCore.QCoreApplication.translate
        WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "Wirebonding QA Toolkit"))
        self.label.setText(_translate("WelcomeWindow", "\n"
"Wirebonding\n"
"QA Toolkit\n"
"\n"
""))
        self.btnWirebondRecorder.setText(_translate("WelcomeWindow", "Wirebond Recorder"))
        self.btnTools.setText(_translate("WelcomeWindow", "Tools"))
        self.btnExit.setText(_translate("WelcomeWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeWindow = QtWidgets.QDialog()
    ui = Ui_WelcomeWindow()
    ui.setupUi(WelcomeWindow)
    WelcomeWindow.show()
    sys.exit(app.exec_())

