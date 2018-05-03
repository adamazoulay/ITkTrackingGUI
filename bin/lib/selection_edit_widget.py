from PyQt5 import QtGui, QtWidgets, QtCore, uic  # Import the PyQt5 modules we'll need
from .selection_areas import *


# Define the classes for the edit window gui
class SelectionEditWidget(QtWidgets.QMainWindow):

    def __init__(self, parent):
        super(self.__class__, self).__init__()
        uic.loadUi('lib/SelectionEdit.ui', self)
        self.parent = parent

        # Define self variables
        self.max_cols = 3
        self.cur_selected_item = {}  # This is the dict for the currently viewed component
        self.number_of_custom = 0
        self.custom_item = ''  # Store the current custom item
        self.cur_name = ''
        self.custom_mode = False

        # Turn off image scrolling on load (bug?)
        self.parent.selectionView.setDragMode(QtWidgets.QGraphicsView.NoDrag)

        # Set edit mode flag in parent and reload current image
        self.parent.edit_mode = True

        self.btnAdd.clicked.connect(self.add_selected_components)
        self.btnRemove.clicked.connect(self.remove_selected_components)

        self.btnCustomAdd.clicked.connect(self.add_custom_component)

        self.btnSave.clicked.connect(self.parent.save)
        self.btnClose.clicked.connect(self.close)

        # Save comments triggers
        self.selectedTree.itemSelectionChanged.connect(self.save_comments)
        self.selectedTree.installEventFilter(self)

        # If double clicked and editable:
        self.selectedTree.itemDoubleClicked.connect(self.comment_double_click)

    # Add a function for making the comments field editable
    def comment_double_click(self, tree_item, col):
        # Check if in comment column
        if col == 2:
            tree_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
            self.selectedTree.editItem(tree_item, col)

            # Now save the comment in the selected pads list
            name = tree_item.text(0)
            self.parent.cur_selected[self.parent.cur_location][name].comments = tree_item.text(2)

        name = tree_item.text(0)
        self.parent.cur_selected[self.parent.cur_location][name].comments = tree_item.text(2)

    # Save all comments
    def save_comments(self):
        for i in range(self.selectedTree.topLevelItemCount()):
            item = self.selectedTree.topLevelItem(i)
            name = item.text(0)

            # Board item edit to add comments
            if self.parent.cur_location in self.parent.cur_selected:
                selected_items = self.parent.cur_selected[self.parent.cur_location]

                if name in selected_items:
                    self.parent.cur_selected[self.parent.cur_location][name].comments = item.text(2)

    def eventFilter(self, widget, event):
        # FocusOut event
        if event.type() == QtCore.QEvent.FocusOut:
            # Save comments on focus out
            self.save_comments()
            # return False so that the widget will also handle the event
            # otherwise it won't focus out
            return False
        else:
            # we don't care about other events
            return False

    # Add a custom list of coordinates to mark an area
    def add_custom_component(self):
        # Start by naming the custom component
        self.number_of_custom += 1
        self.cur_name = 'Custom' + str(self.number_of_custom)
        self.custom_item = BoardItem('', '', '', '', '', [], '')
        self.parent.cur_selected[self.parent.cur_location][self.cur_name] = self.custom_item
        self.custom_mode = True

    # Add all selected components to the cur_selected dict and reload the list
    def add_selected_components(self):
        # Get all highlighted items from cur_selected
        cur_indexes = self.elementTree.selectedIndexes()

        # The cur_indexes list contains every row and every column, i.e. [row0col0, row0col1, row1col1, etc]
        # This means we need to loop through the list and grab the first column since it's the index for the dict
        count = self.max_cols
        label_list = []
        for item in cur_indexes:
            if count % self.max_cols == 0:
                label_list.append(item.data())
            count += 1

        # Now add all selected items to the cur_selected dict (create empty if needed)
        if self.parent.cur_location not in self.parent.cur_selected:
            self.parent.cur_selected[self.parent.cur_location] = {}

        for item in label_list:
            elem = self.parent.cur_dict[item]
            elem.comments = ''
            self.parent.cur_selected[self.parent.cur_location][item] = elem

        # Finally, reload the lists, and redraw boxes
        self.load_list()
        self.parent.load_img()

    # Remove all selected components from cur_selected dict and reload the list
    def remove_selected_components(self):
        # Get all highlighted items from selectedTree
        cur_indexes = self.selectedTree.selectedIndexes()

        count = self.max_cols
        label_list = []
        for item in cur_indexes:
            if count % self.max_cols == 0:
                label_list.append(item.data())
            count += 1

        # Now remove all selected items to the cur_selected dict
        for item in label_list:
            # Wipe comments and remove item
            self.parent.cur_selected[self.parent.cur_location][item].comments = ''
            self.parent.cur_selected[self.parent.cur_location].pop(item)

        # Finally, reload the lists
        self.load_list()
        self.parent.load_img()

    # Position the edit_window to the right of the main window
    def build_edit_coords(self):
        g = self.parent.geometry()
        
        xpos = g.x() + g.width()
        ypos = g.y()

        xsize = g.width()/9 * 3
        ysize = g.height()

        self.move(xpos, ypos)
        self.resize(xsize, ysize)

    # Populate the list with selectable areas
    def load_list(self):
        # First wipe the current list from element and selected trees
        self.elementTree.clear()
        self.selectedTree.clear()
        # Find the component currently loaded
        cur_location = self.parent.cur_location
        cur_selected = self.parent.cur_selected

        # Different load cases
        if 'ASIC' in cur_location:
            self.parent.cur_dict = ASIC

        # If any selection exists at current location, load it up
        if cur_location in cur_selected:
            self.cur_selected_item = cur_selected[cur_location]

        # Set for convenience
        cur_dict = self.parent.cur_dict

        # Populate elementTree
        for item in cur_dict:
            elem = cur_dict[item]
            cols = [item, elem.name, elem.description]
            row = QtWidgets.QTreeWidgetItem(cols)
            self.elementTree.addTopLevelItem(row)

        # Populate selectedTree
        for item in self.cur_selected_item:
            elem = self.cur_selected_item[item]
            cols = [item, elem.name, elem.comments]
            row = QtWidgets.QTreeWidgetItem(cols)
            self.selectedTree.addTopLevelItem(row)

        # Reset starting dicts
        self.cur_selected_item = {}
