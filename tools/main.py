'''
This is a QA tracker for ASIC/hybrid/module wire bonding.

============
MORE HERE
============

todo:
- Picture for each different hybrid
- look up wire bonding for r0h0 and r0h1 for numbering of asics
- do hybrid -> asic (number of hybrid, number of asic, wire bond numbers)
- Depending on inspection (i.e. log file, manual input, etc)
- HCC bonds
- Talk to UofT about wire bonding output
- Tool for viewing certain areas


Author: Adam Azoulay, aazoulay@yorku.ca
'''

#imports here
from PIL import Image, ImageDraw, ImageFont, ImageOps
import ITkObject
import pickle
import numpy as np
import xlrd


if __name__ == "__main__":

        #Get current hybrid type (this should be a gui selection eventually)
        moduleName = "R0"
        hybridName = "H1"
        ASIC = "17" #Get ASIC ID numbers and put them on a picture

        #Load in the hybrid object
        pathModule = "data\\" + moduleName + "\\" + moduleName
        pathHybrid = "data\\" + moduleName + "\\" + moduleName + hybridName
        pathASIC = "data\\" + moduleName + "\\" + moduleName + hybridName + "ASIC"
        
        hybridObjFile = open(pathASIC + ".obj", "r")
        hybridObj = pickle.load(hybridObjFile)

        print "ATLAS Strip Wire Bonding QA"
        print "Version: " + hybridObj.name + "\n\n"

        bonder = raw_input("Please enter bonder name: ")

        panelNum = int(raw_input("Please enter the panel number (>0): "))

        hybridNum = int(raw_input("Please enter the hybrid number (0-7): "))

        fileName = "Panel_" + str(panelNum) + "_Hybrid_" + str(hybridNum) + ".txt"
        print "\n\nSaving as " + fileName

        log = open(fileName, "w")

        #=========================================================
        #Start main loop here
        markPads = []
        cmd = ''
        while True:
                cmd = raw_input("Please enter a command ((w)ire, (c)omment, (q)uit): ")
                cmd = cmd.lower()

                #Wire bond issue
                if cmd == "w":
                        
                        wires = hybridObj.wires
                        wireNum = int(raw_input("Please enter a wire bond number (1-1020): "))
                        pad = str(hybridObj.pads[wireNum-1])
                        wireChip = wires[wireNum-1][2]
                        wireDesc = wires[wireNum-1][0]
                        wirePurp = wires[wireNum-1][1]

                        #Record pad number to mark image
                        markPads.append(int(pad))
                        
                        print "\nWire bond", wireNum, "corresponds to Pad #" + pad +\
                                  " on chip #" + wireChip + " which bonds " + wireDesc +\
                                  " to " + wirePurp + "\n"

                        cmdWire = raw_input("Enter R for re-work, F for failed bond, or C if check is needed: ")
                        cmdWire = cmdWire.lower()
                        log.write("Wire #" + str(wireNum) + "\n")
                        log.write("Pad #" + pad + "\n")
                        log.write("Chip #" + wireChip + "\n")
                        log.write("Wirebond from " + wireDesc + " to " + wirePurp + "\n")
                        log.write("\tError: " + cmdWire.upper() + "\n\n")
                        print "Error saved\n"
                        continue

                if cmd == "c":
                        comment = raw_input("Enter comments:\n")
                        log.write("============================\n")
                        log.write(comment)
                        log.write("\n============================\n\n")
                        print ""
                        continue

                if cmd == 'q':
                        break
                
                print "Please enter a valid command\n"


        log.close()

        #Mark image test
        
        
        book = xlrd.open_workbook('data\\sheet.xls')
        print "Loading sheet.xls\n\n"

        if ASIC != "":
                image = Image.open(pathASIC + ".jpg")
                
        print "Loading abc130.JPG\n\n"
        width, height = image.size # overall dimensions 4032 x 3024

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', 30) # For a PC
        fontNum = ImageFont.truetype('arial.ttf', 25) # For a PC
        #font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50) #For a mac
        #txt=Image.new('L', (100,100))
        #d = ImageDraw.Draw(txt)
        #d.text((0, 0), "X", font=font, fill=255)

        #Get the first booksheet
        sheet = book.sheet_by_index(0)

        #Number of rows
        total_rows = sheet.nrows
        total_columns = sheet.ncols

        colz0=[]
        colz1=[]
        colz4=[]
        colz5=[]
        colz6=[]

        #reads the excell sheet in columns
        for row in range(sheet.nrows):
                colz0.append(sheet.cell_value(row,0)) #Pad number
                colz1.append(sheet.cell_value(row,1)) #Pad description
                colz4.append(sheet.cell_value(row,4)) #rotation
                colz5.append(sheet.cell_value(row,5)) #x location?
                colz6.append(sheet.cell_value(row,6)) #y location?

        bob0 = np.asarray(colz0, int) #Pad number
        bob4 = np.asarray(colz4, int) #rotation
        bob5 = np.asarray(colz5, int) #x location?
        bob6 = np.asarray(colz6, int) #y location?


        #Loop through all pads
        xpos = 430
        ypos = 300

        #sort markPads
        markPads = sorted(markPads)
        for pad in markPads:
                
                #Pull first bond to test
                dave = pad

                #Assign number to X mark
                txt=Image.new('L', (100,100))
                d = ImageDraw.Draw(txt)
                d.text((0, 0), "X", font=font, fill=255)

                if pad%2 == 0:
                        offset = 50
                else:
                        offset = 25
                        
                d.text((0, offset), str(pad), font=fontNum, fill=255)

                w=txt.rotate(bob4[dave-1], expand=1)


                txtt=Image.new('L', (500,50))
                dd = ImageDraw.Draw(txtt)
                dd.text((0, 0), str(pad) + ". " + colz1[dave-1], font=font, fill=255)
                 
                
                image.paste( ImageOps.colorize(w, (0,0,0), (255,0,0,255)), (bob5[dave-1],bob6[dave-1]),  w) #x mark

                ww=txtt.rotate(0, expand=1)
                image.paste( ImageOps.colorize(ww, (0,0,0), (255,0,0,255)), (xpos,ypos),  ww) #description text
                ypos += 25


        imgName = moduleName+hybridName+".jpg"
        image.save(imgName)
        print "The image has been saved as " + imgName
        bob = Image.open(imgName)
        bob.show()
