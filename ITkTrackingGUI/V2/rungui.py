from PyQt5 import QtGui, QtWidgets, QtCore, uic  # Import the PyQt5 module we'll need
# import matplotlib.path as mplPath
# import numpy as np
import sys
import os  # We need sys so that we can pass argv to QApplication


# ================================================================================
# TODO:
#  -
# ================================================================================


# Define the classes for the main gui
class IssueTrackingGUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        uic.loadUi('IssueTrackingGUI.ui', self)

        # Class variables
        self.cur_location = ''
        self.zoom_factor = 0

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
            img_path = os.path.join(cur_dir, 'imgs', (cur_img_name + '.jpg'))
            img_pixmap = QtGui.QPixmap(img_path, "1")

            # Scale the image by the zoom
            # zoom = self.zoomScale

            # Build a scene for the graphics view
            scene = QtWidgets.QGraphicsScene(self)
            scene.addPixmap(img_pixmap)
            self.selectionView.setScene(scene)

            # Fit in view
            if self.zoom_factor == 0:
                self.selectionView.fitInView(
                    self.selectionView.sceneRect(), QtCore.Qt.KeepAspectRatio)


# ================================================================================
# All functions and main down here
def display_gui():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = IssueTrackingGUI()  # We set the form to be our MainWindow
    form.show()  # Show the form
    sys.exit(app.exec_())  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    display_gui()  # run the main function
