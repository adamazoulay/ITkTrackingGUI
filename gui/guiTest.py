from PyQt5 import QtGui, QtWidgets # Import the PyQt5 module we'll need
from PyQt5 import QtCore # for quit button
import sys, os # We need sys so that we can pass argv to QApplication
import matplotlib.path as mplPath
import numpy as np
from os import path

from WelcomeWindowGUI import Ui_WelcomeWindow #import design files
from WirebondRecorderGUI import Ui_WirebondRecorder

#================================================================================
#TODO:
#Make image loading a function

#================================================================================

#Define the classes for the various guis
class WirebondRecorder(QtWidgets.QMainWindow, Ui_WirebondRecorder):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

        #Start global variables
        self.level = ['root']
        self.selectionMode = False
        self.browseMode = True

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
        activeAreasASIC = {"pad1" : [(0,0), (0,0), (0,0), (0,0)]} #etc

        self.activeAreas = {"root" : activeAreasRoot, "R0" : activeAreasR0,\
                            "R0H0" : activeAreasR0H0, "R0H1" : activeAreasR0H1,\
                            "ASIC" : activeAreasASIC}

        #Load the initial module selection img
        self.imgSelect.setPixmap(QtGui.QPixmap('imgs/root.jpg',"1")) #Why 1??

        #If module is selected by picture, change the module list
        self.imgSelect.mousePressEvent = self.executeSelection

        #Back button
        self.btnBack.clicked.connect(self.levelUp)

        #Run button
        self.btnRun.clicked.connect(self.changeModeSelect)

        #hide form
        self.qButton.clicked.connect(self.hide)

    #Back button functionality
    def levelUp(self):
        #Check we aren't at root and are in browse mode
        if self.level[-1] != "root" and self.browseMode:
            self.level.pop(-1)
            name = self.level[-1]
            self.levelLabel.setText(self.level[-1])
            print(name)

            self.imgSelect.setPixmap(QtGui.QPixmap('imgs/' + name + '.jpg',"1"))

        #Switch back to browse mode (warning screen?)
        if self.selectionMode:
            self.browseMode = True
            self.selectionMode = False
            self.imgSelect.setStyleSheet("border: 2px solid black;")
            

    def executeSelection(self, ev):
        #Grab click location    
        x = ev.pos().x()
        y = ev.pos().y()

        print('(' + str(x) + ',' +  str(y) + '),') #DEBUG

        if self.browseMode:
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
                    self.level.append(name) #Add level to level array
                    self.levelLabel.setText(self.level[-1]) #change level label DEBUG?

                    #Need to place the new picture
                    print('imgs/' + name + '.jpg') #DEBUG
                    self.imgSelect.setPixmap(QtGui.QPixmap('imgs/' + name + '.jpg','1'))

        if self.selectionMode:
            print("cool")


    def changeModeSelect(self):
        self.browseMode = False
        self.selectionMode = True
        self.imgSelect.setStyleSheet("border: 2px solid red;")
        

class WelcomeWindow(QtWidgets.QMainWindow, Ui_WelcomeWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        #Show the WirebondRecorder
        self.btnWirebondRecorder.clicked.connect(displayRecorder)

        #Global quit
        self.btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)

#================================================================================
#All functions and main down here   
def displayGui():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = WelcomeWindow()              # We set the form to be our WelcomeWindow (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app

def displayRecorder():
    formRec = WirebondRecorder()
    formRec.show()

if __name__ == '__main__':              # if we're running file directly and not importing it
    displayGui()                              # run the main function
    

