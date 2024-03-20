# Callback to update timestamp for every new timestep
# Place this python code in ~/.visit/visitrc before starting VisIt.
# Four separate callbacks are registered for forward step, backward step and slider set 
# of the GUI's VCR controls. There is a bit of a problem with the 'play' button mode.   
# There is NO callback action associated with each step of the 'play' mode. So, handling 
# that requires using the WidnowInformation callback. VisIt will wind up queueing up all 
# the callbacks until playing is stopped.

# line 42: start time of simulation needs to be changed accordingly.

import datetime
import calendar

def UpdateTimestamp(arg):
    global lastState
    global t_start
    currentState = arg.timeSliderCurrentStates[0]
    if currentState != lastState:
        try:
            m = GetMetaData(arg.activeSource)
            # time:format = "modified julian day (MJD)", so multiply by seconds in a day
            tcur = m.times[currentState]*86400.  + t_start
            ts = datetime.datetime.utcfromtimestamp(tcur).strftime('%Y-%m-%d %H:%M:%S')
            timestamp = "Time: " + ts + " GMT"
            annot_obj = GetAnnotationObject("Slider") # find out names by GetAnnotationObjectNames() 
            annot_obj.text =  timestamp
            annot_obj.position = (0.03, 0.94)
            annot_obj.height = 0.05
            annot_obj.fontBold = 1
            lastState = currentState
        except:
            return

def onSetTimeSliderState0():
    UpdateTimestamp(GetWindowInformation())

def onSetTimeSliderState1(timeState):
    UpdateTimestamp(GetWindowInformation())

def onWindowInformation(arg):
    UpdateTimestamp(arg)

#time:units = "days since 1858-11-17 00:00:00" ;
#		time:format = "modified julian day (MJD)" ;
t_start = calendar.timegm(datetime.datetime(1858, 11, 17, 0, 0, 0).timetuple())
lastState = -1
RegisterCallback("SetTimeSliderStateRPC", onSetTimeSliderState1)
RegisterCallback("TimeSliderNextStateRPC", onSetTimeSliderState0)
RegisterCallback("TimeSliderPreviousStateRPC", onSetTimeSliderState0)
RegisterCallback("WindowInformation", onWindowInformation)
