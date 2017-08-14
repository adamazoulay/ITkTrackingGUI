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
        self.curImg = "root"
        self.selectedPads = []
        self.counter = -3
        self.curDict = {}

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
        activeSelectionAreasASIC = {"1" : (246,65), "2" : (258,66), "3" : (275,64),\
                                    "4" : (288,67), "5" : (301,65), "6" : (309,65),\
                                    "7" : (334,64), "8" : (344,63), "9" : (353,64),\
                                    "10" : (362,64), "11" : (371,64), "12" : (380,64),\
                                    "13" : (391,64), "14" : (398,63), "15" : (408,64),\
                                    "16" : (415,63), "17" : (425,63), "18" : (434,64),\
                                    "19" : (443,63), "20" : (453,63), "21" : (462,63)}
        

        self.activeAreas = {"root" : activeAreasRoot, "R0" : activeAreasR0,\
                            "R0H0" : activeAreasR0H0, "R0H1" : activeAreasR0H1,\
                            "ASIC" : activeAreasASIC}

        self.activeSelectionAreas = {"ASIC" : activeSelectionAreasASIC}

        #Load the initial module selection img
        self.loadImg()

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

            self.curImg = name
            self.loadImg()
            

    def executeSelection(self, ev):
        #Grab click location    
        x = ev.pos().x()
        y = ev.pos().y()

        self.counter += 1
        #print('"' + str(self.counter)+'"' + ' : (' + str(x) + ',' +  str(y) + '),') #DEBUG

        name = self.level[-1]

        #Check if it's inside any of the current active areas
        if self.browseMode:
            self.curDict = self.activeAreas[name]
        elif self.selectionMode:
            self.curDict = self.activeSelectionAreas[name]

        for area in self.curDict:
            name = area
            coords = self.curDict[name]

            #Need to build pad box if in selection mode
            if self.selectionMode:
                xVal = coords[0]
                yVal = coords[1]
                size = 4
                #Order: bottom left, bottom right, top right, top left
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
                self.curImg = name
                self.loadImg()

            if inside and self.selectionMode:
                #Display box around selected pad
                #  TODO: if already selected, unselect it
                self.manageBoxs(name, size)

    def manageBoxs(self, name, size):
        #First add the pad to the array
        #  TODO: check if already in list and if so, delete it
        if name in self.selectedPads:
            self.selectedPads.remove(name)
        else:
            self.selectedPads.append(name)

        #Img refresh
        self.loadImg()

        #Prep painter
        painter = QtGui.QPainter()
        painter.begin(self.imgSelect.pixmap())        
        painter.setBrush(QtGui.QColor(255,0,0))        

        #draw all boxes
        for pad in self.selectedPads:
            #Get top right coords of pad
            coords = self.curDict[pad]
            xVal = coords[0]
            yVal = coords[1]            
            painter.drawRect(xVal-size,yVal-size, 2*size, 2*size)

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
            self.selectedPads = []
            return

    def loadImg(self):
        #Load name.jpg into Qlabel imgSelect
        self.imgSelect.setPixmap(QtGui.QPixmap('imgs/'+ self.curImg + '.jpg',"1")) #Why 1??
        

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
    

