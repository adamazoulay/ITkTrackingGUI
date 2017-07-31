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

        #If module is selected, populate hybrid selection
        self.moduleName.currentIndexChanged.connect(self.populate_hybrids)

        #quit
        self.qButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        
    def populate_hybrids(self):
        moduleNum = self.moduleName.currentIndex() - 1
        self.hybridName.clear()

        if moduleNum >= 0:
            self.hybridName.addItem(str(moduleNum))
        
    

    

def displayGui():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = MainApp()                    # We set the form to be our MainApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    displayGui()                              # run the main function

