#===================
#Should rename this to make the modules and asics feel welcome
#  instead of just the hybrids
#===================

class ITkObject(object):

    def __init__(self,name,pads,wires,padCoords):
        #Name of the hybrid (i.e. Barrel 130nm Hybrid)
        self.name = name

        #Pad number on ASIC in order of bonds
        self.pads = pads

        #list with 3-tuples containing (pad name, pad description, and ASIC the wire comes from)
        self.wires = wires
		
		#List of (x,y) tuples containing the top left x,y coords for the bond pads
		self.padCoords = padCoords