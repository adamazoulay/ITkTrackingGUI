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
        WirebondRecorder.resize(826, 685)
        self.centralwidget = QtWidgets.QWidget(WirebondRecorder)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.sldrZoom = QtWidgets.QSlider(self.centralwidget)
        self.sldrZoom.setMinimum(1)
        self.sldrZoom.setMaximum(4)
        self.sldrZoom.setPageStep(1)
        self.sldrZoom.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.sldrZoom.setObjectName("sldrZoom")
        self.verticalLayout.addWidget(self.sldrZoom)
        self.lblZoom = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblZoom.sizePolicy().hasHeightForWidth())
        self.lblZoom.setSizePolicy(sizePolicy)
        self.lblZoom.setMinimumSize(QtCore.QSize(20, 0))
        self.lblZoom.setMaximumSize(QtCore.QSize(20, 16777215))
        self.lblZoom.setObjectName("lblZoom")
        self.verticalLayout.addWidget(self.lblZoom, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 4, 1, 1)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
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
        self.imgSelect = QtWidgets.QGraphicsView(self.centralwidget)
        self.imgSelect.setObjectName("imgSelect")
        self.gridLayout.addWidget(self.imgSelect, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        WirebondRecorder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WirebondRecorder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        WirebondRecorder.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WirebondRecorder)
        self.statusbar.setObjectName("statusbar")
        WirebondRecorder.setStatusBar(self.statusbar)
        self.actionSave_Ctrl_S = QtWidgets.QAction(WirebondRecorder)
        self.actionSave_Ctrl_S.setObjectName("actionSave_Ctrl_S")
        self.actionExit = QtWidgets.QAction(WirebondRecorder)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_Ctrl_o = QtWidgets.QAction(WirebondRecorder)
        self.actionOpen_Ctrl_o.setObjectName("actionOpen_Ctrl_o")
        self.actionSave_As_Ctrl_a = QtWidgets.QAction(WirebondRecorder)
        self.actionSave_As_Ctrl_a.setObjectName("actionSave_As_Ctrl_a")
        self.menuFile.addAction(self.actionOpen_Ctrl_o)
        self.menuFile.addAction(self.actionSave_Ctrl_S)
        self.menuFile.addAction(self.actionSave_As_Ctrl_a)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(WirebondRecorder)
        QtCore.QMetaObject.connectSlotsByName(WirebondRecorder)

    def retranslateUi(self, WirebondRecorder):
        _translate = QtCore.QCoreApplication.translate
        WirebondRecorder.setWindowTitle(_translate("WirebondRecorder", "WBR Selection"))
        self.lblZoom.setText(_translate("WirebondRecorder", "1x"))
        self.btnChangeMode.setText(_translate("WirebondRecorder", "Selection Mode"))
        self.btnSave.setText(_translate("WirebondRecorder", "Save"))
        self.label.setText(_translate("WirebondRecorder", "Wirebond Recorder"))
        self.btnBack.setText(_translate("WirebondRecorder", "Back"))
        self.menuFile.setTitle(_translate("WirebondRecorder", "File"))
        self.menuTools.setTitle(_translate("WirebondRecorder", "Tools"))
        self.menuHelp.setTitle(_translate("WirebondRecorder", "Help"))
        self.actionSave_Ctrl_S.setText(_translate("WirebondRecorder", "Save (Ctrl-s)"))
        self.actionExit.setText(_translate("WirebondRecorder", "Exit"))
        self.actionOpen_Ctrl_o.setText(_translate("WirebondRecorder", "Open (Ctrl-o)"))
        self.actionSave_As_Ctrl_a.setText(_translate("WirebondRecorder", "Save As (Ctrl-a)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WirebondRecorder = QtWidgets.QMainWindow()
    ui = Ui_WirebondRecorder()
    ui.setupUi(WirebondRecorder)
    WirebondRecorder.show()
    sys.exit(app.exec_())

