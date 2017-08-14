# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WirebondRecorderGUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WirebondRecorder(object):
    def setupUi(self, WirebondRecorder):
        WirebondRecorder.setObjectName("WirebondRecorder")
        WirebondRecorder.resize(711, 877)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WirebondRecorder.sizePolicy().hasHeightForWidth())
        WirebondRecorder.setSizePolicy(sizePolicy)
        self.imgSelect = QtWidgets.QLabel(WirebondRecorder)
        self.imgSelect.setGeometry(QtCore.QRect(10, 120, 687, 660))
        self.imgSelect.setAutoFillBackground(False)
        self.imgSelect.setStyleSheet("border: 2px solid black;")
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(WirebondRecorder)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 810, 691, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnRun = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRun.sizePolicy().hasHeightForWidth())
        self.btnRun.setSizePolicy(sizePolicy)
        self.btnRun.setIconSize(QtCore.QSize(16, 16))
        self.btnRun.setObjectName("btnRun")
        self.horizontalLayout.addWidget(self.btnRun)
        self.btnSave = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.qButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qButton.sizePolicy().hasHeightForWidth())
        self.qButton.setSizePolicy(sizePolicy)
        self.qButton.setObjectName("qButton")
        self.horizontalLayout.addWidget(self.qButton)

        self.retranslateUi(WirebondRecorder)
        QtCore.QMetaObject.connectSlotsByName(WirebondRecorder)

    def retranslateUi(self, WirebondRecorder):
        _translate = QtCore.QCoreApplication.translate
        WirebondRecorder.setWindowTitle(_translate("WirebondRecorder", "Wirebond Recorder"))
        self.label_3.setText(_translate("WirebondRecorder", "Current level:"))
        self.btnBack.setText(_translate("WirebondRecorder", "Back"))
        self.label.setText(_translate("WirebondRecorder", "Wirebond Recorder"))
        self.btnRun.setText(_translate("WirebondRecorder", "Run"))
        self.btnSave.setText(_translate("WirebondRecorder", "Save"))
        self.qButton.setText(_translate("WirebondRecorder", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WirebondRecorder = QtWidgets.QDialog()
    ui = Ui_WirebondRecorder()
    ui.setupUi(WirebondRecorder)
    WirebondRecorder.show()
    sys.exit(app.exec_())

