from PyQt5 import QtWidgets, uic  # Import the PyQt5 modules we'll need


# Define the classes for the edit window gui
class ConfigEditWidget(QtWidgets.QMainWindow):

    def __init__(self, parent):
        super(self.__class__, self).__init__()
        uic.loadUi('lib/config.ui', self)
        self.parent = parent

        # Load up all current configuration variables
        self.unText.setText(self.parent.config['un'])
        self.instituteText.setText(self.parent.config['inst'])
        self.db1Text.setText(self.parent.config['dbkey1'])
        self.db2Text.setText(self.parent.config['dbkey2'])
        self.idText.setText(self.parent.config['idNumber'])

        self.btnSaveConfig.clicked.connect(self.save_config)

        self.btnCancel.clicked.connect(self.close)

    #  Go through all fields and save them to the header in the parent
    def save_config(self):
        self.parent.config['un'] = self.unText.text()
        self.parent.config['inst'] = self.instituteText.text()
        self.parent.config['dbkey1'] = self.db1Text.text()
        self.parent.config['dbkey1'] = self.db1Text.text()
        self.parent.config['idNumber'] = self.idText.text()
        self.close()
