#start_fvcom_lm.py
#Instructions:
# - First, modify "MODIFY" section with the proper paths
# - Open VisIt, select Controls:Launch CLI
# - A terminal should open with >>>
# - Copy and paste everything between BEGIN COPY and END COPY
# - Copy and paste commands one by one

##----After modifying paths, BEGIN COPY---------------------

##--MODIFY-------------------
##--Set path to scripts----
SCRIPT_PATH = "/Users/lllowe/visit-scripts"
#Put the full path to the file
FILE_NAME = "/Users/lllowe/visit-scripts/mi_0013.nc"
##--End MODIFY

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
"var" : "TP",
#clim=0 means use default min/max for colormap
"clim" : 1,
#If clim=1, choose the min/max for colormap
"cmin" : 0.002,
"cmax" : 0.008,
#The colormap
"cmap" : "turbo",
#Scale Z by
"scale" : 1000,
#Percent of grid to choose Y slice
"percent" : 35,
#Origin point of transect
"from_x" : 560998.31,
"from_y" : 4767358.50,
#Destination point of transect
"to_x" : 539195.69,
"to_y" : 4765827.50,
#schism, fvcom, or efdc
"model" : "fvcom" 
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
