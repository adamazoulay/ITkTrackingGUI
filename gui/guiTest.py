from PyQt4 import QtGui # Import the PyQt4 module we'll need
from PyQt4 import QtCore # for quit button
import sys # We need sys so that we can pass argv to QApplication


import QAgui # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer


class MainApp(QtGui.QMainWindow, QAgui.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

        #First, let's populate the list of available module (based on images)
        self.populate_modules

        #If module is selected, populate hybrid selection
        self.moduleName.currentIndexChanged.connect(self.populate_hybrids)

        #quit
        self.qButton.clicked.connect(QtCore.QCoreApplication.instance().quit)


    #List population functions
    def populate_modules(self):
        self.moduleName.clear() #Clear the list
        
        #Get list of images files without extension
        #  then use them to populate the module list
        #Likewise, do this with the hybrids, asics, etc
        
    def populate_hybrids(self):
        moduleNum = self.moduleName.currentIndex() - 1
        self.hybridName.clear()

        #R0 module
        if moduleNum == 0:
            self.hybridName.addItem("")
            self.hybridName.addItem("H0")
            self.hybridName.addItem("H1")
        #R1
        if moduleNum == 1:
            self.hybridName.addItem("")
            self.hybridName.addItem("H0")
            self.hybridName.addItem("H1")
        #R3
        if moduleNum == 3:
            self.hybridName.addItem("")
            self.hybridName.addItem("H0")
            self.hybridName.addItem("H1")
            self.hybridName.addItem("H2")
            self.hybridName.addItem("H3")
        #R4
        if moduleNum == 4:
            self.hybridName.addItem("")
            self.hybridName.addItem("H0")
            self.hybridName.addItem("H1")
        #R5
        if moduleNum == 5:
            self.hybridName.addItem("")
            self.hybridName.addItem("H0")
            self.hybridName.addItem("H1")
    

    

def displayGui():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = MainApp()                    # We set the form to be our MainApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    displayGui()                              # run the main function

