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
        WirebondRecorder.resize(854, 796)
        self.centralwidget = QtWidgets.QWidget(WirebondRecorder)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnChangeMode = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnChangeMode.sizePolicy().hasHeightForWidth())
        self.btnChangeMode.setSizePolicy(sizePolicy)
        self.btnChangeMode.setMinimumSize(QtCore.QSize(100, 40))
        self.btnChangeMode.setMaximumSize(QtCore.QSize(100, 40))
        self.btnChangeMode.setIconSize(QtCore.QSize(16, 16))
        self.btnChangeMode.setObjectName("btnChangeMode")
        self.horizontalLayout.addWidget(self.btnChangeMode)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setMinimumSize(QtCore.QSize(90, 40))
        self.btnSave.setMaximumSize(QtCore.QSize(90, 40))
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.qButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qButton.sizePolicy().hasHeightForWidth())
        self.qButton.setSizePolicy(sizePolicy)
        self.qButton.setMinimumSize(QtCore.QSize(90, 40))
        self.qButton.setMaximumSize(QtCore.QSize(90, 40))
        self.qButton.setObjectName("qButton")
        self.horizontalLayout.addWidget(self.qButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(340, 40))
        self.label.setMaximumSize(QtCore.QSize(340, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBack.sizePolicy().hasHeightForWidth())
        self.btnBack.setSizePolicy(sizePolicy)
        self.btnBack.setMinimumSize(QtCore.QSize(90, 40))
        self.btnBack.setMaximumSize(QtCore.QSize(90, 40))
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout_2.addWidget(self.btnBack)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.imgSelect = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgSelect.sizePolicy().hasHeightForWidth())
        self.imgSelect.setSizePolicy(sizePolicy)
        self.imgSelect.setAutoFillBackground(False)
        self.imgSelect.setStyleSheet("border: 2px solid black;")
        self.imgSelect.setFrameShape(QtWidgets.QFrame.Box)
        self.imgSelect.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imgSelect.setText("")
        self.imgSelect.setObjectName("imgSelect")
        self.gridLayout.addWidget(self.imgSelect, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        WirebondRecorder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WirebondRecorder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 26))
        self.menubar.setObjectName("menubar")
        WirebondRecorder.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WirebondRecorder)
        self.statusbar.setObjectName("statusbar")
        WirebondRecorder.setStatusBar(self.statusbar)

        self.retranslateUi(WirebondRecorder)
        QtCore.QMetaObject.connectSlotsByName(WirebondRecorder)

    def retranslateUi(self, WirebondRecorder):
        _translate = QtCore.QCoreApplication.translate
        WirebondRecorder.setWindowTitle(_translate("WirebondRecorder", "MainWindow"))
        self.btnChangeMode.setText(_translate("WirebondRecorder", "Selection Mode"))
        self.btnSave.setText(_translate("WirebondRecorder", "Save"))
        self.qButton.setText(_translate("WirebondRecorder", "Exit"))
        self.label.setText(_translate("WirebondRecorder", "Wirebond Recorder"))
        self.btnBack.setText(_translate("WirebondRecorder", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WirebondRecorder = QtWidgets.QMainWindow()
    ui = Ui_WirebondRecorder()
    ui.setupUi(WirebondRecorder)
    WirebondRecorder.show()
    sys.exit(app.exec_())

