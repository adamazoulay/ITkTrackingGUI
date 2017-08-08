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
        activeAreasRoot = dict([["R0", [(96,28), (263,30), (257,219), (93,223)]],\
                                ["R1", [(373,38), (591,39), (587,224), (378,222)]],\
                                ["R2", [(0,0), (0,0), (0,0), (0,0)]],\
                                ["R3", [(0,0), (0,0), (0,0), (0,0)]],\
                                ["R4", [(0,0), (0,0), (0,0), (0,0)]],\
                                ["R5", [(0,0), (0,0), (0,0), (0,0)]]])
        activeAreasR0 = {"R0H0" : [(79,222), (594,224), (588,327), (82,319)],
                         "R0H1" : [(88,354), (582,355), (575,460), (100,456)]}
        activeAreasR0H0 = {"ASIC" : [(21,282), (73,278), (26,319), (76,315)]}
        activeAreasR0H1 = {"ASIC" : [(76,221), (122,220), (80,252), (126,248)]}
        activeAreasASIC = {"pad1" : []} #etc

        self.activeAreas = {"root" : activeAreasRoot, "R0" : activeAreasR0,\
                            "R0H0" : activeAreasR0H0, "R0H1" : activeAreasR0H1,\
                            "ASIC" : activeAreasASIC}
        
        #First, let's populate the list and imgs of available module (based on images)
        self.populate_modules()

        #Load the initial module selection img
        self.imgSelect.setPixmap(QtGui.QPixmap('imgs/root.jpg'))

        #If module is selected by picture, change the module list
        self.imgSelect.mousePressEvent = self.executeSelection
       
        #If module is selected in list, populate hybrid selection
        # note: this works from picture and list selection
        self.moduleName.currentIndexChanged.connect(self.populate_hybrids)

        #Back button
        self.btnBack.clicked.connect(self.levelUp)

        #hide form
        self.qButton.clicked.connect(self.hide)

    #Back button functionality
    def levelUp(self):
        #Check we aren't at root
        if self.level[-1] != "root":
            self.level.pop(-1)
            name = self.level[-1]
            self.levelLabel.setText(self.level[-1])
            print name

            self.imgSelect.setPixmap(QtGui.QPixmap('imgs/' + name + '.jpg'))
        

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


    def executeSelection(self, ev):
        #Grab click location    
        x = ev.pos().x()
        y = ev.pos().y()

        print '(' + str(x) + ',' +  str(y) + '),' #DEBUG

        #Check if it's inside any of the current active areas
        curDict = self.activeAreas[self.level[-1]]
        for area in curDict:
            name = area
            coords = curDict[name]
            tempPath = mplPath.Path(np.array([coords[0], coords[1],\
                                              coords[2], coords[3]]))
            inside = tempPath.contains_point((x,y))

            #If it is, do stuff
            if inside:
                #Make this all a function for use with the back button!!
                #print name #DEBUG
                #self.moduleName.setCurrentIndex(int(name[-1])+1) #Set correct module index FIX THIS
                self.level.append(name) #Add level to level array
                self.levelLabel.setText(self.level[-1]) #change level label DEBUG?

                #Need to place the new picture
                print 'imgs/' + name + '.jpg' #DEBUG
                self.imgSelect.setPixmap(QtGui.QPixmap('imgs/' + name + '.jpg'))
        

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
    formRec = WirebondRecorder()
    formRec.show()

if __name__ == '__main__':              # if we're running file directly and not importing it
    displayGui()                              # run the main function

