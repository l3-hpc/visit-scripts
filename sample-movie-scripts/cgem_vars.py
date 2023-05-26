#filename
FILE_NAME = "peanut"

#Python dictionary for variables
cgem_list = [A1,Qn1,Qp1,Z1,Z2,NO3,NH4,PO4,DIC,O2,OM1A,OM2A,OM1Z,OM2Z,CDOM,Si,OM1BC,OM2BC,Alk,Tr]

A1 = {
"var" : "GEN_1",
"clim" : 1,
"cmin" : 6e7,
"cmax" : 1e8,
"cmap" : "turbo"
}

Qn1 = {
"var" : "GEN_2",
"clim" : 1,
"cmin" : 1.53e-10,
"cmax" : 6.85e-9,
"cmap" : "turbo"
}


Qp1 = {
"var" : "GEN_3",
"clim" : 1,
"cmin" : 1.07e-11,
"cmax" : 4.28e-10,
"cmap" : "turbo"
}


Z1 = {
"var" : "GEN_4",
"clim" : 1,
"cmin" : 1,
"cmax" : 300,
"cmap" : "turbo"
}

Z2 = {
"var" : "GEN_5",
"clim" : 1,
"cmin" : 1,
"cmax" : 3000,
"cmap" : "turbo"
}


NO3 = { 
"var" : "GEN_6",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

NH4 = {
"var" : "GEN_7",
"clim" : 1,
"cmin" : 0,
"cmax" : 5,
"cmap" : "turbo"
}

PO4 = {  
"var" : "GEN_8",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

DIC = {
"var" : "GEN_9",
"clim" : 1,
"cmin" : 1000,
"cmax" : 3000,
"cmap" : "turbo"
}

O2 = {
"var" : "GEN_10",
"clim" : 1,
"cmin" : 0,
"cmax" : 300,
"cmap" : "turbo"
}

OM1A = {
"var" : "GEN_11",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM2A = {
"var" : "GEN_12",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM1Z = {
"var" : "GEN_13",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM2Z = {
"var" : "GEN_14",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM1R = {
"var" : "GEN_15",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM2R = {
"var" : "GEN_16",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

CDOM = {
"var" : "GEN_17",
"clim" : 1,
"cmin" : 0,
"cmax" : 2,
"cmap" : "turbo"
}

Si = {
"var" : "GEN_18",
"clim" : 1,
"cmin" : 0,
"cmax" : 20,
"cmap" : "turbo"
}

OM1BC = {
"var" : "GEN_19",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM2BC = {
"var" : "GEN_20",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

Alk = {
"var" : "GEN_21",
"clim" : 1,
"cmin" : 0,
"cmax" : 3000,
"cmap" : "turbo"
}

Tr = {
"var" : "GEN_21",
"clim" : 1,
"cmin" : .999,
"cmax" : 1.001,
"cmap" : "turbo"
}

setvars = {
#The filename
"db" : FILE_NAME,
#The variable to be plotted
"var" : "GEN_1",
#clim=0 means use default min/max for colormap
"clim" : 1,
#If clim=1, choose the min/max for colormap
"cmin" : 3e5,
"cmax" : 1e9,
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
#schism, fvcom, or efdc
"model" : "schism"
}

for var in cgem_vars:
    setvars['var'] = var['var']
    setvars['clim'] = var['clim']
    setvars['cmin'] = var['cmin']
    setvars['cmax'] = var['cmax']
    setvars['cmap'] = var['cmap']
    


