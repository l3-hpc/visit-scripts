#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

from visit import *

#To calculate normal vector for defining transect
import numpy as np

#Time slider
import datetime
import calendar

#Initialize Time slider
global lastState
global MJD
global t_start
lastState = -1
#MJD = True
#if(MJD):
#    t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
#else:
#    t_start = 1572566400

#Create a time slider
slider = CreateAnnotationObject("TimeSlider")
slider.text = ""
slider.height = 0.05
slider.width = 0.3
slider.position = (0.03, 0.94)

#This is called if 'step'ping through time, but not 'play'    
def UpdateTimestamp(arg):
    global lastState
    global MJD
    global t_start
    currentState = arg.timeSliderCurrentStates[0]
    if currentState != lastState:
        try:
            m = GetMetaData(arg.activeSource)
            if(MJD):
                # time:format = "modified julian day (MJD)", so multiply by seconds in a day
                tcur = m.times[currentState]*86400.  + t_start
            else:
                tcur = m.times[currentState] + t_start
            ts = datetime.datetime.utcfromtimestamp(tcur).strftime('%Y-%m-%d %H:%M:%S')
            timestamp = "Time: " + ts + " GMT"
            annot_obj = GetAnnotationObject("TimeSlider1") # find out names by GetAnnotationObjectNames()
            annot_obj.text =  timestamp
            lastState = currentState
        except:
            return

def onSetTimeSliderState0():
    UpdateTimestamp(GetWindowInformation())

def onSetTimeSliderState1(timeState):
    UpdateTimestamp(GetWindowInformation())

def onWindowInformation(arg):
    UpdateTimestamp(arg)

#Create a 3D pseudocolor plot
def create_pseudocolor_3Dplot(setvars):
    DeleteAllPlots()

    #Annotations
    AnnotationAtts = AnnotationAttributes()
    #Don't print out username and name of database
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    #Turn of 3D axes
    AnnotationAtts.axes3D.visible = 0
    #White background
    AnnotationAtts.backgroundColor = (255, 255, 255, 255)
    #Black Foreground
    AnnotationAtts.foregroundColor = (0, 0, 0, 255)
    #AnnotationAtts.axes2D.xAxis.title.visible = 1
    SetAnnotationAttributes(AnnotationAtts)

    #Create the plot
    AddPlot("Pseudocolor", setvars["var"], 1, 1)
    SetActivePlots(0)

    #Scale in Z
    AddOperator("Transform",1)
    TransformAtts = TransformAttributes()
    TransformAtts.doRotate = 0
    TransformAtts.rotateOrigin = (0, 0, 0)
    TransformAtts.rotateAxis = (0, 0, 1)
    TransformAtts.rotateAmount = 0
    TransformAtts.rotateType = TransformAtts.Deg  # Deg, Rad
    TransformAtts.doScale = 1
    TransformAtts.scaleOrigin = (0, 0, 0)
    TransformAtts.scaleX = 1
    TransformAtts.scaleY = 1
    TransformAtts.scaleZ = setvars["scale"]
    SetOperatorOptions(TransformAtts, 0, 1)

    #If using SCHISM, get rid of junk values
    if(setvars["schism"]):
        AddOperator("Threshold", 1)
        ThresholdAtts = ThresholdAttributes()
        ThresholdAtts.outputMeshType = 0
        ThresholdAtts.boundsInputType = 0
        ThresholdAtts.listedVarNames = (setvars["var"])
        ThresholdAtts.zonePortions = (0)
        ThresholdAtts.lowerBounds = (-1e+37)
        ThresholdAtts.upperBounds = (1e+37)
        ThresholdAtts.defaultVarName = setvars["var"]
        ThresholdAtts.defaultVarIsScalar = 1
        ThresholdAtts.boundsRange = ("-1e+37:1e+37")
        SetOperatorOptions(ThresholdAtts, 1, 1)

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


def create_pseudocolor_2Dslice(setvars):
    DeleteAllPlots()

    ##Just for 2D
    #Axes are on
    AnnotationAtts = AnnotationAttributes()
    #Don't print out username and name of database
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    #get rid of x-y-x axis thing in the bottom left
    AnnotationAtts.axes3D.triadFlag = 0
    #White background
    AnnotationAtts.backgroundColor = (255, 255, 255, 255)
    #Black Foreground
    AnnotationAtts.foregroundColor = (0, 0, 0, 255)
    #Turn on 2D axes
    AnnotationAtts.axes2D.visible = 1
    ##x-axis labeling is fine for slices 
    AnnotationAtts.axes2D.xAxis.title.visible = 1
    AnnotationAtts.axes2D.xAxis.label.visible = 1
    #For y-axis, we want depth, but VisIt relabels it
    AnnotationAtts.axes2D.yAxis.title.visible = 0
    SetAnnotationAttributes(AnnotationAtts)

    #Create plot
    AddPlot("Pseudocolor", setvars["var"], 1, 1)

    #Scale in Z
    AddOperator("Transform",1)
    TransformAtts = TransformAttributes()
    TransformAtts.scaleZ = setvars["scale"]
    SetOperatorOptions(TransformAtts, 0, 1)

    #If using SCHISM, get rid of junk values
    if(setvars["schism"]):
        AddOperator("Threshold", 1)
        ThresholdAtts = ThresholdAttributes()
        ThresholdAtts.outputMeshType = 0
        ThresholdAtts.boundsInputType = 0
        ThresholdAtts.listedVarNames = (setvars["var"])
        ThresholdAtts.zonePortions = (0)
        ThresholdAtts.lowerBounds = (-1e+37)
        ThresholdAtts.upperBounds = (1e+37)
        ThresholdAtts.defaultVarName = setvars["var"]
        ThresholdAtts.defaultVarIsScalar = 1
        ThresholdAtts.boundsRange = ("-1e+37:1e+37")
        SetOperatorOptions(ThresholdAtts, 1, 1)

    #Full frame
    View2DAtts = View2DAttributes()
    View2DAtts.fullFrameActivationMode = View2DAtts.On  # On, Off, Auto
    View2DAtts.fullFrameAutoThreshold = 100
    SetView2D(View2DAtts)
    ResetView()

    #Add a slice in Y by percent
    AddOperator("Slice", 1)
    SliceAtts = SliceAttributes()
    SliceAtts.originType = SliceAtts.Percent
    SliceAtts.originPercent = setvars["percent"] 
    SliceAtts.project2d = 1
    SetOperatorOptions(SliceAtts, 1, 1)

    #Set plot attributes
    SetActivePlots(0)
    SetViewExtentsType("actual")
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.minFlag =setvars["clim"] 
    PseudocolorAtts.maxFlag = setvars["clim"]
    PseudocolorAtts.colorTableName = setvars["cmap"] 
    PseudocolorAtts.min = setvars["cmin"] 
    PseudocolorAtts.max =  setvars["cmax"]
    SetPlotOptions(PseudocolorAtts)

    #Draw the plot
    DrawPlots()

def create_pseudocolor_2Dtransect(setvars):
    DeleteAllPlots()

    #Annotations
    #For 2D, Axes are on
    AnnotationAtts = AnnotationAttributes()
    #Don't print out username and name of database
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    #get rid of x-y-x axis thing in the bottom left
    AnnotationAtts.axes3D.triadFlag = 0
    #White background
    AnnotationAtts.backgroundColor = (255, 255, 255, 255)
    #Black Foreground
    AnnotationAtts.foregroundColor = (0, 0, 0, 255)
    #Turn on 2D axes
    AnnotationAtts.axes2D.visible = 1
    ##x-axis labeling is fine for slices 
    AnnotationAtts.axes2D.xAxis.title.visible = 1
    AnnotationAtts.axes2D.xAxis.label.visible = 1
    #For y-axis, we want depth, but VisIt relabels it
    AnnotationAtts.axes2D.yAxis.title.visible = 0
    SetAnnotationAttributes(AnnotationAtts)

    #Calculate arbitrary normal vector from plane
    p1 = np.array([setvars["from_x"],setvars["from_y"],0])
    p2 = np.array([setvars["to_x"],setvars["to_y"], 0])
    p3 = np.array([setvars["to_x"],setvars["to_y"], -1000])
    X = np.array([p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2]])
    Y = np.array([p3[0]-p1[0],p3[1]-p1[1],p3[2]-p1[2]])
    myvec = np.cross(X,Y)
    norm_myvec = myvec/np.linalg.norm(myvec)

    #Set up 3D plot
    AddPlot("Pseudocolor", setvars["var"], 1, 1)
    #Scale Z
    AddOperator("Transform",1)
    TransformAtts = TransformAttributes()
    TransformAtts.scaleZ = setvars["scale"]
    SetOperatorOptions(TransformAtts, 0, 1)

    #If using SCHISM, get rid of junk values
    if(setvars["schism"]):
        AddOperator("Threshold", 1)
        ThresholdAtts = ThresholdAttributes()
        ThresholdAtts.outputMeshType = 0
        ThresholdAtts.boundsInputType = 0
        ThresholdAtts.listedVarNames = (setvars["var"])
        ThresholdAtts.zonePortions = (0)
        ThresholdAtts.lowerBounds = (-1e+37)
        ThresholdAtts.upperBounds = (1e+37)
        ThresholdAtts.defaultVarName = setvars["var"]
        ThresholdAtts.defaultVarIsScalar = 1
        ThresholdAtts.boundsRange = ("-1e+37:1e+37")
        SetOperatorOptions(ThresholdAtts, 1, 1)

    #Full frame
    View2DAtts = View2DAttributes()
    View2DAtts.fullFrameActivationMode = View2DAtts.On  # On, Off, Auto
    View2DAtts.fullFrameAutoThreshold = 100
    SetView2D(View2DAtts)
    ResetView()

    #Select Box
    AddOperator("Box", 1)
    BoxAtts = BoxAttributes()
    BoxAtts.amount = BoxAtts.Some  # Some, All
    BoxAtts.minx = min(p1[0],p2[0])  
    BoxAtts.maxx = max(p1[0],p2[0]) 
    BoxAtts.miny = min(p1[1],p2[1])
    BoxAtts.maxy = max(p1[1],p2[1]) 
    BoxAtts.minz = -250000
    BoxAtts.maxz = 0
    BoxAtts.inverse = 0
    SetOperatorOptions(BoxAtts, 2, 1)

    #Add Slice
    AddOperator("Slice", 1)
    SliceAtts = SliceAttributes()
    SliceAtts.originType = SliceAtts.Point  # Point, Intercept, Percent, Zone, Node
    SliceAtts.originPoint = (p1[0], p1[1], p1[2])
    SliceAtts.originIntercept = 0
    SliceAtts.originPercent = 0
    SliceAtts.originZone = 0
    SliceAtts.originNode = 0
    SliceAtts.normal = (norm_myvec[0], norm_myvec[1], norm_myvec[2])
    SliceAtts.axisType = SliceAtts.Arbitrary  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
    SliceAtts.upAxis = (0, 0, 1)
    SliceAtts.project2d = 1
    SliceAtts.interactive = 1
    SliceAtts.flip = 0
    SliceAtts.originZoneDomain = 0
    SliceAtts.originNodeDomain = 0
    SliceAtts.meshName = "Bathymetry_Mesh"
    if(setvars["schism"]):
        SliceAtts.meshName = "3D_Mesh"
    SliceAtts.theta = 0
    SliceAtts.phi = 0
    SetOperatorOptions(SliceAtts, 1, 1)

    #Zoom to boxed transect region
    SetViewExtentsType("actual")
    SetActivePlots(0)

    #Plot attributes
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.minFlag = setvars["clim"] 
    PseudocolorAtts.maxFlag = setvars["clim"] 
    PseudocolorAtts.colorTableName = setvars["cmap"]
    PseudocolorAtts.min = setvars["cmin"]
    PseudocolorAtts.max = setvars["cmax"]
    SetPlotOptions(PseudocolorAtts)

    #Draw the plot
    DrawPlots()

def transect_against_3D(setvars):
    DeleteAllPlots()

    #Annotations
    AnnotationAtts = AnnotationAttributes()
    #Don't print out username and name of database
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    #Turn of 3D axes
    AnnotationAtts.axes3D.visible = 0
    #Black background
    AnnotationAtts.backgroundColor = (0, 0, 0, 255)
    #White Foreground
    AnnotationAtts.foregroundColor = (255, 255,255, 255)
    #AnnotationAtts.axes2D.xAxis.title.visible = 1
    SetAnnotationAttributes(AnnotationAtts)

    #Calculate arbitrary normal vector from plane
    p1 = np.array([setvars["from_x"],setvars["from_y"],0])
    p2 = np.array([setvars["to_x"],setvars["to_y"],0])
    p3 = np.array([setvars["to_x"],setvars["to_y"], -1000])
    X = np.array([p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2]])
    Y = np.array([p3[0]-p1[0],p3[1]-p1[1],p3[2]-p1[2]])
    myvec = np.cross(X,Y)
    norm_myvec = myvec/np.linalg.norm(myvec)

    #Add plot
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

    #Scale Z
    #Scale in Z
    AddOperator("Transform",1)
    TransformAtts = TransformAttributes()
    TransformAtts.doRotate = 0
    TransformAtts.rotateOrigin = (0, 0, 0)
    TransformAtts.rotateAxis = (0, 0, 1)
    TransformAtts.rotateAmount = 0
    TransformAtts.rotateType = TransformAtts.Deg  # Deg, Rad
    TransformAtts.doScale = 1
    TransformAtts.scaleOrigin = (0, 0, 0)
    TransformAtts.scaleX = 1
    TransformAtts.scaleY = 1
    TransformAtts.scaleZ = setvars["scale"]
    SetOperatorOptions(TransformAtts, 0, 1)

    #Add Mesh Plot with the same attributes
    if(setvars["schism"]):
        AddPlot("Mesh", "3D_Mesh", 1, 1)
    else:
        AddPlot("Mesh", "SigmaLayer_Mesh", 1, 1)        


    #Change the color and opacity of mesh
    SetActivePlots(1)
    MeshAtts = MeshAttributes()
    MeshAtts.legendFlag = 1
    MeshAtts.lineWidth = 0
    MeshAtts.meshColor = (128, 128, 128, 255)
    MeshAtts.meshColorSource = MeshAtts.MeshCustom  # Foreground, MeshCustom, MeshRandom
    MeshAtts.opaqueColorSource = MeshAtts.Background  # Background, OpaqueCustom, OpaqueRandom
    MeshAtts.opaqueMode = MeshAtts.Auto  # Auto, On, Off
    MeshAtts.pointSize = 0.05
    MeshAtts.opaqueColor = (255, 255, 255, 255)
    MeshAtts.smoothingLevel = MeshAtts.None  # None, Fast, High
    MeshAtts.pointSizeVarEnabled = 0
    MeshAtts.pointSizeVar = "Default"
    MeshAtts.pointType = MeshAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    MeshAtts.showInternal = 0
    MeshAtts.pointSizePixels = 2
    MeshAtts.opacity = 0.333333
    SetPlotOptions(MeshAtts)

    #If using SCHISM, get rid of junk values
    if(setvars["schism"]):
        SetActivePlots(0)
        AddOperator("Threshold", 1)
        ThresholdAtts = ThresholdAttributes()
        ThresholdAtts.outputMeshType = 0
        ThresholdAtts.boundsInputType = 0
        ThresholdAtts.listedVarNames = (setvars["var"])
        ThresholdAtts.zonePortions = (0)
        ThresholdAtts.lowerBounds = (-1e+37)
        ThresholdAtts.upperBounds = (1e+37)
        ThresholdAtts.defaultVarName = setvars["var"]
        ThresholdAtts.defaultVarIsScalar = 1
        ThresholdAtts.boundsRange = ("-1e+37:1e+37")
        SetOperatorOptions(ThresholdAtts, 1, 1)

    #Select Box, hopefully to just the Active Plots
    #SetActivePlots((0, 1))
    SetActivePlots(0)
    AddOperator("Box", 0)
    BoxAtts = BoxAttributes()
    BoxAtts.amount = BoxAtts.Some  # Some, All
    BoxAtts.minx = min(p1[0],p2[0])
    BoxAtts.maxx = max(p1[0],p2[0])
    BoxAtts.miny = min(p1[1],p2[1])
    BoxAtts.maxy = max(p1[1],p2[1])
    BoxAtts.minz = -250000
    BoxAtts.maxz = 0
    BoxAtts.inverse = 0
    SetOperatorOptions(BoxAtts, 1, 0)

    #Add slicing, do NOT project to 2D
    AddOperator("Slice", 0)
    SliceAtts = SliceAttributes()
    SliceAtts.originType = SliceAtts.Point  # Point, Intercept, Percent, Zone, Node
    SliceAtts.originPoint = (p1[0], p1[1], p1[2])
    SliceAtts.originIntercept = 0
    SliceAtts.originPercent = 0
    SliceAtts.originZone = 0
    SliceAtts.originNode = 0
    SliceAtts.normal = (norm_myvec[0], norm_myvec[1], norm_myvec[2])
    SliceAtts.axisType = SliceAtts.Arbitrary  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
    SliceAtts.upAxis = (0, 0, 1)
    #do not project to 2d
    SliceAtts.project2d = 0
    SliceAtts.interactive = 1
    SliceAtts.flip = 0
    SliceAtts.originZoneDomain = 0
    SliceAtts.originNodeDomain = 0
    SliceAtts.meshName = "Bathymetry_Mesh"
    if(setvars["schism"]):
        SliceAtts.meshName = "3D_Mesh"
    SliceAtts.theta = 0
    SliceAtts.phi = 0
    #I need to look up what that means
    SetOperatorOptions(SliceAtts, 2, 0)

    #Draw the plot
    DrawPlots()

def open_file(setvars):
    global MJD
    global t_start
#if(MJD):
#    t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
#else:
#    t_start = 1572566400
    if(setvars["schism"]):
        OpenDatabase(setvars["db"],0,"SCHISM")
        MJD = False 
        t_start = 1572566400
    else:
        OpenDatabase(setvars["db"],0,"")
        MJD = True
        t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())


#RegisterCallback executes a function when something happens in the GUI 
RegisterCallback("SetTimeSliderStateRPC", onSetTimeSliderState1)
RegisterCallback("TimeSliderNextStateRPC", onSetTimeSliderState0)
RegisterCallback("TimeSliderPreviousStateRPC", onSetTimeSliderState0)
RegisterCallback("WindowInformation", onWindowInformation)

#RegisterMacro executes a function when you type the name at the command line
RegisterMacro("create_pseudocolor_3Dplot",create_pseudocolor_3Dplot)
RegisterMacro("create_create_pseudocolor_2Dslice",create_pseudocolor_2Dslice)
RegisterMacro("create_pseudocolor_2Dtransect",create_pseudocolor_2Dtransect)
RegisterMacro("transect_against_3D",transect_against_3D)
RegisterMacro("open_file",open_file)

#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
