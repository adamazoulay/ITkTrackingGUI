# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QAgui.ui'
#
# Created: Tue Aug 01 10:45:18 2017
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(805, 616)
        self.qButton = QtGui.QPushButton(MainWindow)
        self.qButton.setGeometry(QtCore.QRect(720, 560, 71, 41))
        self.qButton.setObjectName(_fromUtf8("qButton"))
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(10, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.moduleName = QtGui.QComboBox(MainWindow)
        self.moduleName.setGeometry(QtCore.QRect(190, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.moduleName.setFont(font)
        self.moduleName.setObjectName(_fromUtf8("moduleName"))
        self.pushButton_4 = QtGui.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 560, 71, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(MainWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 560, 71, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.hybridName = QtGui.QComboBox(MainWindow)
        self.hybridName.setGeometry(QtCore.QRect(190, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hybridName.setFont(font)
        self.hybridName.setObjectName(_fromUtf8("hybridName"))
        self.label_2 = QtGui.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.R0jpg = QtGui.QGraphicsView(MainWindow)
        self.R0jpg.setGeometry(QtCore.QRect(260, 30, 81, 81))
        self.R0jpg.setObjectName(_fromUtf8("R0jpg"))
        self.R3jpg = QtGui.QGraphicsView(MainWindow)
        self.R3jpg.setGeometry(QtCore.QRect(530, 30, 81, 81))
        self.R3jpg.setObjectName(_fromUtf8("R3jpg"))
        self.R2jpg = QtGui.QGraphicsView(MainWindow)
        self.R2jpg.setGeometry(QtCore.QRect(440, 30, 81, 81))
        self.R2jpg.setObjectName(_fromUtf8("R2jpg"))
        self.R1jpg = QtGui.QGraphicsView(MainWindow)
        self.R1jpg.setGeometry(QtCore.QRect(350, 30, 81, 81))
        self.R1jpg.setObjectName(_fromUtf8("R1jpg"))
        self.R4jpg = QtGui.QGraphicsView(MainWindow)
        self.R4jpg.setGeometry(QtCore.QRect(620, 30, 81, 81))
        self.R4jpg.setObjectName(_fromUtf8("R4jpg"))
        self.R5jpg = QtGui.QGraphicsView(MainWindow)
        self.R5jpg.setGeometry(QtCore.QRect(710, 30, 81, 81))
        self.R5jpg.setObjectName(_fromUtf8("R5jpg"))
        self.mainImg = QtGui.QGraphicsView(MainWindow)
        self.mainImg.setGeometry(QtCore.QRect(20, 150, 771, 391))
        self.mainImg.setObjectName(_fromUtf8("mainImg"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.moduleName, self.qButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Wirebond Recorder", None))
        self.qButton.setText(_translate("MainWindow", "Exit", None))
        self.label.setText(_translate("MainWindow", "Select the module:", None))
        self.pushButton_4.setText(_translate("MainWindow", "Tools", None))
        self.pushButton_5.setText(_translate("MainWindow", "Run", None))
        self.label_2.setText(_translate("MainWindow", "Select the hybrid:", None))

