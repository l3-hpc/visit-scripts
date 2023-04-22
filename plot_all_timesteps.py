#PEP-8 style guide says each line should be 79 characters or less.............|
#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

#For exit command
import sys 

#To calculate normal vector for defining transect
import numpy as np

##-- MODIFY -------------------
##--Set path to scripts----
SCRIPT_PATH = "/Users/lllowe/visit-scripts"
#Put the full path to the file
FILE_NAME = "/Users/lllowe/A-CGEM/outputs-srand/GEN_4_1.nc"
#Define where the images should be printed out
#If the images exist already, they will be overwritten
IMGS_DIR = "/Users/lllowe/A-CGEM/images/"
##-- END MODIFY ---------------

#So it can find simple_schism.py
import sys
sys.path.append(SCRIPT_PATH)

from visit import *
from setup_visit import *


global t_start


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
#Are you using SCHISM?, True or False
"schism" : True
}

#Open the file
open_file(setvars)
##---END COPY----------------##

###-- All of the above was just defining the 'functions' -------------
##    Below is the start of the loop that actually calls the functions
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

skip_states=1    
m = GetMetaData(setvars["db"])
totalstates = TimeSliderGetNStates()
loopstates = int(totalstates/skip_states)
istate = 0
for state in range(totalstates):
    SetTimeSliderState(state)
    FILE_TS = "_" + str(state) 
    slider.visible=0
    create_pseudocolor_2Dslice(setvars)
    SaveWindowAtts.fileName = setvars["var"] + "_" + "slice_" + str(setvars["percent"]) + FILE_TS
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()

#Comment this out to leave VisIT CLI open after script is complete
sys.exit()

#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
