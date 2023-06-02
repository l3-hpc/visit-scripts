#plot_all_timesteps_le.py
#PEP-8 style guide says each line should be 79 characters or less.............|
#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

#For paths and exit command
import sys 

#To calculate normal vector for defining transect
import numpy as np
#To set the timestamp
import datetime
import calendar

#So it can find simple_schism.py
##--Set path to scripts----
SCRIPT_PATH = "/Users/lllowe/visit-scripts"
sys.path.append(SCRIPT_PATH)

#All visit commands
from visit import *
#Defines plots
from l3v import *
#state variables, like SIT
from leem_vars import *
from setpaths import *

#Put the full path to the file
FILE_NAME = OUTPUTS + "Baseline_2013_0001.nc"
#Define where the images should be printed out

#So it can find simple_schism.py
import sys
sys.path.append(SCRIPT_PATH)

from visit import *
from l3v import *
from leem_vars import *

#Change to match your file 
#t_start = calendar.timegm(datetime.datetime(1970, 1, 1, 0, 0, 0).timetuple())
t_start = calendar.timegm(datetime.datetime(2013, 3, 1, 0, 0, 0).timetuple())

## Plot attributes
setvars = {
#The filename
"db" : FILE_NAME,
#The variable to be plotted
"var" : "SIT",
#Prefix of output file
"name" : "SIT",
#clim=0 means use default min/max for colormap
"clim" : 0,
#If clim=1, choose the min/max for colormap
"cmin" : 0,
"cmax" : 0.1,
#The colormap
"cmap" : "turbo",
#Invert the colormap? no=0, yes=1
"invert" : 0,
#Scale Z by
"scale" : 20,
#Percent of grid to choose Y slice
"percent" : 35,
#Origin point of transect
"from_x" : 320998.31,
"from_y" : 4597358.50,
#Destination point of transect
"to_x" : 380195.69,
"to_y" : 4645827.50,
#Foreground, white
"cfore" : (255, 255, 255, 255),
#Background, black
"cback" : (0, 0, 0, 255),
#Print the legend, 0==False, 1==True
"legend" : 1,
"time" : 0,
"axes" : 0,
#Time slider?
"slider" : True,
#Are you using fvcom, schism, or efdc? 
"model" : "fvcom" 
#
}


#Check that the file exists
if not os.path.exists(setvars["db"]):
    sys.exit("The file " + setvars["db"] + " does not exist.  Check definition of db in setvars. Exiting.")

#Create a directory for images if one doesn't exist.
#Note, existing files will be overwritten
if not os.path.exists(IMAGES):
    os.makedirs(IMAGES)

#Since there will be a large number of images, create directories for each variable
for var in leem_vars:
    #Create a directory for images if one doesn't exist.
    #Note, existing files will be overwritten
    IMGS_DIR = IMAGES + var['name']
    if not os.path.exists(IMGS_DIR):
        os.makedirs(IMGS_DIR)


#Open the file
open_file(setvars)

#DefineScalarExpression("TP_tot", "RPOP + LPOP + RDOP + LDOP + PO4T + LPIP + RPIP + (ZOO1 + ZOO2 + ZOO3)/50.0")


## Define the attributes for saving images 
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = IMAGES
#Setting family to zero means it will overwrite existing files 
SaveWindowAtts.family = 0
#Set aspect ratio
SaveWindowAtts.resConstraint = 0
SaveWindowAtts.width = 1240 
SaveWindowAtts.height = 800
##Options are: BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, 
##  POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
SaveWindowAtts.format = SaveWindowAtts.PNG
SetSaveWindowAttributes(SaveWindowAtts)

#Create a time slider
slider = CreateAnnotationObject("TimeSlider")
slider.text = ""
slider.height = 0.05
slider.width = 0.3
slider.position = (0.03, 0.94)
if(setvars["model"] == "fvcom"):
    tscale = 86400.
else:
    tscale = 1.
m = GetMetaData(setvars["db"])
totalstates = TimeSliderGetNStates()
istate = 0

for plot in which_plots:
    for var in leem_vars:
        #modify variable specific 'setvars'
        setvars['var'] = var['var']
        setvars['name'] = var['name']
        setvars['clim'] = var['clim']
        setvars['cmin'] = var['cmin']
        setvars['cmax'] = var['cmax']
        setvars['cmap'] = var['cmap']
        print(setvars)
        #Loop through all timesteps
        for state in range(totalstates):
            SetTimeSliderState(state)
            FILE_TS = "_" + str(state).zfill(4)
            if(setvars['slider']):
                slider.visible=1
            tcur = m.times[state]*tscale + t_start
            ts = datetime.datetime.utcfromtimestamp(tcur).strftime('%Y-%m-%d %H:%M:%S')
            timestamp = "Time: " + ts + " GMT"
            slider.text=timestamp
            if(plot=="3D"):
                pseudocolor_3D(setvars)
            elif(plot=="2Dslice"):
                pseudocolor_2Dslice(setvars)
            elif(plot=="transect"):
                pseudocolor_2Dtransect(setvars)
            else:
                sys.exit("No plot selected, check which_plots.  Options are 3D, 2D, or transect.  Exiting.")
            SaveWindowAtts.fileName = "/" + setvars["name"] + "/" + setvars["name"] + "_" + plot  + FILE_TS
            SetSaveWindowAttributes(SaveWindowAtts)
            SaveWindow()
            #ClearCacheForAllEngines()
            if(debug and state == dbreak):
                break    

DeleteAllPlots()    
close_file(setvars)

#Comment this out to leave VisIT CLI open after script is complete
sys.exit()

#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
