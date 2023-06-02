#Definitions for CGEM SCHISM runs
#cgem.py
#
#Python dictionaries for variables
#Defined below 
#cgem_vars = [A1,Qn1,Qp1,Z1,Z2,NO3,NH4,PO4,DIC,O2,OM1A,OM2A,OM1Z,OM2Z,CDOM,Si,OM1BC,OM2BC,Alk,Tr]

A1 = {
"var" : "GEN_1",
"name" : "A1",
"clim" : 1,
"cmin" : 6e7,
"cmax" : 1e8,
"cmap" : "turbo"
}

Qn1 = {
"var" : "GEN_2",
"name" : "Qn1",
"clim" : 1,
"cmin" : 1.53e-10,
"cmax" : 6.85e-9,
"cmap" : "turbo"
}


Qp1 = {
"var" : "GEN_3",
"name" : "Qp1",
"clim" : 1,
"cmin" : 1.07e-11,
"cmax" : 4.28e-10,
"cmap" : "turbo"
}


Z1 = {
"var" : "GEN_4",
"name" : "Z1",
"clim" : 1,
"cmin" : 1,
"cmax" : 300,
"cmap" : "turbo"
}

Z2 = {
"var" : "GEN_5",
"name" : "Z2",
"clim" : 1,
"cmin" : 1,
"cmax" : 3000,
"cmap" : "turbo"
}


NO3 = { 
"var" : "GEN_6",
"name" : "NO3",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

NH4 = {
"var" : "GEN_7",
"name" : "NH4",
"clim" : 1,
"cmin" : 0,
"cmax" : 5,
"cmap" : "turbo"
}

PO4 = {  
"var" : "GEN_8",
"name" : "PO4",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

DIC = {
"var" : "GEN_9",
"name" : "DIC",
"clim" : 1,
"cmin" : 1000,
"cmax" : 3000,
"cmap" : "turbo"
}

O2 = {
"var" : "GEN_10",
"name" : "O2",
"clim" : 1,
"cmin" : 0,
"cmax" : 300,
"cmap" : "turbo"
}

OM1A = {
"var" : "GEN_11",
"name" : "OM1A",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM2A = {
"var" : "GEN_12",
"name" : "OM2A",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM1Z = {
"var" : "GEN_13",
"name" : "OM1Z",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM2Z = {
"var" : "GEN_14",
"name" : "OM2Z",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM1R = {
"var" : "GEN_15",
"name" : "OM1R",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM2R = {
"var" : "GEN_16",
"name" : "OM2R",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

CDOM = {
"var" : "GEN_17",
"name" : "CDOM",
"clim" : 1,
"cmin" : 0,
"cmax" : 2,
"cmap" : "turbo"
}

Si = {
"var" : "GEN_18",
"name" : "Si",
"clim" : 1,
"cmin" : 0,
"cmax" : 20,
"cmap" : "turbo"
}

OM1BC = {
"var" : "GEN_19",
"name" : "OM1BC",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

OM2BC = {
"var" : "GEN_20",
"name" : "OM2BC",
"clim" : 1,
"cmin" : 0,
"cmax" : 10,
"cmap" : "turbo"
}

Alk = {
"var" : "GEN_21",
"name" : "Alk",
"clim" : 1,
"cmin" : 0,
"cmax" : 3000,
"cmap" : "turbo"
}

Tr = {
"var" : "GEN_22",
"name" : "Tr",
"clim" : 1,
"cmin" : .999,
"cmax" : 1.001,
"cmap" : "turbo"
}

#Scripts calling this function will loop through the following:
#cgem_vars = [A1,Qn1,Qp1,Z1,Z2,NO3,NH4,PO4,DIC,O2,OM1A,OM2A,OM1Z,OM2Z,CDOM,Si,OM1BC,OM2BC,Alk,Tr]
#cgem_vars = [A1,O2]
#cgem_vars = [Salt,Temp]
cgem_vars = [Salt,Temp,A1,Qn1,Qp1,Z1,Z2,NO3,NH4,PO4,DIC,O2,OM1A,OM2A,OM1Z,OM2Z,CDOM,Si,Alk,Tr]
which_plots = ['_surface','_near_bottom','_depth_average']

