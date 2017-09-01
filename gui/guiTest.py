from PyQt5 import QtGui, QtWidgets  # Import the PyQt5 module we'll need
from PyQt5 import QtCore  # for quit button
import sys, os  # We need sys so that we can pass argv to QApplication
import matplotlib.path as mplPath
import numpy as np
from os import path

from WelcomeWindowGUI import Ui_WelcomeWindow  # import design files
from WirebondRecorderGUI import Ui_WirebondRecorder
from ConfirmWindowGUI import Ui_ConfirmWindow

# ================================================================================
# TODO:
#  Figure out pad selection saving.
# ================================================================================

# Define the classes for the various guis
class WirebondRecorder(QtWidgets.QMainWindow, Ui_WirebondRecorder):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined

        #set as central widget
        

        # Start global variables
        self.level = ['root']
        self.selectionMode = False
        self.browseMode = True
        self.curImg = "root"
        self.selectedPads = []
        self.counter = -3
        self.curDict = {}
        self.saved = True
        #Pad size scale (need to adjust for zooming stuff)
        self.size = 4

        # Need to store all active areas for each level
        activeAreasRoot = dict([["R0", [(96, 28), (263, 30), (257, 219), (93, 223)]],
                                ["R1", [(373, 38), (591, 39), (587, 224), (378, 222)]],
                                ["R2", [(0, 0), (0, 0), (0, 0), (0, 0)]],
                                ["R3", [(0, 0), (0, 0), (0, 0), (0, 0)]],
                                ["R4", [(0, 0), (0, 0), (0, 0), (0, 0)]],
                                ["R5", [(0, 0), (0, 0), (0, 0), (0, 0)]]])
        activeAreasR0 = {"R0H0": [(82,365), (616,364), (606,485), (93,492)],
                         "R0H1": [(63,199), (631,189), (623,305), (81,321)]}
        activeAreasR0H0 = {"ASIC": [(0, 0), (0, 0), (0, 0), (0, 0)]}
        activeAreasR0H1 = {"ASIC": [(29,284), (90,282), (90,328), (36,334)]}
        activeAreasASIC = {"pad1": [(0, 0), (0, 0), (0, 0), (0, 0)]}  # etc?

        # Here we store the valid selection areas (i.e. bond pads)
        #  give a rough area and assume all are square, so we
        #  can just pass a single point and build the box while
        #  we check the location of the click
        activeSelectionAreasASIC = {"1": (247, 65), "2": (256, 65), "3": (274, 65),
                                    "4": (288, 68), "5": (300, 65), "6": (309, 65),
                                    "7": (334, 65), "8": (343, 65), "9": (352, 65),
                                    "10": (361, 65), "11": (370, 65), "12": (379, 65),
                                    "13": (388, 65), "14": (397, 65), "15": (406, 65),
                                    "16": (415, 65), "17": (424, 65), "18": (433, 65),
                                    "19": (442, 65), "20": (451, 65), "21": (460, 65)}

        self.activeAreas = {"root": activeAreasRoot, "R0": activeAreasR0,
                            "R0H0": activeAreasR0H0, "R0H1": activeAreasR0H1,
                            "ASIC": activeAreasASIC}

        self.activeSelectionAreas = {"ASIC": activeSelectionAreasASIC}

        # Load the initial module selection img and selection areas
        self.loadImg()

        # If module is selected by picture, change the module list
        self.imgSelect.mousePressEvent = self.executeSelection

        # Back button
        self.btnBack.clicked.connect(self.levelUp)

        # Change mode button
        self.btnChangeMode.clicked.connect(self.changeMode)

        # Save button
        self.btnSave.clicked.connect(self.saveSelection)

        # hide form
        self.qButton.clicked.connect(self.hide)

    # Save any information about the selected pads
    def saveSelection(self):
        if len(self.selectedPads) == 0:
            print("Can't save")
            return
        print(self.level)
        print(self.selectedPads)
        self.saved = True


    # Back button functionality
    def levelUp(self):
        # Check we aren't at root and are in browse mode
        if self.level[-1] != "root" and self.browseMode:
            self.level.pop(-1)
            name = self.level[-1]

            self.curImg = name
            self.loadImg()


    # If the image is clicked, run checks
    def executeSelection(self, ev):
        # Grab click location
        x = ev.pos().x()
        y = ev.pos().y()

        self.counter += 1
        # print('"' + str(self.counter)+'"' + ' : (' + str(x) + ',' +  str(y) + '),') #DEBUG
        #print('(' + str(x) + ',' +  str(y) + ')')

        name = self.level[-1]

        # Check if it's inside any of the current active areas
        if self.browseMode:
            self.curDict = self.activeAreas[name]
        elif self.selectionMode:
            self.curDict = self.activeSelectionAreas[name]

        for area in self.curDict:
            name = area
            coords = self.curDict[name]

            # Need to build pad box if in selection mode
            if self.selectionMode:
                xVal = coords[0]
                yVal = coords[1]
                # Order: bottom left, bottom right, top right, top left
                size = self.size
                coordsTemp = [(xVal - size, yVal + size), (xVal + size, yVal + size),
                              (xVal + size, yVal - size), (xVal - size, yVal - size)]
                coords = coordsTemp

            tempPath = mplPath.Path(np.array([coords[0], coords[1],
                                              coords[2], coords[3]]))
            inside = tempPath.contains_point((x, y))

            # If it is, do stuff
            if inside and self.browseMode:
                self.level.append(name)  # Add level to level array

                # Need to place the new picture
                self.curImg = name
                self.loadImg()

            if inside and self.selectionMode:
                # Mark the pas list as unsaved
                self.saved = False
                # Display box around selected pad
                self.manageBoxes(name, size)

    def drawBoxes(self):
        size = self.size
        # Img refresh
        self.loadImg()

        # Prep painter
        painter = QtGui.QPainter()
        painter.begin(self.imgSelect.pixmap())
        painter.setPen(QtGui.QColor(255, 0, 0))

        # draw all boxes
        for area in self.curDict:
            # Draw hollow rect
            # Get top right coords of pad
            coords = self.curDict[area]
            xVal = coords[0]
            yVal = coords[1]            
            
            # if selected, fill in rect
            if area in self.selectedPads:
                painter.setBrush(QtGui.QColor(255, 0, 0))
            else:
                # Just set alpha to 0 (probably a better way to do this. there was!)
                painter.setBrush(QtCore.Qt.NoBrush)

            painter.drawRect(xVal - size, yVal - size, 2 * size, 2 * size)

        painter.end()

    def manageBoxes(self, name, size):
        # First add the pad to the array
        if name in self.selectedPads:
            self.selectedPads.remove(name)
        else:
            self.selectedPads.append(name)

        self.drawBoxes()

    def changeMode(self):
        # If we're in browse mode and a have pads to select:
        if self.browseMode and self.level[-1] == "ASIC":
            self.loadImg()
            self.browseMode = False
            self.selectionMode = True
            self.imgSelect.setStyleSheet("border: 2px solid red;")
            self.btnChangeMode.setText("Browse Mode")
            self.curDict = self.activeSelectionAreas[self.curImg]
            self.drawBoxes()
            return

        # If we're in selection mode:
        if self.selectionMode:
            if self.saved:
                self.loadImg()
                self.browseMode = True
                self.selectionMode = False
                self.imgSelect.setStyleSheet("border: 2px solid black;")
                self.btnChangeMode.setText("Selection Mode")
                self.selectedPads = []
                return
            else:
                # Open confirm window
                self.confirmWindow = ConfirmWindow(self)
                self.confirmWindow.show()

    def loadImg(self):
        # Load name.jpg into Qlabel imgSelect
        self.imgSelect.setPixmap(QtGui.QPixmap('imgs/' + self.curImg + '.jpg', "1"))  # Why 1??


class WelcomeWindow(QtWidgets.QMainWindow, Ui_WelcomeWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Show the WirebondRecorder
        self.btnWirebondRecorder.clicked.connect(displayRecorder)

        # Global quit
        self.btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)

class ConfirmWindow(QtWidgets.QMainWindow, Ui_ConfirmWindow):
    def __init__(self, formDataWindow):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.formDataWindow = formDataWindow

        # Save and continue
        self.btnSecondSave.clicked.connect(self.saveAndContinue)

        # Discard changes
        self.btnContinue.clicked.connect(self.discard)

        # Close window
        self.btnCancel.clicked.connect(self.hide)

    def saveAndContinue(self):
        # Run the save command and change to browse mode
        self.formDataWindow.saveSelection()
        self.formDataWindow.changeMode()
        self.hide()

    def discard(self):
        # Toss changes and go to browse mode
        self.formDataWindow.saved = True
        self.formDataWindow.changeMode()
        self.hide()


# ================================================================================
# All functions and main down here
def displayGui():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = WelcomeWindow()  # We set the form to be our WelcomeWindow (design)
    form.show()  # Show the form
    sys.exit(app.exec_())  # and execute the app


def displayRecorder():
    formRec = WirebondRecorder()
    formRec.show()


if __name__ == '__main__':  # if we're running file directly and not importing it
    displayGui()  # run the main function
