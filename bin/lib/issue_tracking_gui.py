# System imports
import os  # We need sys so that we can pass argv to QApplication
import pickle  # For saving the results
# import matplotlib.path as mplPath
# import numpy as np

# Local imports (gives Qt imports as well)
from .selection_edit_widget import *
from .config_edit_widget import *


# ================================================================================
# TODO:
#  -- general marking
#  -- component lists - find design files
#  - power board
#  - make names red??
# ================================================================================


# Define the classes for the main gui
class IssueTrackingGUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        uic.loadUi('lib/IssueTrackingGUI.ui', self)

        # Class variables
        self.cur_location = ''  # Track current image location
        self.cur_selected = {}  # This is the dict of dicts of ALL selected elements (across all components)
        self.cur_dict = {}  # This is a dict of the available elements for the current location
        self.zoom_factor = 0  # Track the current zoom level
        self.edit_mode = False  # Flag to set edit mode on image
        self.edit_widget = None  # Store the editing window here when needed
        self.config_widget = None  # Store the config window here when needed
        self.scene = None  # Store the scene so we can add selection areas
        self.saved = False  # Check if we need to save a new file
        self.save_path = ''
        self.counter = 0  # Debugging

        # Change this to external file eventually
        self.config = {'un': '', 'inst': '', 'dbkey1': '', 'dbkey2': '', 'idNumber': ''}

        # Define action of the menu items
        self.actionExit.setShortcut("Alt+Q")
        self.actionExit.triggered.connect(self.close)

        self.actionOpen.setShortcut("Alt+O")
        self.actionOpen.triggered.connect(self.open)

        self.actionEdit.setShortcut("Alt+E")
        self.actionEdit.triggered.connect(self.selection_edit)

        self.actionConfiguration.setShortcut("Alt+C")
        self.actionConfiguration.triggered.connect(self.config_edit)

        self.actionSave.setShortcut("Alt+S")
        self.actionSave.triggered.connect(self.save)

        self.actionSave_As.triggered.connect(self.save_as)

        self.actionAbout.triggered.connect(self.about)

        # Load image if tree selection is changed
        self.selectionTree.currentItemChanged.connect(self.load_img)

        # Event filter on selectionView
        self.selectionView.viewport().installEventFilter(self)

    def save(self):
        if not self.saved:
            self.save_as()
            return

        # Save to the chosen location
        data = [self.config, self.cur_selected]
        print(data)
        with open(self.save_path, 'wb') as output:
            pickle.dump(data, output)

    def save_as(self):
        # Open a dialog and ask user to choose file save location
        self.save_path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save As..')[0]  # [0] is the path

        if self.save_path != '':
            self.saved = True
            self.save()

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

        if ev.type() == QtCore.QEvent.MouseButtonRelease:
            pos = ev.pos()
            scene_pt = self.selectionView.mapToScene(pos)
            x = scene_pt.x()
            y = scene_pt.y()
            # Build 4 points
            dx = 7.4
            dy = 16.8
            print('[({:.1f},{:.1f}), ({:.1f},{:.1f}), ({:.1f},{:.1f}), ({:.1f},{:.1f})], '.format(x-dx, y-dy, x+dx, y-dy, x+dx, y+dy, x-dx, y+dy), end='', flush=True)
            self.counter += 1
            return True

        return False

    # KeyPress and KeyRelease control the dragging behaviour of the image
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

    # Open a pickle file containing the cur_selected dict from a previous run
    def open(self):
        open_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.save_path = open_path

        if open_path != '':
            # Load into our variables
            with open(open_path, 'rb') as input_file:
                data = pickle.load(input_file)
                self.config = data[0]
                self.cur_selected = data[1]

            self.saved = True

    # Load the image currently selected in the tree
    def load_img(self):
        # Reset the cur_dict (loaded in selection widget)
        self.cur_dict = {}
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
                # Draw areas and populate lists
                self.edit_widget.load_list()
                self.draw_boxes()

    # Draw the possible selection areas onto the screen
    def draw_boxes(self):
        # Set up some pen colours
        q_red = QtGui.QColor(255, 0, 0)
        q_abitred = QtGui.QColor(255, 0, 0, 50)
        # Qblue = QtGui.QColor(0, 0, 255)
        # QEmpty = QtGui.QColor(0, 0, 0, 0)

        # Loop through all boxes for current dict
        for area in self.cur_dict:

            # First grab coords
            coords = self.cur_dict[area].coords
            pts = []

            # Now convert all coords into a list for the polygon builder
            for coord in coords:
                pts.append(QtCore.QPoint(coord[0],coord[1]))

            # Draw the polygon on the scene
            poly = QtGui.QPolygonF(pts)
            self.scene.addPolygon(poly, q_red, q_abitred)

    # Open the edit window
    def selection_edit(self):
        self.edit_widget = SelectionEditWidget(self)
        self.edit_widget.show()
        self.load_img()

    # Open the config window
    def config_edit(self):
        self.config_widget = ConfigEditWidget(self)
        self.config_widget.show()

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
