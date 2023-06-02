#Plot CGEM
#plot_schism_cgem.py

##--Set path to scripts----
##On my Mac:
#SCRIPT_PATH = "/Users/lllowe/visit-scripts"
#On Hazel:
SCRIPT_PATH = "/rsstu/users/l/lllowe/tops/visit-scripts"

import os
#So it can find setup_visit.py
import sys 
sys.path.append(SCRIPT_PATH)

from visit import *
import l3v 
#Defines cgem_vars, the state variables (A1, Qn1, etc.), and which_plots
from cgem_vars import * 
#Defines OUTPUTS, USE_DB, DBFILES, IMAGES directories
from setpaths import *

#Argument is array number for plot variable 
ivar = int(sys.argv[1])
var = cgem_vars[ivar]
print(var)
#sys.exit()


#Check that output directory exists
if not os.path.exists(OUTPUTS):
    sys.exit("The directory " + OUTPUTS + " does not exist. Exiting.")

#Since there will be a large number of images, create directories for each variable
#Create a directory for images if one doesn't exist.
#Note, existing files will be overwritten
IMGS_DIR = IMAGES + var['name']
if not os.path.exists(IMGS_DIR):
    os.makedirs(IMGS_DIR)

#set defaults
setvars = {
#The filename
"db" : OUTPUTS + 'GEN_1_1.nc',
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
#"cfore" : (255, 255, 255, 255),
#black
"cfore" : (0, 0, 0, 255),
#Background, black
"cback" : (255, 255, 255, 255), 
#Print the legend, time, axes, slider 0==False, 1==True
"legend" : 1,
"time" : 0,
"axes" : 0,
"slider" : 0
}

SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = IMAGES
SaveWindowAtts.fileName = "salt"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
SaveWindowAtts.width = 1024 
SaveWindowAtts.height = 1024 
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.None  # None, PackBits, Jpeg, Deflate, LZW
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.pixelData = 1
SetSaveWindowAttributes(SaveWindowAtts)

#Create a title 
title = CreateAnnotationObject("Text2D")
title.text = ""
title.position = (0.04, 0.93)

# Begin spontaneous state
#View2DAtts = View2DAttributes()
#View2DAtts.windowCoords = (-88.5502, -87.6843, 30.107, 31.085)
#View2DAtts.viewportCoords = (0, 1, 0, 1)
#View2DAtts.fullFrameActivationMode = View2DAtts.On  # On, Off, Auto
#View2DAtts.fullFrameAutoThreshold = 100
#View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
#View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
#View2DAtts.windowValid = 1
#SetView2D(View2DAtts)
# End spontaneous state

for iplot in which_plots:
    print(iplot)

    if(USE_DB):
        DATABASE = DBFILES + var['name'] + '.visit' 
    else:
        DATABASE = OUTPUTS + var['var'] + '_1.nc'
    print(DATABASE)

    OpenDatabase(DATABASE,0,"SCHISM")

    setvars['var'] = var['var'] + iplot
    setvars['name'] = var['name']
    setvars['clim'] = var['clim']
    setvars['cmin'] = var['cmin']
    setvars['cmax'] = var['cmax']
    setvars['cmap'] = var['cmap']

    #sys.exit()

    SaveWindowAtts.outputDirectory = IMAGES + setvars['name']
    SetSaveWindowAttributes(SaveWindowAtts)

    #istart usually 0
    istart = 0
    #change if you want less...
    #istart = TimeSliderGetNStates() - 10
 
    for state in range(istart,TimeSliderGetNStates()):
#    for state in range(2):
        TimeSliderSetState(state)
        title.text = setvars['name']
        #Annotations
        AnnotationAtts = AnnotationAttributes()
        #Don't print out username and name of database
        AnnotationAtts.userInfoFlag = 0
        AnnotationAtts.databaseInfoFlag = 0
        #White foreground 
        AnnotationAtts.foregroundColor = setvars['cfore'] 
        #Black background
        AnnotationAtts.backgroundColor = setvars['cback']
        #AnnotationAtts.axes2D.xAxis.title.visible = 1
        AnnotationAtts.legendInfoFlag = setvars['legend'] 
        AnnotationAtts.timeInfoFlag = 0
        AnnotationAtts.axes2D.visible = 0
        AnnotationAtts.axes2D.xAxis.title.visible = 0
        AnnotationAtts.axes2D.yAxis.title.visible = 0
        AnnotationAtts.axes2D.xAxis.label.visible = 0
        AnnotationAtts.axes2D.yAxis.label.visible = 0
        AnnotationAtts.axes3D.visible = 0
        SetAnnotationAttributes(AnnotationAtts)
    
        #Create the plot
        AddPlot("Pseudocolor", setvars["var"], 1, 1)
        SetActivePlots(0)
    
        #Set plot attributes
        PseudocolorAtts = PseudocolorAttributes()
        PseudocolorAtts.minFlag = setvars["clim"]
        PseudocolorAtts.maxFlag = setvars["clim"]
        PseudocolorAtts.colorTableName = setvars["cmap"]
        PseudocolorAtts.min = setvars["cmin"]
        PseudocolorAtts.max = setvars["cmax"]
        SetPlotOptions(PseudocolorAtts)
    
        #Draw the plot
        DrawPlots()
    
        FILENAME = setvars['name'] + iplot + "_" +  str(state).zfill(6)
        SaveWindowAtts.fileName = FILENAME
        SetSaveWindowAttributes(SaveWindowAtts)
        SaveWindow()

        DeleteAllPlots()

        ClearCacheForAllEngines()


    CloseDatabase(DATABASE)
    
sys.exit()
