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
        #  Format of cur_seleced is {cur_location: {area_name: BoardItem}}
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

        # Load the selection tree and edit window
        self.load_selection_tree()

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

        # Colour tree and load edit window
        self.colour_selection_tree()
        self.selection_edit()

    # Load a list of all available modules/hybrids/components
    def load_selection_tree(self):
        # First clear the list
        self.selectionTree.clear()

        # Now add all components according to the list (located in lib/selection_areas.py)
        for module_name in selection_tree_components:
            # Add the top level to the tree
            module = QtWidgets.QTreeWidgetItem([module_name])

            for hybrid_name in selection_tree_components[module_name]:
                # Add hybrid to module
                hybrid = QtWidgets.QTreeWidgetItem([hybrid_name])
                module.addChild(hybrid)

                components = selection_tree_components[module_name][hybrid_name]
                for item in components:
                    component = QtWidgets.QTreeWidgetItem([item])
                    hybrid.addChild(component)
            
            # Add finished module and move on to the next one
            self.selectionTree.addTopLevelItem(module)

    def colour_selection_tree(self):
        # At end, colour this whole list red
        red_list = []
        # Loop through all items on the tree
        # Start with the modules
        for m_index in range(self.selectionTree.topLevelItemCount()):
            cur_module = self.selectionTree.topLevelItem(m_index)

            # Default black
            cur_module.setForeground(0, QtGui.QBrush(QtGui.QColor('Black')))

            # Now hybrids
            for h_index in range(cur_module.childCount()):
                cur_hybrid = cur_module.child(h_index)

                cur_hybrid.setForeground(0, QtGui.QBrush(QtGui.QColor('Black')))

                # Finally all components
                for c_index in range(cur_hybrid.childCount()):
                    cur_component = cur_hybrid.child(c_index)

                    cur_component.setForeground(0, QtGui.QBrush(QtGui.QColor('Black')))

                    # Build the cur_location string to check if the component is selected on
                    cur_location = cur_module.text(0) + cur_hybrid.text(0) + cur_component.text(0)

                    # Set to red if selected
                    if (cur_location in self.cur_selected) and (len(self.cur_selected[cur_location]) != 0):
                        red_list.append(cur_component)
                        if cur_hybrid not in red_list:
                            red_list.append(cur_hybrid)
                        if cur_module not in red_list:
                            red_list.append(cur_module)

        # Now we loop through red list and colour all items
        for item in red_list:
            item.setForeground(0, QtGui.QBrush(QtGui.QColor('Red')))
                   
    def save(self):
        if not self.saved:
            self.save_as()
            return

        # Save to the chosen location
        data = [self.config, self.cur_selected]
        with open(self.save_path, 'wb') as output:
            pickle.dump(data, output)

        # Make names red if needed
        self.colour_selection_tree()

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
            # print('[({:.1f},{:.1f}), ({:.1f},{:.1f}), ({:.1f},{:.1f}), ({:.1f},{:.1f})], '.format(x-dx, y-dy, x+dx, y-dy, x+dx, y+dy, x-dx, y+dy), end='', flush=True)
            self.counter += 1

            # Check if our click was inside of any current (!!UNSELECTED!!) selection areas
            if len(self.cur_dict) > 0 and self.edit_mode:
                for area in self.cur_dict:
                    # First grab coords
                    coords = self.cur_dict[area].coords
                    pts = []

                    # Now convert all coords into a list for the polygon builder
                    for coord in coords:
                        pts.append(QtCore.QPoint(coord[0], coord[1]))

                    # Build the QPolygon and check if the coords are inside of it
                    poly = QtGui.QPolygonF(pts)

                    inside = poly.containsPoint(QtCore.QPointF(x, y), 0)
                    if inside:
                        # cur_indexes = self.edit_widget.elementTree.selectedIndexes()

                        # Now we select it if it doesn't exit on the list. If it does, we deselect it
                        if (self.cur_location in self.cur_selected) and (area in self.cur_selected[self.cur_location]):
                            self.cur_selected[self.cur_location].pop(area)
                        elif self.cur_location in self.cur_selected:
                            self.cur_selected[self.cur_location][area] = self.cur_dict[area]
                        else:
                            self.cur_selected[self.cur_location] = {}
                            self.cur_selected[self.cur_location][area] = self.cur_dict[area]
                        self.load_img()

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

        # Colour components that have been selected
        self.colour_selection_tree()

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
            if cur_img_name[-6:-2] == 'ASIC':
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
        q_blue = QtGui.QColor(0, 0, 255)
        q_abitblue = QtGui.QColor(0, 0, 255, 50)
        # QEmpty = QtGui.QColor(0, 0, 0, 0)

        # Loop through all boxes for current dict
        if len(self.cur_dict) > 0:
            for area in self.cur_dict:

                # First grab coords
                coords = self.cur_dict[area].coords
                pts = []

                # Now convert all coords into a list for the polygon builder
                for coord in coords:
                    pts.append(QtCore.QPoint(coord[0], coord[1]))

                # Draw the polygon on the scene
                poly = QtGui.QPolygonF(pts)
                self.scene.addPolygon(poly, q_red, q_abitred)

        # Loop through all areas in the selected list
        if self.cur_location in self.cur_selected:
            selected_dict = self.cur_selected[self.cur_location]
            for area in selected_dict:
                # First grab coords
                coords = selected_dict[area].coords
                pts = []

                # Now convert all coords into a list for the polygon builder
                for coord in coords:
                    pts.append(QtCore.QPoint(coord[0], coord[1]))

                # Draw the polygon on the scene
                poly = QtGui.QPolygonF(pts)
                self.scene.addPolygon(poly, q_blue, q_abitblue)

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
