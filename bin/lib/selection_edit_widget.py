from PyQt5 import QtGui, QtWidgets, QtCore, uic  # Import the PyQt5 module we'll need
from .selection_areas import *


# Define the classes for the edit window gui
class SelectionEditWidget(QtWidgets.QMainWindow):

    def __init__(self, parent):
        super(self.__class__, self).__init__()
        uic.loadUi('lib/SelectionEdit.ui', self)
        self.parent = parent

        # Define self variables
        self.max_cols = 3
        self.cur_selected_item = {}

        # Turn off image scrolling on load (bug?)
        self.parent.selectionView.setDragMode(QtWidgets.QGraphicsView.NoDrag)

        # Set edit mode flag in parent and reload current image
        self.parent.edit_mode = True

        self.btnAdd.clicked.connect(self.add_selected_components)
        self.btnRemove.clicked.connect(self.remove_selected_components)


    # Add all selected components to the cur_selceted dict and reload the list
    def add_selected_components(self):
        # Get all highlighted items from cur_selected
        cur_indexes = self.elementTree.selectedIndexes()

        # The cur_indexes list contains every row and every column, i.e. [row0col0, row0col1, row1col1, etc]
        # This means we need to loop through the list and gram the first column since it's the index for the dict
        count = self.max_cols
        label_list = []
        for item in cur_indexes:
            if count % (self.max_cols) == 0:
                label_list.append(item.data())
            count += 1


        # Now add all selected items to the cur_selected dict (create empty if needed)
        if self.parent.cur_location not in self.parent.cur_selected:
                self.parent.cur_selected[self.parent.cur_location] = {}

        for item in label_list:
            elem = self.parent.cur_dict[item]
            self.parent.cur_selected[self.parent.cur_location][item] = elem

        # Finally, reload the lists
        self.load_list()

    # Remove all selected components from cur_selceted dict and reload the list
    def remove_selected_components(self):
        # Get all highlighted items from selectedTree
        cur_indexes = self.selectedTree.selectedIndexes()

        count = self.max_cols
        label_list = []
        for item in cur_indexes:
            if count % (self.max_cols) == 0:
                label_list.append(item.data())
            count += 1


        # Now remove all selected items to the cur_selected dict
        for item in label_list:
            self.parent.cur_selected[self.parent.cur_location].pop(item)

        # Finally, reload the lists
        self.load_list()


    # Populate the list with selectable areas
    def load_list(self):
        # First wipe the current list from element and selected trees
        self.elementTree.clear()
        self.selectedTree.clear()
        # Find the component currently loaded
        cur_location = self.parent.cur_location
        cur_selected = self.parent.cur_selected

        # Different load cases
        if cur_location[-5:-1] == 'ASIC':
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
