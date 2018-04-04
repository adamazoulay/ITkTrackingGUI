from PyQt5 import QtGui, QtWidgets, QtCore, uic  # Import the PyQt5 module we'll need
from .selection_areas import *


# Define the classes for the edit window gui
class SelectionEditWidget(QtWidgets.QMainWindow):

    def __init__(self, parent):
        super(self.__class__, self).__init__()
        uic.loadUi('lib/SelectionEdit.ui', self)
        self.parent = parent

        # Turn off image scrolling on load (bug?)
        self.parent.selectionView.setDragMode(QtWidgets.QGraphicsView.NoDrag)

        # Set edit mode flag in parent and reload current image
        self.parent.edit_mode = True

    # Populate the list with selectable areas
    def load_list(self):
        # First wipe the current list
        self.elementTree.clear()
        # Find the component currently loaded
        cur_location = self.parent.cur_location

        cur_dict={'1': 'test'}

        if cur_location[-5:-1] == 'ASIC':
            cur_dict = ASIC

        for item in cur_dict:
            elem = cur_dict[item]
            cols = [item, elem.name, elem.description]
            row = QtWidgets.QTreeWidgetItem(cols)
            self.elementTree.addTopLevelItem(row)
