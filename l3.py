#l3 helper functions

## Plot attributes

#set defaults
setvars_salinity = {
#The filename
"db" : "filename",
#which year
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
#Print the legend, 0==False, 1==True
"legend" : 1,
"time" : 0,
"axes" : 0
}

#set defaults
setvars_temperature = {
#The filename
"db" : "filename",
#which year
"year" : 2019,
#The variable to be plotted
"var" : "temperature_depth_average",
#clim=0 means use default min/max for colormap
"clim" : 1,
#If clim=1, choose the min/max for colormap
"cmin" : 12,
"cmax" : 32,
#The colormap
"cmap" : "RdYlBu",
#Invert the colormap?
"invert" : 1,
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
#Print the legend, 0==False, 1==True
"legend" : 0,
"time" : 0,
"axes" : 0
}


## Date/Time indicies

#Valid model years
model_years = [
"2019"
]

#Define months
iJan = 0
iFeb = 1
iMar = 2
iApr = 3
iMay = 4
iJun = 5
iJul = 6
iAug = 7
iSep = 8
iOct = 9
iNov = 10
iDec = 11

which_months = [
"Jan",
"Feb",
"Mar",
"Apr",
"May",
"Jun",
"Jul",
"Aug",
"Sep",
"Oct",
"Nov",
"Dec"
]

which_vars = [
"salinity",
"temperature"
]

#Non leap year
range_year = [
(1,32),
(32,60),
(60,91),
(91,121),
(121,152),
(152,182),
(182,213),
(213,244),
(244,274),
(274,305),
(305,335),
(335,366)
]

#Leap year
range_leap_year = [
(1,32),
(32,61),
(60,92),
(92,122),
(122,153),
(153,183),
(183,214),
(214,245),
(245,275),
(275,306),
(306,336),
(336,367)
]
