from PyQt5 import QtGui, QtWidgets, QtCore  # Import the PyQt5 module we'll need
import sys
import os  # We need sys so that we can pass argv to QApplication
import matplotlib.path as mplPath
import numpy as np

from WirebondRecorderGUI import Ui_WirebondRecorder
from ConfirmWindowGUI import Ui_ConfirmWindow

# ================================================================================
# TODO:
#  Figure out pad selection saving. - note: change serial back to title after save
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
		self.counter = -3
		self.curDict = {}
		self.saved = True
		self.sceneRect = QtCore.QRectF(0, 0, 0, 0)
		self.serial = ''

		# Scale and offset values, for resize and adjust (need to change on
		# every resize and zoom)
		self.zoomScale = 1

		# Pad size scale (need to adjust for zooming stuff)
		self.size = 10

		# Start maximized and resized
		self.showMaximized()
		self.imgSelect.setStyleSheet("border: 2px solid black;")

		# Need to store all active areas for each level
		activeAreasRoot = dict([["R0", [(96, 28), (263, 30), (257, 219), (93, 223)]],
								["R1", [(0, 0), (0, 0), (0, 0), (0, 0)]],
								["R2", [(0, 0), (0, 0), (0, 0), (0, 0)]],
								["R3", [(0, 0), (0, 0), (0, 0), (0, 0)]],
								["R4", [(0, 0), (0, 0), (0, 0), (0, 0)]],
								["R5", [(0, 0), (0, 0), (0, 0), (0, 0)]]])
		activeAreasR0 = {"R0H1": [(59.0, 168.0), (443.0, 167.0), (446.0, 246.0), (65.0, 251.0)],
						 "R0H0": [(70.0, 290.0), (436.0, 296.0), (431.0, 372.0), (77.0, 373.0)]}
		activeAreasR0H0 = {"ASICd": [(0, 0), (0, 0), (0, 0), (0, 0)]}
		activeAreasR0H1 = {"ASICu1": [(27, 38), (88, 33), (88, 79), (33, 82)], "ASICu2": [(98.0,40.0), (154.0,39.0), (155.0,73.0), (101.0,77.0)], "ASICu3": [(166.0,33.0), (220.0,30.0), (219.0,66.0), (170.0,67.0)], "ASICu4": [(235.0,32.0), (286.0,32.0), (288.0,65.0), (239.0,68.0)], "ASICu5": [(299.0,29.0), (354.0,30.0), (356.0,67.0), (299.0,65.0)], "ASICu6": [(366.0,29.0), (424.0,29.0), (420.0,68.0), (371.0,69.0)], "ASICu7": [(434.0,30.0), (494.0,31.0), (490.0,69.0), (436.0,69.0)], "ASICu8": [(502.0,33.0), (560.0,36.0), (556.0,75.0), (499.0,71.0)], "ASICu9": [(570.0,37.0), (624.0,42.0), (622.0,71.0), (569.0,71.0)]}
		activeAreasASIC = {"pad1": [(0, 0), (0, 0), (0, 0), (0, 0)]}  # etc?

		# Here we store the valid selection areas (i.e. bond pads)
		#  give a rough area and assume all are square, so we
		#  can just pass a single point and build the box while
		#  we check the location of the click
		#  TODO: THINK OF BETTER WAY TO STORE THESE. SEPERATE FILE?
		activeSelectionAreasASICu = {'1': (1743.0,205.0), '2': (1756.0,270.0), '3': (1745.0,336.0), '4': (1756.0,399.0), '5': (1698.0, 1382.0), '6': (1662.0, 1380.0), '7': (1640.0, 1382.0), '8': (1618.0, 1379.0), '9': (1580.0, 1382.0), '10': (1562.0, 1381.0), '11': (1481.0, 1383.0), '12': (1402.0, 1383.0), '13': (1385.0, 1382.0), '14': (1362.0, 1380.0), '15': (1341.0, 1384.0), '16': (1320.0, 1382.0), '17': (1298.0, 1382.0), '18': (1278.0, 1382.0), '19': (1256.0, 1384.0), '20': (1239.0, 1386.0), '21': (1213.0, 1384.0), '22': (1197.0, 1384.0), '23': (1175.0, 1385.0), '24': (1153.0, 1386.0), '25': (1131.0, 1385.0), '26': (1111.0, 1384.0), '27': (1089.0, 1385.0), '28': (1071.0, 1386.0), '29': (1048.0, 1387.0), '30': (1028.0, 1383.0), '31': (1005.0, 1386.0), '32': (983.0, 1389.0), '33': (965.0, 1385.0), '34': (943.0, 1387.0), '35': (925.0, 1387.0), '36': (902.0, 1388.0), '37': (881.0, 1388.0), '38': (858.0, 1390.0), '39': (831.0, 1386.0), '40': (810.0, 1387.0), '41': (787.0, 1388.0), '42': (769.0, 1385.0), '43': (748.0, 1386.0), '44': (733.0, 1386.0), '45': (707.0, 1386.0), '46': (686.0, 1387.0), '47': (668.0, 1385.0), '48': (644.0, 1386.0), '49': (620.0, 1387.0), '50': (601.0, 1388.0), '51': (583.0, 1387.0), '52': (564.0, 1387.0), '53': (525.0, 1383.0), '54': (505.0, 1385.0), '55': (483.0, 1387.0), '56': (446.0, 1387.0), '57': (423.0, 1387.0), '58': (402.0, 1388.0), '59': (362.0, 1388.0), '60': (318.0, 1319.0), '61': (318.0, 1283.0), '62': (321.0, 1244.0), '63': (319.0, 1206.0), '64': (318.0, 1158.0), '65': (315.0, 1124.0), '66': (316.0, 1074.0), '67': (315.0, 1028.0), '68': (314.0, 988.0), '69': (318.0, 945.0), '70': (317.0, 899.0), '71': (314.0, 864.0), '72': (317.0, 811.0), '73': (318.0, 767.0), '74': (316.0, 729.0), '75': (312.0,405.0), '76': (298.0,335.0), '77': (311.0,275.0), '78': (298.0,209.0)}

		activeSelectionAreasASICd = {"1": (694.0, 294.0)}

		activeSelectionAreasR0H1 = {"PWR": (10, 65)}

		self.activeAreas = {"root": activeAreasRoot, "R0": activeAreasR0,
							"R0H0": activeAreasR0H0, "R0H1": activeAreasR0H1,
							"ASICu1": activeAreasASIC, "ASICu2": activeAreasASIC, "ASICu3": activeAreasASIC, "ASICu4": activeAreasASIC, "ASICu5": activeAreasASIC, "ASICu6": activeAreasASIC, "ASICu7": activeAreasASIC, "ASICu8": activeAreasASIC, "ASICu9": activeAreasASIC, "ASICd": activeAreasASIC}

		self.activeSelectionAreas = {
			"R0H1": activeSelectionAreasR0H1, "ASICu1": activeSelectionAreasASICu, "ASICu2": activeSelectionAreasASICu, "ASICu3": activeSelectionAreasASICu, "ASICu4": activeSelectionAreasASICu, "ASICu5": activeSelectionAreasASICu, "ASICu6": activeSelectionAreasASICu, "ASICu7": activeSelectionAreasASICu, "ASICu8": activeSelectionAreasASICu, "ASICu9": activeSelectionAreasASICu,
			"ASICd": activeSelectionAreasASICd}

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
		# Initilize scene and load image
		self.scene = QtWidgets.QGraphicsScene(self)
		self.loadImg()

		# Exit menu item
		self.actionExit.triggered.connect(self.close)
		#shortcutExit = QtWidgets.QShortcut(QtGui.QKeySequence(self.tr("Ctrl+E", "File|Exit")), self.parent)

	# If zoom is changed let's update the image
	def changeZoom(self, value):
		if value == 1:
			zoom = 1
		elif value > 1:
			zoom = 1 + (value-1)/5.
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

	# Function for adding the currently selected areas to the .areas save file
	def updateAreas(self, fileName):

		# Open the file (Should be in program directory for now)
		areasFile = open(fileName, 'r+')
		# Read in the dict form the file
		curFile = eval(areasFile.read())

		# Wipe the file now that we've read it
		areasFile.seek(0, 0)
		areasFile.truncate()

		# Set the entry in the save file as the currently selected pads
		curFile[tuple(self.level)] = self.selectedPads

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
		# print('"' + str(self.counter)+'"' + ' : (' + str(x) + ',' + str(y) +'),')  # DEBUG
		print('(' + str(x) + ',' + str(y) + ')')

		# Store scene rect
		topLeftPt = -1.*self.imgSelect.mapFromScene(0, 0)
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
				# Mark the pas list as unsaved
				self.saved = False
				# Display box around selected pad
				self.manageBoxes(name, size)

	def drawBoxes(self):
		size = self.size
		# Set pen colour
		Qred = QtGui.QColor(255, 0, 0)
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

				rect = QtCore.QRectF(xVal-size, yVal-size, 2*size, 2*size)

				# if selected, fill in rect
				if area in self.selectedPads:
					self.scene.addRect(rect, Qred, Qred)
				else:
					# Just set alpha to 0 (probably a better way to do this.
					# there was!)
					self.scene.addRect(rect, Qred, QEmpty)

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
			self.logText.append("Removed pad " + name)
		else:
			self.selectedPads.append(name)
			self.logText.append("Added pad " + name)

		# Make sure we save the top left pos before loading
		self.sceneTopLeft = self.imgSelect.mapFromScene(0, 0)
		self.loadImg()

	def changeMode(self):
		# If we're in browse mode and have pads to select:
		if self.browseMode and (self.level[-1] in self.activeSelectionAreas):
			self.browseMode = False
			self.selectionMode = True
			self.imgSelect.setStyleSheet("border: 2px solid red;")
			self.btnChangeMode.setText("Browse Mode")
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
				self.btnChangeMode.setText("Selection Mode")
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

		#Append to curent level
		self.serial = self.level[-1] + '.' + self.serial

		self.logText.append("Serial set: " + self.serial)

		# Create empty file (Change this later)
		if not(os.path.isfile(self.serial + ".areas")):
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
					self.selectedPads = curFile[tuple(levels)]
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
