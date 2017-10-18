# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfirmWindowGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfirmWindow(object):
    def setupUi(self, ConfirmWindow):
        ConfirmWindow.setObjectName("ConfirmWindow")
        ConfirmWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        ConfirmWindow.resize(346, 146)
        self.verticalLayoutWidget = QtWidgets.QWidget(ConfirmWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnContinue = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnContinue.sizePolicy().hasHeightForWidth())
        self.btnContinue.setSizePolicy(sizePolicy)
        self.btnContinue.setObjectName("btnContinue")
        self.horizontalLayout.addWidget(self.btnContinue)
        self.btnSecondSave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSecondSave.sizePolicy().hasHeightForWidth())
        self.btnSecondSave.setSizePolicy(sizePolicy)
        self.btnSecondSave.setObjectName("btnSecondSave")
        self.horizontalLayout.addWidget(self.btnSecondSave)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnCancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ConfirmWindow)
        QtCore.QMetaObject.connectSlotsByName(ConfirmWindow)

    def retranslateUi(self, ConfirmWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfirmWindow.setWindowTitle(_translate("ConfirmWindow", "Unsaved Changes"))
        self.label.setText(_translate("ConfirmWindow", "There are unsaved pads selected.\n"
"Continue?\n"
""))
        self.btnContinue.setText(_translate("ConfirmWindow", "Continue"))
        self.btnSecondSave.setText(_translate("ConfirmWindow", "Save"))
        self.btnCancel.setText(_translate("ConfirmWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfirmWindow = QtWidgets.QDialog()
    ui = Ui_ConfirmWindow()
    ui.setupUi(ConfirmWindow)
    ConfirmWindow.show()
    sys.exit(app.exec_())

