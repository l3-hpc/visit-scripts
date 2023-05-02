#VisIt script to make movie starting from session file
import sys

#Define an output directory
OUTDIR = "/Users/lllowe/AA-Movies/streamlines"
#Define a base file name
BASE_FILENAME = "tempwstream"
#The file name, ifile is the couter
#FILENAME = BASE_FILENAME + str(ifile).zfill(4)

RestoreSessionWithDifferentSources("/Users/lllowe/temp_with_streamlines_noannotation.session", 0, ("localhost:/Users/lllowe/A-ORD/leem_wilson.nc"))
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.000690066, -0.000217751, 1)
View3DAtts.focus = (484789, 4.66739e+06, -60255.6)
View3DAtts.viewUp = (-0.00149866, 0.999999, 0.000218785)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 218748
View3DAtts.nearPlane = -436527
View3DAtts.farPlane = 436527
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (484789, 4.66739e+06, -61907.2)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

ViewAxisArrayAtts = ViewAxisArrayAttributes()
ViewAxisArrayAtts.domainCoords = (0, 1)
ViewAxisArrayAtts.rangeCoords = (0, 1)
ViewAxisArrayAtts.viewportCoords = (0, 1, 0, 1)
SetViewAxisArray(ViewAxisArrayAtts)


#for ifile in range(8762):

for ifile in range(600):

    FILENAME = BASE_FILENAME + str(ifile).zfill(4)

    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.outputDirectory = OUTDIR
    SaveWindowAtts.fileName = FILENAME
    SaveWindowAtts.family = 0
    SaveWindowAtts.format = SaveWindowAtts.PPM  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
    SaveWindowAtts.width = 3840 
    SaveWindowAtts.height = 2160 
    SaveWindowAtts.screenCapture = 0
    SaveWindowAtts.saveTiled = 0
    SaveWindowAtts.quality = 80
    SaveWindowAtts.progressive = 0
    SaveWindowAtts.binary = 0
    SaveWindowAtts.stereo = 0
    SaveWindowAtts.compression = SaveWindowAtts.None  # None, PackBits, Jpeg, Deflate, LZW
    SaveWindowAtts.forceMerge = 0
    SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
    SaveWindowAtts.pixelData = 3
    SaveWindowAtts.advancedMultiWindowSave = 0
    SaveWindowAtts.subWindowAtts.win1.position = (0, 0)
    SaveWindowAtts.subWindowAtts.win1.size = (128, 128)
    SaveWindowAtts.subWindowAtts.win1.layer = 0
    SaveWindowAtts.subWindowAtts.win1.transparency = 0
    SaveWindowAtts.subWindowAtts.win1.omitWindow = 0
    SaveWindowAtts.opts.types = ()
    SaveWindowAtts.opts.help = ""
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()
    if(ifile != 8761):
        TimeSliderNextState()
    if(ifile%200 == 0):
        ClearCacheForAllEngines()

sys.exit()
