from PyQt5 import QtGui, QtWidgets  # Import the PyQt5 module we'll need
from PyQt5 import QtCore  # for quit button
import sys
import os  # We need sys so that we can pass argv to QApplication
import matplotlib.path as mplPath
import numpy as np
from os import path

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

        # set as central widget

        # Start global variables
        self.level = ['root']
        self.selectionMode = False
        self.browseMode = True
        self.curImg = "root"
        self.selectedPads = []
        self.counter = 0
        self.curDict = {}
        self.saved = True

        # Scale and offset values, for resize and adjust (need to change on
        # every resize and zoom)
        self.zoomScale = 1
        self.zoomOffset = (0, 0)
        self.xyOffset = (0, 0)  # (x, y)

        # Pixmap dims
        self.pixmapDims = (0, 0)  # (width, height)

        # Pad size scale (need to adjust for zooming stuff)
        self.size = 4

        # Start maximized and resized        
        self.showMaximized()       
        
        # Need to store all active areas for each level
        activeAreasRoot = dict([["R0", [(96, 28), (263, 30), (257, 219), (93, 223)]],
                                ["R1", [(373, 38), (591, 39),
                                        (587, 224), (378, 222)]],
                                ["R2", [(0, 0), (0, 0), (0, 0), (0, 0)]],
                                ["R3", [(0, 0), (0, 0), (0, 0), (0, 0)]],
                                ["R4", [(0, 0), (0, 0), (0, 0), (0, 0)]],
                                ["R5", [(0, 0), (0, 0), (0, 0), (0, 0)]]])
        activeAreasR0 = {"R0H0": [(82, 365), (616, 364), (606, 485), (93, 492)],
                         "R0H1": [(63, 199), (631, 189), (623, 305), (81, 321)]}
        activeAreasR0H0 = {"ASIC": [(0, 0), (0, 0), (0, 0), (0, 0)]}
        activeAreasR0H1 = {
            "ASIC": [(27, 38), (88, 33), (88, 79), (33, 82)]}
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
        activeSelectionAreasR0H1 = {"PWR": (10, 65)}

        self.activeAreas = {"root": activeAreasRoot, "R0": activeAreasR0,
                            "R0H0": activeAreasR0H0, "R0H1": activeAreasR0H1,
                            "ASIC": activeAreasASIC}

        self.activeSelectionAreas = {
            "R0H1": activeSelectionAreasR0H1, "ASIC": activeSelectionAreasASIC}

        # If module is selected by picture, change the module list
        self.imgSelect.mousePressEvent = self.executeSelection

        # Back button
        self.btnBack.clicked.connect(self.levelUp)

        # Change mode button
        self.btnChangeMode.clicked.connect(self.changeMode)

        # Save button
        self.btnSave.clicked.connect(self.saveSelection)

        # Load the initial module selection img and selection areas
        self.curDict = self.activeAreas[self.curImg]
        self.imgSelect.setAlignment(QtCore.Qt.AlignCenter)
        self.loadImg()

    # Get the scaling and offset values
    def findScaleAndOffset(self):
        # Determine new self.zoomScale and self.xyOffset
        # First get size of the imgSelect box
        imgSelectWidth = self.imgSelect.width()
        imgSelectHeight = self.imgSelect.height()

        pixMapWidth = self.pixmapDims[0]
        pixMapHeight = self.pixmapDims[1]

        # Find the xy offset
        xOff = (imgSelectWidth - pixMapWidth)/2
        yOff = (imgSelectHeight - pixMapHeight)/2

        # Add zoom offet
        xZoom = self.zoomOffset[0]
        yZoom = self.zoomOffset[1]

        self.xyOffset = (xOff, yOff)

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
        # print('"' + str(self.counter)+'"' + ' : (' + str(x) + ',' +  str(y) +
        # '),') #DEBUG
        print('(' + str(x) + ',' + str(y) + ')')

        name = self.level[-1]

        # Check if it's inside any of the current active areas
        if self.browseMode:
            self.curDict = self.activeAreas[name]
        elif self.selectionMode:
            self.curDict = self.activeSelectionAreas[name]

        # Refresh the scale and offset to correct the coordinates
        self.findScaleAndOffset()

        xOff = self.xyOffset[0]
        yOff = self.xyOffset[1]
        x -= xOff
        y -= yOff

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

        #Set pen colour
        Qred = QtGui.QColor(255, 0, 0)

        # Load correct currentDict
        if self.browseMode:
            tempDict = self.activeAreas[self.curImg]
        else:
            tempDict = self.curDict

        for area in tempDict:
            # draw all boxes in selection mode
            if self.selectionMode:
                # Draw hollow rect
                # Get top right coords of pad
                coords = tempDict[area]
                xVal = coords[0]
                yVal = coords[1]

                rect = QtCore.QRectF(xVal-size, yVal-size, 2*size, 2*size)

                # if selected, fill in rect
                if area in self.selectedPads:
                    self.scene.addRect(rect, Qred, Qred)
                else:
                    # Just set alpha to 0 (probably a better way to do this.
                    # there was!)
                    self.scene.addRect(rect, Qred, QtGui.QColor(0, 0, 0, 0))

            if self.browseMode:
                # Draw hollow rect
                # Get top right and bottom left coords of area
                coords = tempDict[area]
                xValTop = coords[0][0]
                yValTop = coords[0][1]
                xValBot = coords[2][0]
                yValBot = coords[2][1]

                width = abs(xValBot-xValTop)
                height = abs(yValBot-yValTop)

                rect = QtCore.QRectF(xValTop, yValTop, width, height)

                self.scene.addRect(rect, Qred, QtGui.QColor(0, 0, 0, 0))

    def manageBoxes(self, name, size):
        # First add the pad to the array
        if name in self.selectedPads:
            self.selectedPads.remove(name)
        else:
            self.selectedPads.append(name)

        self.loadImg()

    def changeMode(self):
        # If we're in browse mode and a have pads to select:
        if self.browseMode and (self.level[-1] in self.activeSelectionAreas):
            self.browseMode = False
            self.selectionMode = True
            self.imgSelect.setStyleSheet("border: 2px solid red;")
            self.btnChangeMode.setText("Browse Mode")
            self.curDict = self.activeSelectionAreas[self.curImg]
            self.loadImg()
            return

        # If we're in selection mode:
        if self.selectionMode:
            if self.saved:
                self.browseMode = True
                self.selectionMode = False
                self.imgSelect.setStyleSheet("border: 2px solid black;")
                self.btnChangeMode.setText("Selection Mode")
                self.selectedPads = []
                self.loadImg()
                return
            else:
                # Open confirm window
                self.confirmWindow = ConfirmWindow(self)
                self.confirmWindow.show()

    def loadImg(self):
        # Load name.jpg into QGraphicsView imgSelect
        imgPixmap = QtGui.QPixmap(
            'imgs/' + self.curImg + '.jpg', "1")  # Why 1??

        # Get dims of pixmap
        w = imgPixmap.width()
        h = imgPixmap.height()
        self.pixmapDims = (w, h)

        # Scale the image by the zoom
        zoom = self.zoomScale
        imgPixmap = imgPixmap.scaled(w*zoom, h*zoom)

        # Get dims of the qLabel
        imgSelectWidth = self.imgSelect.width()
        imgSelectHeight = self.imgSelect.height()

        #Build a scene for the graphics view
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addPixmap(imgPixmap)
        self.imgSelect.setScene(self.scene)

        self.findScaleAndOffset()

        self.drawBoxes()
        print(self.imgSelect.width(), self.imgSelect.height())


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
    form = WirebondRecorder()  # We set the form to be our WelcomeWindow
    form.show()  # Show the form
    sys.exit(app.exec_())  # and execute the app

if __name__ == '__main__':  # if we're running file directly and not importing it
    displayGui()  # run the main function
