# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WirebondRecorderGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WirebondRecorder(object):
    def setupUi(self, WirebondRecorder):
        WirebondRecorder.setObjectName("WirebondRecorder")
        WirebondRecorder.resize(708, 853)
        self.qButton = QtWidgets.QPushButton(WirebondRecorder)
        self.qButton.setGeometry(QtCore.QRect(620, 790, 71, 41))
        self.qButton.setObjectName("qButton")
        self.pushButton_5 = QtWidgets.QPushButton(WirebondRecorder)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 790, 71, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.imgSelect = QtWidgets.QLabel(WirebondRecorder)
        self.imgSelect.setGeometry(QtCore.QRect(10, 120, 687, 660))
        self.imgSelect.setAutoFillBackground(True)
        self.imgSelect.setFrameShape(QtWidgets.QFrame.Box)
        self.imgSelect.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imgSelect.setText("")
        self.imgSelect.setObjectName("imgSelect")
        self.label_3 = QtWidgets.QLabel(WirebondRecorder)
        self.label_3.setGeometry(QtCore.QRect(430, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.levelLabel = QtWidgets.QLabel(WirebondRecorder)
        self.levelLabel.setGeometry(QtCore.QRect(550, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.levelLabel.setFont(font)
        self.levelLabel.setText("")
        self.levelLabel.setObjectName("levelLabel")
        self.btnBack = QtWidgets.QPushButton(WirebondRecorder)
        self.btnBack.setGeometry(QtCore.QRect(620, 70, 71, 41))
        self.btnBack.setObjectName("btnBack")
        self.label = QtWidgets.QLabel(WirebondRecorder)
        self.label.setGeometry(QtCore.QRect(10, 0, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(WirebondRecorder)
        QtCore.QMetaObject.connectSlotsByName(WirebondRecorder)

    def retranslateUi(self, WirebondRecorder):
        _translate = QtCore.QCoreApplication.translate
        WirebondRecorder.setWindowTitle(_translate("WirebondRecorder", "Wirebond Recorder"))
        self.qButton.setText(_translate("WirebondRecorder", "Exit"))
        self.pushButton_5.setText(_translate("WirebondRecorder", "Run"))
        self.label_3.setText(_translate("WirebondRecorder", "Current level:"))
        self.btnBack.setText(_translate("WirebondRecorder", "Back"))
        self.label.setText(_translate("WirebondRecorder", "Wirebond Recorder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WirebondRecorder = QtWidgets.QDialog()
    ui = Ui_WirebondRecorder()
    ui.setupUi(WirebondRecorder)
    WirebondRecorder.show()
    sys.exit(app.exec_())

