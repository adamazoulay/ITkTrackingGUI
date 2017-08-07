from PyQt4 import QtGui # Import the PyQt4 module we'll need
from PyQt4 import QtCore # for quit button
import sys, os # We need sys so that we can pass argv to QApplication
import matplotlib.path as mplPath
import numpy as np

from WelcomeWindowGUI import Ui_WelcomeWindow #import design files
from WirebondRecorderGUI import Ui_WirebondRecorder

#================================================================================
#Define the classes for the various guis

class WirebondRecorder(QtGui.QMainWindow, Ui_WirebondRecorder):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

        #Start an array here to keep track of the level we are at
        self.level = ['root']

        #Set level label (maybe debug?)
        self.levelLabel.setText(self.level[-1])

        #Need to store all active areas for each level
        activeAreasRoot = [["R0", [(96,28), (263,30), (257,219), (93,223)]],\
                           ["R1", [(0,0), (0,0), (0,0), (0,0)]],\
                           ["R2", [(0,0), (0,0), (0,0), (0,0)]],\
                           ["R3", [(0,0), (0,0), (0,0), (0,0)]],\
                           ["R4", [(0,0), (0,0), (0,0), (0,0)]],\
                           ["R5", [(0,0), (0,0), (0,0), (0,0)]]]

        self.activeAreas = [activeAreasRoot,[],[]]
        
        #First, let's populate the list and imgs of available module (based on images)
        self.populate_modules()

        #Load the initial module selection img
        self.imgSelect.setPixmap(QtGui.QPixmap('imgs/endcapModules.jpg'))

        
        #If module is selected by picture, change the module list
        self.imgSelect.mousePressEvent = self.executeSelection
       
        #If module is selected in list, populate hybrid selection
        # note: this works from picture and list selection
        self.moduleName.currentIndexChanged.connect(self.populate_hybrids)

        #hide form
        self.qButton.clicked.connect(self.hide)


    #List population functions
    def populate_modules(self):
        #Get list of images files without extension
        #  then use them to populate the module list
        #Likewise, do this with the hybrids, asics, etc
        self.moduleName.addItem("")
        modList = getModuleList()
        for name in modList:
            self.moduleName.addItem(name)
        
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


    def executeSelection(self, ev):
        #Grab click location    
        x = ev.pos().x()
        y = ev.pos().y()

        #Current zoom level
        level = len(self.level) - 1

        #Check if it's inside any of the active areas
        for area in self.activeAreas[0]:                  
            coords = area[1]
            tempPath = mplPath.Path(np.array([coords[0], coords[1],\
                                              coords[2], coords[3]]))
            inside = tempPath.contains_point((x,y))

            #If it is, do stuff
            if inside:
                print area[0]
                self.moduleName.setCurrentIndex(int(area[0][1])+1)
                self.level.append(area[0])
                self.levelLabel.setText(self.level[-1])
        

class WelcomeWindow(QtGui.QMainWindow, Ui_WelcomeWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        #Show the WirebondRecorder
        self.btnWirebondRecorder.clicked.connect(displayRecorder)

        #Global quit
        self.btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)




#================================================================================
#All functions and main down here   
def getModuleList():
    mods = []
    for x in os.listdir("../data/"):
        if x[0] == "R":
            mods.append(x)
    return mods

def displayGui():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = WelcomeWindow()              # We set the form to be our WelcomeWindow (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app

def displayRecorder():
    #appRec = QtGui.QApplication(sys.argv)
    formRec = WirebondRecorder()
    formRec.show()
    #appRec.exec_() 


if __name__ == '__main__':              # if we're running file directly and not importing it
    displayGui()                              # run the main function

