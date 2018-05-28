# System imports
import os  # We need sys so that we can pass argv to QApplication
import pickle  # For saving the results

# Local imports (gives Qt imports as well)
from .selection_edit_widget import *
from .config_edit_widget import *


# Define the classes for the main gui
class IssueTrackingGUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        uic.loadUi('lib/IssueTrackingGUI.ui', self)

        # Class variables
        self.cur_location = ''  # Track current image location
        self.cur_selected = {}  # This is the dict of dicts of ALL selected elements (across all components)
        #  Format of cur_selected is {cur_location: {area_name: BoardItem, custom_count: Int}}
        self.cur_dict = {}  # This is a dict of the available elements for the current location
        self.zoom_factor = 0  # Track the current zoom level
        self.edit_mode = False  # Flag to set edit mode on image
        self.edit_widget = None  # Store the editing window here when needed
        self.config_widget = None  # Store the config window here when needed
        self.scene = None  # Store the scene so we can add selection areas
        self.saved = False  # Check if we need to save a new file
        self.save_path = ''
        self.counter = 0  # Debugging

        # Change this to external file eventually?
        self.config = {'un': '', 'inst': '', 'dbkey1': '', 'dbkey2': '', 'idNumber': '', 'custom_num': 1}

        # Define action of the menu items
        self.actionExit.setShortcut("Alt+Q")
        self.actionExit.triggered.connect(self.close)

        self.actionNew.setShortcut("Alt+N")
        self.actionNew.triggered.connect(self.new)

        self.actionOpen.setShortcut("Alt+O")
        self.actionOpen.triggered.connect(self.open)

        self.actionConfiguration.setShortcut("Alt+C")
        self.actionConfiguration.triggered.connect(self.config_edit)

        self.actionSave.setShortcut("Alt+S")
        self.actionSave.triggered.connect(self.save)

        self.actionSave_As.triggered.connect(self.save_as)

        self.actionHelp.triggered.connect(self.open_help)

        self.actionAbout.triggered.connect(self.about)

        # Load image if tree selection is changed
        self.selectionTree.currentItemChanged.connect(self.load_img)

        # Event filter on selectionView
        self.selectionView.viewport().installEventFilter(self)

        # Load edit window
        self.selection_edit()

    @staticmethod
    def open_help():
        url = QtCore.QUrl('https://itktrackingguidocs.readthedocs.io/en/latest/')
        QtGui.QDesktopServices.openUrl(url)

    def colour_selection_tree(self):

        total_len = self.selectionTree.topLevelItemCount()

        elems = []
        for i in range(total_len):
            self.flatten_tree(elems, self.selectionTree.topLevelItem(i))

        # Now we have a list of all the elements in the tree
        red_list = []

        for item in elems:
            # First set to default black
            item.setForeground(0, QtGui.QBrush(QtGui.QColor('Black')))

            # Build the location string
            loc = item.text(0)
            temp_item = item
            while temp_item.parent() is not None:
                temp_item = temp_item.parent()
                loc = temp_item.text(0) + loc

            if loc in self.cur_selected:
                if len(self.cur_selected[loc]) != 0:
                    red_list.append(item)

        # Now we have all selected items in the red_list, just loop and make them red (and parents)
        for item in red_list:

            while item != None:
                item.setForeground(0, QtGui.QBrush(QtGui.QColor('Red')))
                item = item.parent()

    def flatten_tree(self, elems, node):
        children = node.childCount()

        # First add the current node
        elems.append(node)

        # Then loop through remaining children
        for i in range(children):
            self.flatten_tree(elems, node.child(i))

        return elems

    def save(self):
        if not self.saved:
            self.save_as()
            return

        # Save to the chosen location
        data = [self.config, self.cur_selected]
        with open(self.save_path, 'wb') as output:
            pickle.dump(data, output)

    def save_as(self):
        # Open a dialog and ask user to choose file save location
        self.save_path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save As..')[0]  # [0] is the path

        if self.save_path != '':
            self.saved = True
            self.save()

    # This will start a new item to be marked on
    # TODO why is this saving the comments?
    def new(self):
        # Wipe all and start again
        # Class variables
        self.cur_location = ''  # Track current image location
        self.cur_selected = {}  # This is the dict of dicts of ALL selected elements (across all components)
        self.cur_dict = {}  # This is a dict of the available elements for the current location
        self.zoom_factor = 0  # Track the current zoom level
        self.config_widget = None  # Store the config window here when needed
        self.scene = None  # Store the scene so we can add selection areas
        self.saved = False  # Check if we need to save a new file
        self.save_path = ''

        # Reset custom numbering
        self.config['custom_num'] = 1

        self.edit_widget.load_list()

        self.colour_selection_tree()
        self.load_img()

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

        # add point to custom array, 1 is left click
        if (ev.type() == QtCore.QEvent.MouseButtonRelease) and (ev.button() == 1) and self.edit_widget.custom_mode:
            pos = ev.pos()
            scene_pt = self.selectionView.mapToScene(pos)
            x = scene_pt.x()
            y = scene_pt.y()

            # Start building the custom positions and adding to BoardItem array
            item = self.cur_selected[self.cur_location][self.edit_widget.cur_name]
            item.coords.append((x, y))
            self.cur_selected[self.cur_location][self.edit_widget.cur_name] = item

            # Refresh the boxes
            self.load_img()
            return True

        # Disable custom mode, 2 is right click
        if (ev.type() == QtCore.QEvent.MouseButtonRelease) and (ev.button() == 2) and self.edit_widget.custom_mode:
            self.edit_widget.custom_mode = False
            self.edit_widget.load_list()
            return True

        # 1 is left click
        if (ev.type() == QtCore.QEvent.MouseButtonRelease) and (ev.button() == 1):
            pos = ev.pos()
            scene_pt = self.selectionView.mapToScene(pos)
            x = scene_pt.x()
            y = scene_pt.y()

            # This whole sectio is for building the location lists
            # Build 4 points
            dx = 12.2
            dy = 23.1
            sensor_pads = 0
            if sensor_pads:
                for n in range(64):
                    step = 22.2
                    print(
                        '[({:.1f},{:.1f}), ({:.1f},{:.1f}), ({:.1f},{:.1f}), ({:.1f},{:.1f})], '.format(x - dx, y - dy,
                                                                                                        x + dx, y - dy,
                                                                                                        x + dx, y + dy,
                                                                                                        x - dx, y + dy),
                        end='', flush=True)
                    x += step
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
            if 'ASIC' in cur_img_name:
                cur_img_name = 'ASICu'
            elif 'HCC' in cur_img_name:
                cur_img_name = 'HCC'
            elif ('Powerboard' in cur_img_name) and ('Barrel' in cur_img_name):
                cur_img_name = 'pwrBarrel'

            # Load name.jpg into QGraphicsView selectionView
            cur_dir = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(cur_dir, '..', 'imgs', (cur_img_name + '.jpg'))
            img_pixmap = QtGui.QPixmap(img_path, "1")

            # Build a scene for the graphics view
            self.scene = QtWidgets.QGraphicsScene(self)
            self.scene.addPixmap(img_pixmap)
            self.selectionView.setScene(self.scene)

            # Add an empty dict if not in there
            if self.cur_location not in self.cur_selected:
                self.cur_selected[self.cur_location] = {}

            # Fit in view
            if self.zoom_factor == 0:
                self.selectionView.fitInView(
                    self.selectionView.sceneRect(), QtCore.Qt.KeepAspectRatio)

            if self.edit_mode:
                # Draw areas and populate lists
                self.edit_widget.load_list()
                self.draw_boxes()

            self.colour_selection_tree()

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

    # Gets the resolution and finds a placement for the main and edit windows
    def build_window_coords(self):
        # Get the area the program can actually use
        ag = QtWidgets.QDesktopWidget().availableGeometry()

        xpos = ag.width() / 14
        ypos = ag.height() / 10

        xsize = xpos * 12
        ysize = ypos * 8

        self.move(xpos, ypos)
        self.resize(xsize, ysize)

        # Now set the widget sizes
        self.selectionTree.resize(xsize, ysize)
        self.selectionView.resize(xsize, ysize)
        self.edit_widget.resize(xsize * 0.25, ysize)

    # Open the edit window
    def selection_edit(self):
        self.edit_widget = SelectionEditWidget(self)

        self.splitter.addWidget(self.edit_widget)
        self.load_img()

    # Open the config window
    def config_edit(self):
        self.config_widget = ConfigEditWidget(self)
        self.config_widget.show()

    # Display the about popup
    def about(self):
        info = '''This application was developed for use in the tracking of issues during production of ITk components.

Forward any questions or comments to aazoulay@yorku.ca'''
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'About', info)

        # Add image
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(cur_dir, '..', 'imgs', 'about_img.jpg')
        icon_path = os.path.join(cur_dir, '..', 'imgs', 'form.png')
        msg.setIconPixmap(QtGui.QPixmap(img_path).scaled(350, 350, QtCore.Qt.KeepAspectRatio))
        msg.setWindowIcon(QtGui.QIcon(icon_path))
        msg.exec_()
