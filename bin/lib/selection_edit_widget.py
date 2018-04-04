from PyQt5 import QtGui, QtWidgets, QtCore, uic  # Import the PyQt5 module we'll need
from .selection_areas import *


# Define the classes for the edit window gui
class SelectionEditWidget(QtWidgets.QMainWindow):

    def __init__(self, parent):
        super(self.__class__, self).__init__()
        uic.loadUi('lib/SelectionEdit.ui', self)
        self.parent = parent

        # Define self variables
        self.cur_dict = {}

        # Turn off image scrolling on load (bug?)
        self.parent.selectionView.setDragMode(QtWidgets.QGraphicsView.NoDrag)

        # Set edit mode flag in parent and reload current image
        self.parent.edit_mode = True

        self.btnAdd.clicked.connect(self.add_selected_components)


    # Add all selected components to the cur_selceted dict and reload the list
    def add_selected_components(self):
        # Get all highlighted items from cur_selected
        cur_index = self.elementTree.currentIndex()
        cur_data = self.elementTree.data(cur_index)
        print(cur_data)


    # Populate the list with selectable areas
    def load_list(self):
        # First wipe the current list from element and selected trees
        self.elementTree.clear()
        self.selectedTree.clear()
        # Find the component currently loaded
        cur_location = self.parent.cur_location
        cur_selected = self.parent.cur_selected

        cur_dict = self.cur_dict

        if cur_location[-5:-1] == 'ASIC':
            cur_dict = ASIC

        # Populate elementTree
        for item in cur_dict:
            elem = cur_dict[item]
            cols = [item, elem.name, elem.description]
            row = QtWidgets.QTreeWidgetItem(cols)
            self.elementTree.addTopLevelItem(row)

        # Populate selectedTree
        for item in cur_selected:
            elem = cur_selected[item]
            cols = [item, elem.name, elem.comments]
            row = QtWidgets.QTreeWidgetItem(cols)
            self.elementTree.addTopLevelItem(row)
