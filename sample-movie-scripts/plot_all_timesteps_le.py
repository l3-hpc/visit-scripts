#PEP-8 style guide says each line should be 79 characters or less.............|
#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

#For exit command
import sys 

#To calculate normal vector for defining transect
import numpy as np

##--MODIFY-------------------
##--Set path to scripts----
SCRIPT_PATH = "/Users/lllowe/visit-scripts"
#Put the full path to the file
FILE_NAME = "/Users/lllowe/A-ORD/Baseline_2013_0001.nc"
#Define where the images should be printed out
#If the images exist already, they will be overwritten
IMGS_DIR = "/Users/lllowe/A-ORD/images/"
##-- END MODIFY ---------------

#So it can find simple_schism.py
import sys
sys.path.append(SCRIPT_PATH)

from visit import *
from setup_visit_base import *

## Plot attributes
setvars = {
#The filename
"db" : FILE_NAME,
#The variable to be plotted
"var" : "TP_tot",
#clim=0 means use default min/max for colormap
"clim" : 1,
#If clim=1, choose the min/max for colormap
"cmin" : 0,
"cmax" : 0.1,
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
#Are you using SCHISM?, True or False
"model" : "fvcom" 
}


#Check that the file exists
if not os.path.exists(setvars["db"]):
    sys.exit("The file " + setvars["db"] + " does not exist.  Check definition of db in setvars. Exiting.")

#Create a directory for images if one doesn't exist.
#Note, existing files will be overwritten
if not os.path.exists(IMGS_DIR):
    os.makedirs(IMGS_DIR)


#Open the file
open_file(setvars)


DefineScalarExpression("TP_tot", "RPOP + LPOP + RDOP + LDOP + PO4T + LPIP + RPIP + (ZOO1 + ZOO2 + ZOO3)/50.0")


## Define the attributes for saving images 
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = IMGS_DIR 
#Sets the name below
###SaveWindowAtts.fileName = IMGS_NAME
#Setting family to zero means it will overwrite existing files 
SaveWindowAtts.family = 0
#Set aspect ratio
#SaveWindowAtts.resConstraint = 1 #NoConstraint
#SaveWindowAtts.width = 700
#SaveWindowAtts.height = 600
##Options are: BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, 
##  POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
SaveWindowAtts.format = SaveWindowAtts.PNG
SetSaveWindowAttributes(SaveWindowAtts)

t_start = calendar.timegm(datetime.datetime(1970, 1, 1, 0, 0, 0).timetuple())

m = GetMetaData(setvars["db"])
totalstates = TimeSliderGetNStates()
istate = 0

for state in range(totalstates):
    SetTimeSliderState(state)
    FILE_TS = "_" + str(state).zfill(4)
    slider.visible=1
    tcur = m.times[state] + t_start
    ts = datetime.datetime.utcfromtimestamp(tcur).strftime('%Y-%m-%d %H:%M:%S')
    timestamp = "Time: " + ts + " GMT"
    slider.text=timestamp
    create_pseudocolor_projection(setvars)
    SaveWindowAtts.fileName = setvars["var"] + FILE_TS
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()
    #ClearCacheForAllEngines()

#Comment this out to leave VisIT CLI open after script is complete
sys.exit()

#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
