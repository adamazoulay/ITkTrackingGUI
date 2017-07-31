from PyQt4 import QtGui # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication


import QAgui # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer


class MainApp(QtGui.QMainWindow, QAgui.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

def displayGui():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = MainApp()                    # We set the form to be our MainApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    displayGui()                              # run the main function

