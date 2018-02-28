# System imports
import os  # We need sys so that we can pass argv to QApplication
# import matplotlib.path as mplPath
# import numpy as np
from PyQt5 import QtGui, QtWidgets, QtCore, uic  # Import the PyQt5 module we'll need

# Local imports
from .selection_edit_widget import SelectionEditWidget
from .selection_areas import *

# ================================================================================
# TODO:
#  - Save files
# ================================================================================


# Define the classes for the main gui
class IssueTrackingGUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        uic.loadUi('lib/IssueTrackingGUI.ui', self)

        # Class variables
        self.cur_location = ''  # Track current image location
        self.zoom_factor = 0  # Track the current zoom level
        self.edit_mode = False  # Flag to set edit mode on image
        self.edit_widget = None  # Store the editing window here when needed
        self.scene = None  # Store the scene so we can add selection areas

        # Define action of the menu items
        self.actionExit.setShortcut("Alt+Q")
        self.actionExit.triggered.connect(self.close)

        self.actionEdit.setShortcut("Alt+E")
        self.actionEdit.triggered.connect(self.selection_edit)

        self.actionAbout.triggered.connect(self.about)

        # Load image if tree selection is changed
        self.selectionTree.currentItemChanged.connect(self.load_img)

        # Event filter on selectionView
        self.selectionView.viewport().installEventFilter(self)

    def eventFilter(self, obj, ev):
        if ev.type() == QtCore.QEvent.Wheel:
            zoom_in_factor = 1.25
            zoom_out_factor = 1 / zoom_in_factor

            # Save the scene pos
            old_pos = self.selectionView.mapToScene(ev.pos())

            # Zoom
            if ev.angleDelta().y() > 0:
                zoom_factor = zoom_in_factor
            else:
                zoom_factor = zoom_out_factor

            self.selectionView.scale(zoom_factor, zoom_factor)
            self.zoom_factor = zoom_factor

            # Get the new position
            new_pos = self.selectionView.mapToScene(ev.pos())

            # Move scene to old position
            delta = new_pos - old_pos
            self.selectionView.translate(delta.x(), delta.y())
            return True
        if ev.type() == QtCore.QEvent.KeyPress:
            print('test')
        return False

    # KeyPress and KeyRelease control the draging behaviour of the image
    def keyPressEvent(self, event):
        if event.modifiers() == QtCore.Qt.ControlModifier:
            self.selectionView.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

        # Reset the zoom
        if event.key() == QtCore.Qt.Key_R:
            self.selectionView.fitInView(
                self.selectionView.sceneRect(), QtCore.Qt.KeepAspectRatio)

    def keyReleaseEvent(self, event):
        if event.modifiers() != QtCore.Qt.ControlModifier:
            self.selectionView.setDragMode(QtWidgets.QGraphicsView.NoDrag)

    # Resize the image if the window changes
    def resizeEvent(self, event):
        self.load_img()
        QtWidgets.QMainWindow.resizeEvent(self, event)

    # Load the image currently selected in the tree
    def load_img(self):
        # Make sure correct image name is selected
        cur_img_obj = self.selectionTree.currentItem()

        if cur_img_obj is not None:
            # Build name from parent nodes
            cur_img_name = ''
            while cur_img_obj is not None:
                cur_img_name = cur_img_obj.text(0) + cur_img_name
                cur_img_obj = cur_img_obj.parent()

            # Store total location
            self.cur_location = cur_img_name

            # Adjust for ASIC and HCC pictures
            if cur_img_name[-5:-1] == 'ASIC':
                cur_img_name = 'ASICu'
            elif cur_img_name[-3:] == 'HCC':
                cur_img_name = 'HCC'

            # Load name.jpg into QGraphicsView selectionView
            cur_dir = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(cur_dir, '..', 'imgs', (cur_img_name + '.jpg'))
            img_pixmap = QtGui.QPixmap(img_path, "1")

            # Build a scene for the graphics view
            self.scene = QtWidgets.QGraphicsScene(self)
            self.scene.addPixmap(img_pixmap)
            self.selectionView.setScene(self.scene)

            # Fit in view
            if self.zoom_factor == 0:
                self.selectionView.fitInView(
                    self.selectionView.sceneRect(), QtCore.Qt.KeepAspectRatio)

            if self.edit_mode:
                self.draw_boxes()

    # Draw the possible selection areas onto the screen
    def draw_boxes(self):
        # Set up some pen colours
        q_red = QtGui.QColor(255, 0, 0)
        # Qblue = QtGui.QColor(0, 0, 255)
        q_abitred = QtGui.QColor(255, 0, 0, 50)
        # QEmpty = QtGui.QColor(0, 0, 0, 0)

        # Loop through all boxes for current dict
        current_box = R0H0['R2']
        # Draw box on the image
        coords = current_box.coords
        x = coords[0][0]
        y = coords[0][1]
        width = coords[1][0] - x
        height = y - coords[3][1]
        rect = QtCore.QRectF(x, y, width, height)
        self.scene.addRect(rect, q_red, q_abitred)

    # Open the edit window
    def selection_edit(self):
        self.edit_widget = SelectionEditWidget(self)
        self.edit_widget.show()

    # Display the about popup
    def about(self):
        info = '''This application was developed for use in the tracking of issues during production of ITk components.

Forward any questions or comments to aazoulay@yorku.ca (change this to gitlab wiki later)'''
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'About', info)

        # Add image
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(cur_dir, '..', 'imgs', 'about_img.jpg')
        icon_path = os.path.join(cur_dir, '..', 'imgs', 'form.png')
        msg.setIconPixmap(QtGui.QPixmap(img_path).scaled(350, 350, QtCore.Qt.KeepAspectRatio))
        msg.setWindowIcon(QtGui.QIcon(icon_path))
        msg.exec_()