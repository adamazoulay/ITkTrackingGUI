# Issue Tracking GUI (ITG)

This is a work-in-progress tool for tracking the physical defects that occur during ITk module production. It allows users to visually select the area of interest and make comments, as well as *eventually* upload the results directly to the production database for later use.

## Installation

Currently the ITG has only been tested thoroughly on Windows 10 x64, but since Qt is cross platform it should work on all OSes as long as the correct dependencies are installed.

### Installation

1. Download and install [Python 3.6.1](https://www.python.org/downloads/release/python-361/) (downloads at the bottom of the page). Make sure you select the option to add Python to the system PATH during installation.

2. Download and extract the ITG (download button at the top right of project page) to a directory on your computer.

3. Install additional dependencies by running `pip install -r requirements.txt` (on Windows) or  `pip3 install -r requirements.txt` (on OSX) from inside the root folder.

### Usage

To run the program, inside a terminal in the "bin" folder, enter `python main.py` (on Windows) or `python3 main.py` (on OSX).

To use the GUI to record defects, simply select the component you wish to mark from the tree on the left. Press the edit button from the "File" menu, or press the "E" key. Make your selections by clicking the image and fill in comments, then click save. The locations will be saved to a file in the "bin" directory.


**NOTE**
This is still in the beta stages and is constantly being updated. Please be gentle.
