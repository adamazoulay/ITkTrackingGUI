# Wirebond QA Tool

This is a work-in-progress tool for tracking the physical defects that occur during ITk module production. It allows users to visually select the area of interest and make comments, as well as *eventually* upload the results directly to the production database for later use.

## Installation/Usage

Currently the GUI has only been tested thoroughly on Windows 10 x64, but since Qt is cross platform it should work on all OSes as long as the correct dependencies are installed.

For Windows installations, the following steps should allow you to run the GUI:

1. Install [WinPython 3.6.1 x64](https://sourceforge.net/projects/winpython/files/WinPython_3.6/3.6.2.0/) (or any Python 3.6.1 package with the SciPy stack) so that you have Qt, matplotlib, and numpy.

2. Run the GUI from the .\WireBondingQA\gui folder with `python rungui.py`. You should see the GUI appear.

3. To use the GUI to record defects, simply click the component you wish to mark and the GUI should zoom to a closer image of the area. Once you have reached the level of zoom you want to mark, change to the "Selection Mode" by clicking the button at the bottom left of the GUI. Make your selections by clicking the image and then click save. The locations will be saved to a file in the "gui" directory.

**NOTE**
This is still in the beta stages and is constantly being updated. Please be gentle.