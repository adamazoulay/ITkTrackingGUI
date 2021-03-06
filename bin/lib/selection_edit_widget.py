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
        self.btnSaveAs.clicked.connect(self.parent.save_as)

        # Save comments triggers
        self.selectedTree.itemSelectionChanged.connect(self.save_comments)
        self.selectedTree.installEventFilter(self)

        # If double clicked and editable:
        self.selectedTree.itemDoubleClicked.connect(self.comment_double_click)

    # Add a function for making the comments field editable
    def comment_double_click(self, tree_item, col):
        # Check if in comment column
        label = tree_item.text(0)
        if col == 2:
            tree_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
            self.selectedTree.editItem(tree_item, col)

        if col == 1 and 'Custom' in label:
            tree_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
            self.selectedTree.editItem(tree_item, col)

        self.parent.cur_selected[self.parent.cur_location][label].name = tree_item.text(1)
        self.parent.cur_selected[self.parent.cur_location][label].comments = tree_item.text(2)

    # Save all comments
    def save_comments(self):
        for i in range(self.selectedTree.topLevelItemCount()):
            item = self.selectedTree.topLevelItem(i)
            name = item.text(0)
            # Disable the edit flags
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            # Board item edit to add comments
            if self.parent.cur_location in self.parent.cur_selected:
                selected_items = self.parent.cur_selected[self.parent.cur_location]

                if name in selected_items:
                    self.parent.cur_selected[self.parent.cur_location][name].comments = item.text(2)

    # TODO: Do we still need this?
    def eventFilter(self, widget, event):
        # FocusOut event
        if event.type() == QtCore.QEvent.FocusOut:
            # Save comments on focus out
            self.save_comments()
            # return False so that the widget will also handle the event
            # otherwise it won't focus out
            return False
        elif event.type() == QtCore.QEvent.KeyPress:
            # Check if it's the enter of return key
            if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
                #self.save_comments()
                pass
            return False
        else:
            # we don't care about other events
            return False

    # Add a custom list of coordinates to mark an area
    def add_custom_component(self):
        # Start by naming the custom component
        number_of_custom = self.parent.config['custom_num']
        self.parent.config['custom_num'] = number_of_custom + 1

        self.cur_name = 'Custom' + str(number_of_custom)
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

        if 'HCC' in cur_location:
            self.parent.cur_dict = HCC

        if cur_location == 'BarrelLH':
            self.parent.cur_dict = BarrelLH

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
