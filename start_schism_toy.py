#start_schism_mb.py
#Instructions:
# - First, modify "MODIFY" section with the proper paths
# - Open VisIt, select Controls:Launch CLI
# - A terminal should open with >>>
# - Copy and paste everything between BEGIN COPY and END COPY
# - Copy and paste plot commands one by one

##---BEGIN COPY---------------

##-- MODIFY -------------------
##--Set path to scripts----
SCRIPT_PATH = "/Users/lllowe/visit-scripts"
#Put the full path to the file
FILE_NAME = "/Users/lllowe/A-CGEM/outputs-srand/GEN_4_1.nc"
##-- END MODIFY ---------------

#So it can find setup_visit.py
import sys 
sys.path.append(SCRIPT_PATH)

from visit import *
from setup_visit import *

## Plot attributes
setvars = {
#The filename
"db" : FILE_NAME,
#The variable to be plotted
"var" : "GEN_4",
#clim=0 means use default min/max for colormap
"clim" : 0,
#If clim=1, choose the min/max for colormap
"cmin" : 0,
"cmax" : 35,
#The colormap
"cmap" : "turbo",
#Scale Z by
"scale" : 20,
#Percent of grid to choose Y slice
"percent" : 35,
#Origin point of transect
"from_x" : 0,
"from_y" : 0,
#Destination point of transect
"to_x" : 600,
"to_y" : 600,
#schism, fvcom, or efdc
"model" : "schism"
}

#Open the file
open_file(setvars)
##---END COPY----------------##


##---Cut and paste these one at a time------##
#3D plot
create_pseudocolor_3Dplot(setvars)

#2D at constant Y (choose Y as percent)
create_pseudocolor_2Dslice(setvars)

#To use a different percent, just change "percent" 
setvars["percent"]= 20
create_pseudocolor_2Dslice(setvars)

#2D transect between two chosen points
create_pseudocolor_2Dtransect(setvars)

#2D transect shown within the 3D grid
#For large grids, it takes forever to rotate when opacity is on
#"Hide" the Mesh variable, Rotate it until you find the transect, then "Show"
transect_against_3D(setvars)
