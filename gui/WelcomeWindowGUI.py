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
        WelcomeWindow.setWindowModality(QtCore.Qt.NonModal)
        WelcomeWindow.setEnabled(True)
        WelcomeWindow.resize(252, 384)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WelcomeWindow.sizePolicy().hasHeightForWidth())
        WelcomeWindow.setSizePolicy(sizePolicy)
        WelcomeWindow.setMinimumSize(QtCore.QSize(252, 384))
        WelcomeWindow.setMaximumSize(QtCore.QSize(252, 384))
        self.gridLayoutWidget = QtWidgets.QWidget(WelcomeWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 231, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnWirebondRecorder = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnWirebondRecorder.sizePolicy().hasHeightForWidth())
        self.btnWirebondRecorder.setSizePolicy(sizePolicy)
        self.btnWirebondRecorder.setMinimumSize(QtCore.QSize(150, 40))
        self.btnWirebondRecorder.setMaximumSize(QtCore.QSize(150, 40))
        self.btnWirebondRecorder.setObjectName("btnWirebondRecorder")
        self.gridLayout.addWidget(self.btnWirebondRecorder, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.btnTools = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTools.sizePolicy().hasHeightForWidth())
        self.btnTools.setSizePolicy(sizePolicy)
        self.btnTools.setMinimumSize(QtCore.QSize(150, 40))
        self.btnTools.setMaximumSize(QtCore.QSize(150, 40))
        self.btnTools.setObjectName("btnTools")
        self.gridLayout.addWidget(self.btnTools, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.btnExit = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setMinimumSize(QtCore.QSize(150, 40))
        self.btnExit.setMaximumSize(QtCore.QSize(150, 40))
        self.btnExit.setObjectName("btnExit")
        self.gridLayout.addWidget(self.btnExit, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.retranslateUi(WelcomeWindow)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWindow)

    def retranslateUi(self, WelcomeWindow):
        _translate = QtCore.QCoreApplication.translate
        WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "Form"))
        self.label.setText(_translate("WelcomeWindow", "\n"
"Wirebonding\n"
"QA Toolkit\n"
""))
        self.btnWirebondRecorder.setText(_translate("WelcomeWindow", "Wirebond Recorder"))
        self.btnTools.setText(_translate("WelcomeWindow", "Tools"))
        self.btnExit.setText(_translate("WelcomeWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeWindow = QtWidgets.QWidget()
    ui = Ui_WelcomeWindow()
    ui.setupUi(WelcomeWindow)
    WelcomeWindow.show()
    sys.exit(app.exec_())

