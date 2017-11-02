from PyQt5 import QtGui, QtWidgets, QtCore  # Import the PyQt5 module we'll need
import sys
import os  # We need sys so that we can pass argv to QApplication
import matplotlib.path as mplPath
import numpy as np

from WirebondRecorderGUI import Ui_WirebondRecorder
from ConfirmWindowGUI import Ui_ConfirmWindow

# ================================================================================
# TODO:
#  Just lots of things
# ================================================================================

# Define the classes for the main gui
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
		activeAreasRoot = {"endcap": [(0.0,-13.0), (707.0,-16.0), (680.0,442.0), (0.0,429.0)], "barrel": [(0, 0), (0, 0), (0, 0), (0, 0)]}
		activeAreasEndcap = dict([["R0", [(96, 28), (263, 30), (257, 219), (93, 223)]],
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
		activeSelectionAreasASICu = {'1': (1743.0,205.0), '2': (1756.0,270.0), '3': (1745.0,336.0), '4': (1756.0,399.0), '5': (1698.0, 1382.0), '6': (1662.0, 1380.0), '7': (1640.0, 1382.0), '8': (1618.0, 1379.0), '9': (1580.0, 1382.0), '10': (1562.0, 1381.0), '11': (1481.0, 1383.0), '12': (1402.0, 1383.0), '13': (1385.0, 1382.0), '14': (1362.0, 1380.0), '15': (1341.0, 1384.0), '16': (1320.0, 1382.0), '17': (1298.0, 1382.0), '18': (1278.0, 1382.0), '19': (1256.0, 1384.0), '20': (1239.0, 1386.0), '21': (1213.0, 1384.0), '22': (1197.0, 1384.0), '23': (1175.0, 1385.0), '24': (1153.0, 1386.0), '25': (1131.0, 1385.0), '26': (1111.0, 1384.0), '27': (1089.0, 1385.0), '28': (1071.0, 1386.0), '29': (1048.0, 1387.0), '30': (1028.0, 1383.0), '31': (1005.0, 1386.0), '32': (983.0, 1389.0), '33': (965.0, 1385.0), '34': (943.0, 1387.0), '35': (925.0, 1387.0), '36': (902.0, 1388.0), '37': (881.0, 1388.0), '38': (858.0, 1390.0), '39': (831.0, 1386.0), '40': (810.0, 1387.0), '41': (787.0, 1388.0), '42': (769.0, 1385.0), '43': (748.0, 1386.0), '44': (733.0, 1386.0), '45': (707.0, 1386.0), '46': (686.0, 1387.0), '47': (668.0, 1385.0), '48': (644.0, 1386.0), '49': (620.0, 1387.0), '50': (601.0, 1388.0), '51': (583.0, 1387.0), '52': (564.0, 1387.0), '53': (525.0, 1383.0), '54': (505.0, 1385.0), '55': (483.0, 1387.0), '56': (446.0, 1387.0), '57': (423.0, 1387.0), '58': (402.0, 1388.0), '59': (362.0, 1388.0), '60': (318.0, 1319.0), '61': (318.0, 1283.0), '62': (321.0, 1244.0), '63': (319.0, 1206.0), '64': (318.0, 1158.0), '65': (315.0, 1124.0), '66': (316.0, 1074.0), '67': (315.0, 1028.0), '68': (314.0, 988.0), '69': (318.0, 945.0), '70': (317.0, 899.0), '71': (314.0, 864.0), '72': (317.0, 811.0), '73': (318.0, 767.0), '74': (316.0, 729.0), '75': (312.0,405.0), '76': (298.0,335.0), '77': (311.0,275.0), '78': (298.0,209.0),'s1': (322.0, 207.0), 's2': (344.207, 207.0), 's3': (366.414, 207.0), 's4': (388.621, 207.0), 's5': (410.828, 207.0), 's6': (433.03499999999997, 207.0), 's7': (455.242, 207.0), 's8': (477.449, 207.0), 's9': (499.656, 207.0), 's10': (521.863, 207.0), 's11': (544.0699999999999, 207.0), 's12': (566.277, 207.0), 's13': (588.484, 207.0), 's14': (610.691, 207.0), 's15': (632.898, 207.0), 's16': (655.105, 207.0), 's17': (677.312, 207.0), 's18': (699.519, 207.0), 's19': (721.726, 207.0), 's20': (743.933, 207.0), 's21': (766.14, 207.0), 's22': (788.347, 207.0), 's23': (810.5540000000001, 207.0), 's24': (832.761, 207.0), 's25': (854.9680000000001, 207.0), 's26': (877.1750000000001, 207.0), 's27': (899.3820000000001, 207.0), 's28': (921.589, 207.0), 's29': (943.796, 207.0), 's30': (966.003, 207.0), 's31': (988.21, 207.0), 's32': (1010.417, 207.0), 's33': (1032.624, 207.0), 's34': (1054.8310000000001, 207.0), 's35': (1077.038, 207.0), 's36': (1099.245, 207.0), 's37': (1121.452, 207.0), 's38': (1143.659, 207.0), 's39': (1165.866, 207.0), 's40': (1188.0729999999999, 207.0), 's41': (1210.28, 207.0), 's42': (1232.487, 207.0), 's43': (1254.694, 207.0), 's44': (1276.901, 207.0), 's45': (1299.1080000000002, 207.0), 's46': (1321.315, 207.0), 's47': (1343.522, 207.0), 's48': (1365.729, 207.0), 's49': (1387.9360000000001, 207.0), 's50': (1410.143, 207.0), 's51': (1432.3500000000001, 207.0), 's52': (1454.557, 207.0), 's53': (1476.7640000000001, 207.0), 's54': (1498.971, 207.0), 's55': (1521.178, 207.0), 's56': (1543.385, 207.0), 's57': (1565.592, 207.0), 's58': (1587.799, 207.0), 's59': (1610.006, 207.0), 's60': (1632.213, 207.0), 's61': (1654.42, 207.0), 's62': (1676.627, 207.0), 's63': (1698.834, 207.0), 's64': (1721.041, 207.0), 's65': (333.0, 274.0), 's66': (355.207, 274.0), 's67': (377.414, 274.0), 's68': (399.621, 274.0), 's69': (421.828, 274.0), 's70': (444.03499999999997, 274.0), 's71': (466.242, 274.0), 's72': (488.449, 274.0), 's73': (510.656, 274.0), 's74': (532.863, 274.0), 's75': (555.0699999999999, 274.0), 's76': (577.277, 274.0), 's77': (599.484, 274.0), 's78': (621.691, 274.0), 's79': (643.898, 274.0), 's80': (666.105, 274.0), 's81': (688.312, 274.0), 's82': (710.519, 274.0), 's83': (732.726, 274.0), 's84': (754.933, 274.0), 's85': (777.14, 274.0), 's86': (799.347, 274.0), 's87': (821.5540000000001, 274.0), 's88': (843.761, 274.0), 's89': (865.9680000000001, 274.0), 's90': (888.1750000000001, 274.0), 's91': (910.3820000000001, 274.0), 's92': (932.589, 274.0), 's93': (954.796, 274.0), 's94': (977.003, 274.0), 's95': (999.21, 274.0), 's96': (1021.417, 274.0), 's97': (1043.624, 274.0), 's98': (1065.8310000000001, 274.0), 's99': (1088.038, 274.0), 's100': (1110.245, 274.0), 's101': (1132.452, 274.0), 's102': (1154.659, 274.0), 's103': (1176.866, 274.0), 's104': (1199.0729999999999, 274.0), 's105': (1221.28, 274.0), 's106': (1243.487, 274.0), 's107': (1265.694, 274.0), 's108': (1287.901, 274.0), 's109': (1310.1080000000002, 274.0), 's110': (1332.315, 274.0), 's111': (1354.522, 274.0), 's112': (1376.729, 274.0), 's113': (1398.9360000000001, 274.0), 's114': (1421.143, 274.0), 's115': (1443.3500000000001, 274.0), 's116': (1465.557, 274.0), 's117': (1487.7640000000001, 274.0), 's118': (1509.971, 274.0), 's119': (1532.178, 274.0), 's120': (1554.385, 274.0), 's121': (1576.592, 274.0), 's122': (1598.799, 274.0), 's123': (1621.006, 274.0), 's124': (1643.213, 274.0), 's125': (1665.42, 274.0), 's126': (1687.627, 274.0), 's127': (1709.834, 274.0), 's128': (1732.041, 274.0), 's129': (322.0, 337.0), 's130': (344.207, 337.0), 's131': (366.414, 337.0), 's132': (388.621, 337.0), 's133': (410.828, 337.0), 's134': (433.03499999999997, 337.0), 's135': (455.242, 337.0), 's136': (477.449, 337.0), 's137': (499.656, 337.0), 's138': (521.863, 337.0), 's139': (544.0699999999999, 337.0), 's140': (566.277, 337.0), 's141': (588.484, 337.0), 's142': (610.691, 337.0), 's143': (632.898, 337.0), 's144': (655.105, 337.0), 's145': (677.312, 337.0), 's146': (699.519, 337.0), 's147': (721.726, 337.0), 's148': (743.933, 337.0), 's149': (766.14, 337.0), 's150': (788.347, 337.0), 's151': (810.5540000000001, 337.0), 's152': (832.761, 337.0), 's153': (854.9680000000001, 337.0), 's154': (877.1750000000001, 337.0), 's155': (899.3820000000001, 337.0), 's156': (921.589, 337.0), 's157': (943.796, 337.0), 's158': (966.003, 337.0), 's159': (988.21, 337.0), 's160': (1010.417, 337.0), 's161': (1032.624, 337.0), 's162': (1054.8310000000001, 337.0), 's163': (1077.038, 337.0), 's164': (1099.245, 337.0), 's165': (1121.452, 337.0), 's166': (1143.659, 337.0), 's167': (1165.866, 337.0), 's168': (1188.0729999999999, 337.0), 's169': (1210.28, 337.0), 's170': (1232.487, 337.0), 's171': (1254.694, 337.0), 's172': (1276.901, 337.0), 's173': (1299.1080000000002, 337.0), 's174': (1321.315, 337.0), 's175': (1343.522, 337.0), 's176': (1365.729, 337.0), 's177': (1387.9360000000001, 337.0), 's178': (1410.143, 337.0), 's179': (1432.3500000000001, 337.0), 's180': (1454.557, 337.0), 's181': (1476.7640000000001, 337.0), 's182': (1498.971, 337.0), 's183': (1521.178, 337.0), 's184': (1543.385, 337.0), 's185': (1565.592, 337.0), 's186': (1587.799, 337.0), 's187': (1610.006, 337.0), 's188': (1632.213, 337.0), 's189': (1654.42, 337.0), 's190': (1676.627, 337.0), 's191': (1698.834, 337.0), 's192': (1721.041, 337.0), 's193': (333.0, 405.0), 's194': (355.207, 405.0), 's195': (377.414, 405.0), 's196': (399.621, 405.0), 's197': (421.828, 405.0), 's198': (444.03499999999997, 405.0), 's199': (466.242, 405.0), 's200': (488.449, 405.0), 's201': (510.656, 405.0), 's202': (532.863, 405.0), 's203': (555.0699999999999, 405.0), 's204': (577.277, 405.0), 's205': (599.484, 405.0), 's206': (621.691, 405.0), 's207': (643.898, 405.0), 's208': (666.105, 405.0), 's209': (688.312, 405.0), 's210': (710.519, 405.0), 's211': (732.726, 405.0), 's212': (754.933, 405.0), 's213': (777.14, 405.0), 's214': (799.347, 405.0), 's215': (821.5540000000001, 405.0), 's216': (843.761, 405.0), 's217': (865.9680000000001, 405.0), 's218': (888.1750000000001, 405.0), 's219': (910.3820000000001, 405.0), 's220': (932.589, 405.0), 's221': (954.796, 405.0), 's222': (977.003, 405.0), 's223': (999.21, 405.0), 's224': (1021.417, 405.0), 's225': (1043.624, 405.0), 's226': (1065.8310000000001, 405.0), 's227': (1088.038, 405.0), 's228': (1110.245, 405.0), 's229': (1132.452, 405.0), 's230': (1154.659, 405.0), 's231': (1176.866, 405.0), 's232': (1199.0729999999999, 405.0), 's233': (1221.28, 405.0), 's234': (1243.487, 405.0), 's235': (1265.694, 405.0), 's236': (1287.901, 405.0), 's237': (1310.1080000000002, 405.0), 's238': (1332.315, 405.0), 's239': (1354.522, 405.0), 's240': (1376.729, 405.0), 's241': (1398.9360000000001, 405.0), 's242': (1421.143, 405.0), 's243': (1443.3500000000001, 405.0), 's244': (1465.557, 405.0), 's245': (1487.7640000000001, 405.0), 's246': (1509.971, 405.0), 's247': (1532.178, 405.0), 's248': (1554.385, 405.0), 's249': (1576.592, 405.0), 's250': (1598.799, 405.0), 's251': (1621.006, 405.0), 's252': (1643.213, 405.0), 's253': (1665.42, 405.0), 's254': (1687.627, 405.0), 's255': (1709.834, 405.0), 's256': (1732.041, 405.0)}

		activeSelectionAreasASICd = {"1": (694.0, 294.0)}

		activeSelectionAreasR0H1 = {"PWR": (10, 65)}

		self.activeAreas = {"root": activeAreasRoot, "endcap": activeAreasEndcap ,"R0": activeAreasR0,
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
		self.serial = self.serial + "." + self.level[-1]

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
