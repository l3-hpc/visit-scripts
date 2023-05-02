RestoreSessionWithDifferentSources("/Users/lllowe/LakeErie/VisItSessionFiles/3D.moving.session", 0, ("/Users/lllowe/LakeErie/DATA/TP_NCSU.nc")) 

ResetView()

TimeSliderNextState()
TimeSliderNextState()
TimeSliderNextState()


# Begin spontaneous state
c0 = View3DAttributes()
c0.viewNormal = (0, 0, 1)
c0.focus = (484789, 4.66739e+06, -36966.9)
c0.viewUp = (0, 1, 0)
c0.viewAngle = 30
c0.parallelScale = 212311
c0.nearPlane = -424622
c0.farPlane = 424622
c0.imagePan = (0, 0)
c0.imageZoom = 1
c0.perspective = 0
c0.centerOfRotationSet = 0
c0.centerOfRotation = (484789, 4.66739e+06, -36966.9)
c0.axis3DScaleFlag = 0
c0.axis3DScales = (1, 1, 1)

c1 = View3DAttributes()
c1.viewNormal = (0, 0, 1)
c1.focus = (484789, 4.66739e+06, -36966.9)
c1.viewUp = (0, 1, 0)
c1.viewAngle = 30
c1.parallelScale = 212311
c1.nearPlane = -424622
c1.farPlane = 424622
c1.imagePan = (0, 0)
c1.imageZoom = 1.77156
c1.perspective = 0
c1.centerOfRotationSet = 0
c1.centerOfRotation = (484789, 4.66739e+06, -36966.9)
c1.axis3DScaleFlag = 0
c1.axis3DScales = (1, 1, 1)

c2 = View3DAttributes()
c2.viewNormal = (0.268274, -0.919027, 0.288823)
c2.focus = (484789, 4.66739e+06, -36966.9)
c2.viewUp = (0.0819944, 0.320509, 0.94369)
c2.viewAngle = 30
c2.parallelScale = 212311
c2.nearPlane = -424324
c2.farPlane = 424324
c2.imagePan = (0, 0)
c2.imageZoom = 1.77156
c2.perspective = 0
c2.centerOfRotationSet = 0
c2.centerOfRotation = (484789, 4.66739e+06, -35906.6)
c2.axis3DScaleFlag = 0
c2.axis3DScales = (1, 1, 1)

# Begin spontaneous state
c3 = View3DAttributes()
c3.viewNormal = (0.236634, -0.824846, -0.513453)
c3.focus = (484789, 4.66739e+06, -36966.9)
c3.viewUp = (0.096296, -0.505949, 0.857171)
c3.viewAngle = 30
c3.parallelScale = 212311
c3.nearPlane = -424238
c3.farPlane = 424238
c3.imagePan = (0, 0)
c3.imageZoom = 1.77156
c3.perspective = 0  
c3.centerOfRotationSet = 0
c3.centerOfRotation = (484789, 4.66739e+06, -36156)
c3.axis3DScaleFlag = 0
c3.axis3DScales = (1, 1, 1)
# End spontaneous state


c4 = View3DAttributes()
c4.viewNormal = (0.152081, -0.345591, 0.92598)
c4.focus = (484789, 4.66739e+06, -36966.9)
c4.viewUp = (-0.575845, 0.730459, 0.367195)
c4.viewAngle = 30
c4.parallelScale = 212311
c4.nearPlane = -424238
c4.farPlane = 424238
c4.imagePan = (0, 0)
c4.imageZoom = 1.77156
c4.perspective = 0
c4.centerOfRotationSet = 0
c4.centerOfRotation = (484789, 4.66739e+06, -36156)
c4.axis3DScaleFlag = 0
c4.axis3DScales = (1, 1, 1)

c5 = c4

cpts = (c0, c1, c2, c3, c4, c5)

x = []

for i in range(7):
    x = x + [float(i) / float(6.)]

                                        
nSteps=200
for i in range(nSteps):
    t = float(i) / float(nSteps-1)
    v = EvalCubicSpline(t,x,cpts)
    SetView3D(v)
    TimeSliderNextState()

TimeSliderNextState()
TimeSliderNextState()
HideActivePlots()
TimeSliderNextState()
TimeSliderNextState()
