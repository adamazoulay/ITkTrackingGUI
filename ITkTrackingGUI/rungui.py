from PyQt5 import QtGui, QtWidgets, QtCore  # Import the PyQt5 module we'll need
import sys
import os  # We need sys so that we can pass argv to QApplication
import matplotlib.path as mplPath
import numpy as np

from WirebondRecorderGUI import Ui_WirebondRecorder
from ConfirmWindowGUI import Ui_ConfirmWindow

# Import the config file
import config
from selectionAreas import *


# ================================================================================
# TODO:
#  - Add database uploading
#  - Separate mark locations to different file
#  - Finish config file and header information for save file
# ================================================================================

# Define the classes for the main gui
class WirebondRecorder(QtWidgets.QMainWindow, Ui_WirebondRecorder):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in WirebondRecorderGUI.py file automatically
        # It sets up layout and widgets that are defined

        # Start global variables
        self.level = ['root']
        self.selectionMode = False
        self.browseMode = True
        self.curImg = "root"
        self.selectedPads = []
        self.markedPads = []
        self.comments = {}
        self.compPass = True
        self.counter = -4
        self.curDict = {}
        self.saved = True
        self.sceneRect = QtCore.QRectF(0, 0, 0, 0)
        self.serial = ''

        # Scale and offset values, for resize and adjust (need to change on
        # every resize and zoom)
        self.zoomScale = 0

        # Pad size scale (need to adjust for zooming stuff)
        self.size = 10

        # Start maximized and resized
        self.showMaximized()
        self.imgSelect.setStyleSheet("border: 2px solid black;")

        # Need to store all active areas for each level
        activeAreasRoot = {"endcap": [(0.0, -13.0), (600, -16.0), (600, 442.0), (0.0, 429.0)],
                           "barrel": [(1.0, 481.0), (592.0, 480.0), (592.0, 923.0), (0.0, 923.0)]}
        activeAreasEndcap = {"R0": [(96, 28), (263, 30), (257, 219), (93, 223)],
                             "R1": [(0, 0), (0, 0), (0, 0), (0, 0)],
                             "R2": [(0, 0), (0, 0), (0, 0), (0, 0)],
                             "R3": [(0, 0), (0, 0), (0, 0), (0, 0)],
                             "R4": [(0, 0), (0, 0), (0, 0), (0, 0)],
                             "R5": [(0, 0), (0, 0), (0, 0), (0, 0)]}
        activeAreasR0 = {"R0H1": [(108.0, 567.0), (1437.0, 571.0), (1422.0, 819.0), (138.0, 847.0)],
                         "R0H0": [(152.0, 978.0), (1399.0, 1033.0), (1382.0, 1273.0), (185.0, 1263.0)]}
        activeAreasR0H0 = {"HCC": [(272.0, 138.0), (418.0, 126.0), (422.0, 213.0), (282.0, 224.0)],
                           "ASICd1": [(104.0, 419.0), (340.0, 402.0), (356.0, 612.0), (119.0, 630.0)],
                           "ASICd2": [(404.0, 397.0), (638.0, 387.0), (653.0, 600.0), (414.0, 613.0)],
                           "ASICd3": [(704.0, 383.0), (940.0, 377.0), (947.0, 592.0), (711.0, 597.0)],
                           "ASICd4": [(1007.0, 378.0), (1240.0, 379.0), (1244.0, 589.0), (1008.0, 592.0)],
                           "ASICd5": [(1308.0, 378.0), (1540.0, 387.0), (1535.0, 587.0), (1302.0, 585.0)],
                           "ASICd6": [(1606.0, 384.0), (1846.0, 391.0), (1831.0, 604.0), (1596.0, 596.0)],
                           "ASICd7": [(1907.0, 397.0), (2138.0, 413.0), (2127.0, 627.0), (1891.0, 612.0)],
                           "ASICd8": [(2201.0, 416.0), (2438.0, 441.0), (2418.0, 643.0), (2185.0, 625.0)]}
        activeAreasR0H1 = {"HCC": [(304.0, 496.0), (452.0, 488.0), (459.0, 576.0), (321.0, 587.0)],
                           "ASICu1": [(79.0, 132.0), (332.0, 102.0), (336.0, 325.0), (97.0, 333.0)],
                           "ASICu2": [(370.0, 104.0), (609.0, 87.0), (624.0, 308.0), (384.0, 314.0)],
                           "ASICu3": [(659.0, 91.0), (904.0, 79.0), (910.0, 288.0), (672.0, 295.0)],
                           "ASICu4": [(955.0, 77.0), (1194.0, 70.0), (1198.0, 280.0), (960.0, 284.0)],
                           "ASICu5": [(1245.0, 74.0), (1487.0, 79.0), (1486.0, 282.0), (1247.0, 281.0)],
                           "ASICu6": [(1540.0, 73.0), (1778.0, 79.0), (1776.0, 289.0), (1536.0, 282.0)],
                           "ASICu7": [(1834.0, 84.0), (2075.0, 96.0), (2064.0, 303.0), (1826.0, 291.0)],
                           "ASICu8": [(2126.0, 95.0), (2368.0, 116.0), (2352.0, 323.0), (2116.0, 309.0)],
                           "ASICu9": [(2416.0, 117.0), (2655.0, 143.0), (2638.0, 351.0), (2403.0, 327.0)]}
        activeAreasBarrel = {"LH": [(178.6, 508.9), (1657.8, 512.9), (1659.2, 741.6), (177.3, 744.3)],
                             "RH": [(182.7, 923.0), (1657.8, 913.5), (1660.5, 1127.3), (189.5, 1131.4)]}
        activeAreasLH = {"HCC": [(228.2, 495.6), (372.0, 496.8), (369.6, 575.3), (230.6, 574.1)],
                         "ASICu1": [(29.7, 159.3), (276.9, 164.0), (279.3, 332.8), (28.5, 331.6)],
                         "ASICu2": [(318.5, 161.6), (566.9, 158.1), (570.5, 334.0), (324.5, 332.8)],
                         "ASICu3": [(609.7, 156.9), (856.9, 161.6), (856.9, 334.0), (615.7, 329.2)],
                         "ASICu4": [(899.7, 158.1), (1147.0, 158.1), (1150.5, 334.0), (902.1, 325.7)],
                         "ASICu5": [(1193.3, 153.3), (1440.5, 156.9), (1439.3, 337.5), (1196.9, 329.2)],
                         "ASICu6": [(1484.5, 159.3), (1728.2, 156.9), (1727.0, 329.2), (1482.1, 335.2)],
                         "ASICu7": [(1778.1, 155.7), (2017.0, 156.9), (2013.4, 335.2), (1780.4, 334.0)],
                         "ASICu8": [(2066.9, 160.5), (2307.0, 158.1), (2311.7, 337.5), (2074.0, 330.4)],
                         "ASICu9": [(2360.5, 154.5), (2595.8, 155.7), (2600.5, 332.8), (2360.5, 324.5)]}
        activeAreasRH = {}
        activeAreasASIC = {}
        activeAreasHCC = {}

        activeSelectionAreasR0H1 = {}

        self.activeAreas = {"root": activeAreasRoot, "endcap": activeAreasEndcap, "R0": activeAreasR0,
                            "R0H0": activeAreasR0H0, "R0H1": activeAreasR0H1,
                            "ASICu1": activeAreasASIC, "ASICu2": activeAreasASIC, "ASICu3": activeAreasASIC,
                            "ASICu4": activeAreasASIC, "ASICu5": activeAreasASIC, "ASICu6": activeAreasASIC,
                            "ASICu7": activeAreasASIC, "ASICu8": activeAreasASIC, "ASICu9": activeAreasASIC,
                            "ASICd1": activeAreasASIC, "ASICd2": activeAreasASIC, "ASICd3": activeAreasASIC,
                            "ASICd4": activeAreasASIC, "ASICd5": activeAreasASIC, "ASICd6": activeAreasASIC,
                            "ASICd7": activeAreasASIC, "ASICd8": activeAreasASIC,
                            "HCC": activeAreasHCC, "barrel": activeAreasBarrel, "LH": activeAreasLH,
                            "RH": activeAreasRH}

        self.activeSelectionAreas = {
            "R0H1": activeSelectionAreasR0H1, "HCC": activeSelectionAreasHCC,
            "ASICu1": activeSelectionAreasASICu, "ASICu2": activeSelectionAreasASICu,
            "ASICu3": activeSelectionAreasASICu, "ASICu4": activeSelectionAreasASICu,
            "ASICu5": activeSelectionAreasASICu, "ASICu6": activeSelectionAreasASICu,
            "ASICu7": activeSelectionAreasASICu, "ASICu8": activeSelectionAreasASICu,
            "ASICu9": activeSelectionAreasASICu,
            "ASICd1": activeSelectionAreasASICd, "ASICd2": activeSelectionAreasASICd,
            "ASICd3": activeSelectionAreasASICd, "ASICd4": activeSelectionAreasASICd,
            "ASICd5": activeSelectionAreasASICd, "ASICd6": activeSelectionAreasASICd,
            "ASICd7": activeSelectionAreasASICd, "ASICd8": activeSelectionAreasASICd}

        # If module is selected by picture, change the module list
        self.imgSelect.mousePressEvent = self.executeSelection

        # Back button
        self.btnBack.clicked.connect(self.levelUp)

        # Change mode button
        self.btnChangeMode.clicked.connect(self.changeMode)

        # Save button
        self.btnSave.clicked.connect(self.saveSelection)

        # Zoom slider change
        self.sldrZoom.valueChanged.connect(self.changeZoom)

        # Load the initial module selection and selection areas
        self.curDict = self.activeAreas[self.curImg]
        self.imgSelect.setAlignment(QtCore.Qt.AlignCenter)
        # Initialize scene and load image
        self.scene = QtWidgets.QGraphicsScene(self)
        self.loadImg()

        # Exit menu item
        self.actionExit.triggered.connect(self.close)

    # shortcutExit = QtWidgets.QShortcut(QtGui.QKeySequence(self.tr("Ctrl+E", "File|Exit")), self.parent)

    # If zoom is changed let's update the image
    def changeZoom(self, value):
        if value == 1:
            zoom = 1
        elif value > 1:
            zoom = 1 + (value - 1) / 5.
        else:
            self.imgSelect.fitInView(
                self.imgSelect.sceneRect(), QtCore.Qt.KeepAspectRatio)
            self.lblZoom.setText("Fit")
            self.zoomScale = 0
            self.loadImg()
            return

        self.zoomScale = value
        self.lblZoom.setText(str(zoom) + 'x')

        # Reset zoom and rescale
        self.imgSelect.setTransform(QtGui.QTransform())
        self.imgSelect.scale(zoom, zoom)
        self.loadImg()

    # Save any information about the selected pads
    def saveSelection(self):
        # Append the currently selected pads to the specific serial number file
        fileName = self.serial + ".areas"

        self.updateAreas(fileName)
        self.saved = True
        self.logText.append("Saved to '" + fileName + "'")

        self.loadImg()

    # Function for adding the currently selected areas to the .areas save file
    def updateAreas(self, fileName):
        # Transfer pads to marked list
        for pad in self.selectedPads:
            if pad not in self.markedPads:
                self.markedPads.append(pad)
                # Here we combine the comment from the error category box to the written comment
                self.comments[pad] = str(self.errorCategory.currentText()) + " : " + self.commentBox.toPlainText()
            else:
                self.markedPads.remove(pad)
                self.comments[pad] = ""

        self.commentBox.setText("")
        self.selectedPads = []

        # Open the file (Should be in program directory for now)
        areasFile = open(fileName, 'r+')
        # Read in the dict form the file
        curFile = eval(areasFile.read())

        # Wipe the file now that we've read itself.commentBox.text
        areasFile.seek(0, 0)
        areasFile.truncate()

        # Set the entry in the save file as the currently selected pads
        curFile[tuple(self.level)] = (self.markedPads, self.comments)

        areasFile.write(str(curFile))
        areasFile.close()

    # Back button functionality
    def levelUp(self):
        # Check we aren't at root and are in browse mode
        if self.level[-1] != "root" and self.browseMode:
            self.level.pop(-1)
            self.curImg = self.level[-1]
            self.loadImg()
            self.changeZoom(self.zoomScale)

            # Record to log
            self.logText.append("Changed to " + self.curImg)

    # If the image is clicked, run checks
    def executeSelection(self, ev):
        # Grab click location
        pt = ev.pos()
        scenePt = self.imgSelect.mapToScene(pt)

        x = scenePt.x()
        y = scenePt.y()

        self.counter += 1
        # print('"' + str(self.counter)+'"' + ' : (' + str(x) + ',' + str(y) +'),', end='', flush=True)  # DEBUG
        print('({:.1f},{:.1f}), '.format(x, y), end='', flush=True)

        # Store scene rect
        topLeftPt = -1. * self.imgSelect.mapFromScene(0, 0)
        self.sceneRect = QtCore.QRectF(topLeftPt.x(), topLeftPt.y(), 0, 0)

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
                self.changeZoom(self.zoomScale)

                self.logText.append("Changed to " + self.curImg)

            if inside and self.selectionMode:
                # Mark the pad list as unsaved
                self.saved = False
                # Display box around selected pad
                self.manageBoxes(name, size)

                # Update comment box
                if name in self.markedPads:
                    self.commentBox.setText(self.comments[name])
                else:
                    self.commentBox.setText("")

    def drawBoxes(self):
        size = self.size
        # Set pen colour
        Qred = QtGui.QColor(255, 0, 0)
        Qblue = QtGui.QColor(0, 0, 255)
        Qabitred = QtGui.QColor(255, 0, 0, 50)
        QEmpty = QtGui.QColor(0, 0, 0, 0)

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

                rect = QtCore.QRectF(xVal - size, yVal - size, 2 * size, 2 * size)

                # if selected, fill in rect
                if (area in self.markedPads) and (area in self.selectedPads):
                    self.scene.addRect(rect, Qred, Qblue)
                elif area in self.markedPads:
                    self.scene.addRect(rect, Qblue, Qblue)
                elif area in self.selectedPads:
                    self.scene.addRect(rect, Qblue, Qabitred)
                else:
                    self.scene.addRect(rect, Qred, Qabitred)  # Last arg gives the fill colour

            if self.browseMode:
                # Draw hollow rect
                # Get top right and bottom left coords of area
                coords = tempDict[area]
                xValTop = coords[0][0]
                yValTop = coords[0][1]
                xValBot = coords[2][0]
                yValBot = coords[2][1]

                width = abs(xValBot - xValTop)
                height = abs(yValBot - yValTop)

                rect = QtCore.QRectF(xValTop, yValTop, width, height)
                self.scene.addRect(rect, Qred, Qabitred)

    def manageBoxes(self, name, size):
        # First add the pad to the array
        if name in self.selectedPads:
            self.selectedPads.remove(name)
            self.logText.append("Deselected pad " + name)
        else:
            self.selectedPads.append(name)
            self.logText.append("Selected pad " + name)

        # Make sure we save the top left pos before loading
        self.sceneTopLeft = self.imgSelect.mapFromScene(0, 0)
        self.loadImg()

    def changeMode(self):
        self.commentBox.setText("")
        # If we're in browse mode and have pads to select:
        if self.browseMode and (self.level[-1] in self.activeSelectionAreas):
            self.browseMode = False
            self.selectionMode = True
            self.imgSelect.setStyleSheet("border: 2px solid red;")
            self.btnChangeMode.setText("Browse")
            self.curDict = self.activeSelectionAreas[self.curImg]

            # Make/open save
            self.initSave()

            self.loadImg()
            return

        # If we're in selection mode:
        if self.selectionMode:
            if self.saved:
                self.browseMode = True
                self.selectionMode = False
                self.imgSelect.setStyleSheet("border: 2px solid black;")
                self.btnChangeMode.setText("Edit")
                self.selectedPads = []
                self.loadImg()
                return
            else:
                # Open confirm window
                self.confirmWindow = ConfirmWindow(self)
                self.confirmWindow.show()

    def getSerialFromUser(self):
        # Eventually, have list of valid keys and check to make sure
        #  it's valid
        validSerials = ['1234', '1111']

        serial, ok = QtWidgets.QInputDialog.getText(self, 'Serial number',
                                                    'Please enter the serial number of the component:')

        # Debugging
        validSerials.append(serial)

        if not ok:
            return

        while serial not in validSerials:
            print(serial)
            serial, ok = QtWidgets.QInputDialog.getText(self, 'Serial number',
                                                        'Invalid serial. Please enter a valid serial number:')
            if not ok:
                return

        return serial

    def loadImg(self):
        # Load name.jpg into QGraphicsView imgSelect
        curDir = os.path.dirname(os.path.abspath(__file__))
        # Account for ASICs
        if self.curImg[:5] == "ASICu":
            curImgTemp = "ASICu"
        elif self.curImg[:5] == "ASICd":
            curImgTemp = "ASICd"
        else:
            curImgTemp = self.curImg

        imgPath = os.path.join(curDir, 'imgs', (curImgTemp + '.jpg'))
        imgPixmap = QtGui.QPixmap(imgPath, "1")  # Why 1??

        # Scale the image by the zoom
        zoom = self.zoomScale

        # Build a scene for the graphics view
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addPixmap(imgPixmap)
        self.imgSelect.setScene(self.scene)

        self.drawBoxes()

    def initSave(self):
        self.serial = self.getSerialFromUser()
        # self.lblmainTitle.setText(self.serial)

        # Append to curent level
        self.serial = self.serial + "." + self.level[-1]

        self.logText.append("Serial set: " + self.serial)

        # Create empty file (Change this later)
        if not (os.path.isfile(self.serial + ".areas")):
            file = open(self.serial + ".areas", 'w')
            file.write("{}")
            file.close()
            self.logText.append("Created selection file at '" + self.serial + ".areas'")
        # If it's in the path, load the pads if the exist
        else:
            # Open the file (Should be in program directory for now)
            areasFile = open(self.serial + ".areas", 'r+')
            # Read in the dict form the file
            curFile = eval(areasFile.read())

            for levels in curFile:
                if levels[-1] == self.level[-1]:
                    self.markedPads = curFile[tuple(levels)][0]
                    self.comments = curFile[tuple(levels)][1]
                    self.logText.append("Loaded selection from file '" + self.serial + ".areas'")

            areasFile.close()


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
