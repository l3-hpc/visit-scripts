#start_efdc_slre.py
#Instructions:
# - First, modify "MODIFY" section with the proper paths
# - Open VisIt, select Controls:Launch CLI
# - A terminal should open with >>>
# - Copy and paste everything between BEGIN COPY and END COPY
# - Copy and paste commands one by one

##--MODIFY-------------------
##--Set path to scripts----
SCRIPT_PATH = "/Users/lllowe/visit-scripts"
#Put the full path to the file
FILE_NAME = "/Users/lllowe/EFDC-CGEM/DATA/slre-cgem.2hrs.nc"
##--END MODIFY

##----BEGIN COPY---------------------
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
"var" : "Tr",
#clim=0 means use default min/max for colormap
"clim" : 1,
#If clim=1, choose the min/max for colormap
"cmin" : 0,
"cmax" : 2,
#The colormap
"cmap" : "turbo",
#Scale Z by
"scale" : .04,
#Percent of grid to choose Y slice
"percent" : 35,
#Origin point of transect
"from_x" : -86.29696,
"from_y" : 46.64568,
#Destination point of transect
"to_x" : -85.88377,
"to_y" : 46.81679,
#schism, fvcom, or efdc
"model" : "efdc" 
}

#Open the file
open_file(setvars)
##---END COPY----------------##

##---Cut and paste these one at a time------##
#3D plot
create_pseudocolor_3Dplot(setvars)

#Change the timeslider or else it will be boring!

#2D projection
create_pseudocolor_projection(setvars)

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
#EFDC doesn't have mesh right now
transect_against_3D(setvars)
