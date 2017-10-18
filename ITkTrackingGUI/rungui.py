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
		self.sceneRect = QtCore.QRectF(0,0,0,0)
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
								["R1", [(373, 38), (591, 39),
										(587, 224), (378, 222)]],
								["R2", [(0, 0), (0, 0), (0, 0), (0, 0)]],
								["R3", [(0, 0), (0, 0), (0, 0), (0, 0)]],
								["R4", [(0, 0), (0, 0), (0, 0), (0, 0)]],
								["R5", [(0, 0), (0, 0), (0, 0), (0, 0)]]])
		activeAreasR0 = {"R0H1": [(59.0,168.0), (443.0,167.0), (446.0,246.0), (65.0,251.0)],
						 "R0H0": [(70.0,290.0), (436.0,296.0), (431.0,372.0), (77.0,373.0)]}
		activeAreasR0H0 = {"ASIC": [(0, 0), (0, 0), (0, 0), (0, 0)]}
		activeAreasR0H1 = {
			"ASIC": [(27, 38), (88, 33), (88, 79), (33, 82)]}
		activeAreasASIC = {"pad1": [(0, 0), (0, 0), (0, 0), (0, 0)]}  # etc?

		# Here we store the valid selection areas (i.e. bond pads)
		#  give a rough area and assume all are square, so we
		#  can just pass a single point and build the box while
		#  we check the location of the click
		activeSelectionAreasASIC = {"1": (694.0, 294.0),
									"2": (715.0, 294.0),
									"3": (755.0, 290.0),
									"4": (783.0, 296.0),
									"5": (814.0, 289.0),
									"6": (837.0, 286.0),
									"7": (894.0, 288.0),
									"8": (915.0, 288.0),
									"9": (934.0, 288.0),
									"10": (956.0, 287.0),
									"11": (979.0, 289.0),
									"12": (997.0, 288.0),
									"13": (1020.0, 288.0),
									"14": (1039.0, 286.0),
									"15": (1056.0, 288.0),
									"16": (1078.0, 286.0),
									"17": (1103.0, 286.0),
									"18": (1123.0, 287.0),
									"19": (1144.0, 286.0),
									"20": (1162.0, 285.0),
									"21": (1183.0, 286.0)}

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
			self.imgSelect.fitInView(self.imgSelect.sceneRect(), QtCore.Qt.KeepAspectRatio)
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
		if len(self.selectedPads) == 0:
			print("Can't save")
			return
		print(self.level)
		print(self.selectedPads)

		# Save as a .txt file here
		txtFile = open(self.serial + ".txt",'w')
		txtFile.write(str(self.level))
		txtFile.write(str(self.selectedPads))
		txtFile.close()

		self.saved = True

	# Back button functionality
	def levelUp(self):
		# Check we aren't at root and are in browse mode
		if self.level[-1] != "root" and self.browseMode:
			self.level.pop(-1)
			name = self.level[-1]

			self.curImg = name			
			self.loadImg()
			self.changeZoom(self.zoomScale)

	# If the image is clicked, run checks
	def executeSelection(self, ev):
		# Grab click location
		pt = ev.pos()
		scenePt = self.imgSelect.mapToScene(pt)

		x = scenePt.x()
		y = scenePt.y()

		self.counter += 1
		#print('"' + str(self.counter)+'"' + ' : (' + str(x) + ',' + str(y) +'),')  # DEBUG
		#print('(' + str(x) + ',' + str(y) + ')')

		# Store scene rect
		topLeftPt = -1.*self.imgSelect.mapFromScene(0,0)
		self.sceneRect = QtCore.QRectF(topLeftPt.x(),topLeftPt.y(),0,0)
		
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
		else:
			self.selectedPads.append(name)

		# Make sure we save the top left pos before loading
		self.sceneTopLeft = self.imgSelect.mapFromScene(0,0)
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

			# Now we need to get the serial number for the part we are marking.
			# The serial number should be the primary key in the DB we will upload
			# results to
			if self.serial == '':
				self.serial = self.getSerialFromUser()
				self.lblmainTitle.setText(self.serial)
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
		validSerials = ['1234','1111']

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
		imgPixmap = QtGui.QPixmap(
			'ITkTrackingGUI/imgs/' + self.curImg + '.jpg', "1")  # Why 1??

		# Scale the image by the zoom
		zoom = self.zoomScale

		# Build a scene for the graphics view
		self.scene = QtWidgets.QGraphicsScene(self)
		self.scene.addPixmap(imgPixmap)
		self.imgSelect.setScene(self.scene)

		self.drawBoxes()

			



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
