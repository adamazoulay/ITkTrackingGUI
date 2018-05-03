# System imports
import sys
from PyQt5 import QtWidgets

# Local imports
from lib.issue_tracking_gui import IssueTrackingGUI


# ================================================================================
# This program runs the ITG to record areas marked during visual inspection
#
# Adam Azoulay, 2017-2018
# ================================================================================
# All functions and main down here
def display_gui():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = IssueTrackingGUI()  # We set the form to be our MainWindow
    form.build_window_coords()  # Set the main windows coords
    form.edit_widget.build_edit_coords()  # Set the edit window coords
    form.show()  # Show the form
    sys.exit(app.exec_())  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    display_gui()  # run the main function
