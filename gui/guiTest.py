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

        #Here we store the valid selection areas (i.e. bond pads)
        #  give a rough area and assume all are square, so we
        #  can just pass a single point and build the box while
        #  we check the location of the click
        activeSelectionAreasASIC = {"1" : (248,65)}
        

        self.activeAreas = {"root" : activeAreasRoot, "R0" : activeAreasR0,\
                            "R0H0" : activeAreasR0H0, "R0H1" : activeAreasR0H1,\
                            "ASIC" : activeAreasASIC}

        self.activeSelectionAreas = {"ASIC" : activeSelectionAreasASIC}

        #Load the initial module selection img
        self.imgSelect.setPixmap(QtGui.QPixmap('imgs/root.jpg',"1")) #Why 1??

        #If module is selected by picture, change the module list
        self.imgSelect.mousePressEvent = self.executeSelection

        #Back button
        self.btnBack.clicked.connect(self.levelUp)

        #Run button
        self.btnChangeMode.clicked.connect(self.changeMode)

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

        #print('(' + str(x) + ',' +  str(y) + '),') #DEBUG

        name = self.level[-1]

        #Check if it's inside any of the current active areas
        if self.browseMode:
            curDict = self.activeAreas[name]
        elif self.selectionMode:
            curDict = self.activeSelectionAreas[name]

        for area in curDict:
            name = area
            coords = curDict[name]

            #Need to build pad box if in selection mode
            if self.selectionMode:
                xVal = coords[0]
                yVal = coords[1]
                size = 5
                coordsTemp = [(xVal-size,yVal+size), (xVal+size,yVal+size),\
                              (xVal+size,yVal-size), (xVal-size,yVal-size)]
                coords = coordsTemp

            tempPath = mplPath.Path(np.array([coords[0], coords[1],\
                                              coords[2], coords[3]]))
            inside = tempPath.contains_point((x,y))

            #If it is, do stuff
            if inside and self.browseMode:                    
                self.level.append(name) #Add level to level array
                self.levelLabel.setText(self.level[-1]) #change level label DEBUG?

                #Need to place the new picture
                #print('imgs/' + name + '.jpg') #DEBUG
                self.imgSelect.setPixmap(QtGui.QPixmap('imgs/' + name + '.jpg','1'))

            if inside and self.selectionMode:
                #Display box around selected pad
                #  TODO: if already selected, unselect it
                print(name)
                self.drawBox(coords)
                

    def drawBox(self, coords):
        painter = QtGui.QPainter()
        painter.begin(self.imgSelect)        
        painter.setBrush(QtGui.QColor(000,000,255))
        print(coords)
        
        painter.drawRect(0,0,300,300)#(coords[0][0],coords[0][1],\
                         #coords[1][0],coords[1][1])

        painter.end()
        #self.update()
                

    def changeMode(self):
        #If we're in browse mode:
        if self.browseMode:
            self.browseMode = False
            self.selectionMode = True
            self.imgSelect.setStyleSheet("border: 2px solid red;")
            self.btnChangeMode.setText("Browse Mode")
            return

        #If we're in selection mode:
        if self.selectionMode:
            self.browseMode = True
            self.selectionMode = False
            self.imgSelect.setStyleSheet("border: 2px solid black;")
            self.btnChangeMode.setText("Selection Mode")
            return
        

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
    

