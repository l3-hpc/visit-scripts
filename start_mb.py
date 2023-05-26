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
FILE_NAME = "/Users/lllowe/VisItForSCHISM/salinity_100.nc"
##-- END MODIFY ---------------

#So it can find setup_visit.py
import sys 
sys.path.append(SCRIPT_PATH)

from visit import *
import l3v 

#set defaults
setvars = {
#The filename
"db" : FILE_NAME,
"year" : 2019, 
#The variable to be plotted
"var" : "salinity_depth_average",
#clim=0 means use default min/max for colormap
"clim" : 0,
#If clim=1, choose the min/max for colormap
"cmin" : 0,
"cmax" : 35,
#The colormap
"cmap" : "viridis",
#Invert the colormap?
"invert" : 0,
#Scale Z by
"scale" : 0.004,
#Percent of grid to choose Y slice
"percent" : 35,
#Origin point of transect
"from_x" : -88.50,
"from_y" : 30.10,
#Destination point of transect
"to_x" : -87.70,
"to_y" : 31.1,
#Back/foreground colors
#Foreground, white
"cfore" : (255, 255, 255, 255),
#Background, black
"cback" : (0, 0, 0, 255),
#Print the legend, time, axes, slider 0==False, 1==True
"legend" : 1,
"time" : 0,
"axes" : 0,
"slider" : 0
}

#Open the file
#l3v.open_file(setvars)
OpenDatabase(setvars["db"],0,"SCHISM")
##---END COPY----------------##


##---Cut and paste these one at a time------##
#3D plot
l3v.pseudocolor_2D(setvars)

#3D plot
l3v.pseudocolor_3D(setvars)

#2D at constant Y (choose Y as percent)
l3v.pseudocolor_2Dslice(setvars)

#To use a different percent, just change "percent" 
setvars["percent"]= 20
l3v.pseudocolor_2Dslice(setvars)

#2D transect between two chosen points
l3v.pseudocolor_2Dtransect(setvars)

#2D transect shown within the 3D grid
#For large grids, it takes forever to rotate when opacity is on
#"Hide" the Mesh variable, Rotate it until you find the transect, then "Show"
l3v.transect_against_3D(setvars)

#Other functions
#average_over_time(<salinity_depth_average> ,0,23,1)
