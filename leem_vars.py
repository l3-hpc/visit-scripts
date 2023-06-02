#Definitions for LEEM runs
#leem_vars.py
#
#Python dictionaries for variables
#Defined below
#For example... 
#cgem_vars = [A1,Qn1,Qp1,Z1,Z2,NO3,NH4,PO4,DIC,O2,OM1A,OM2A,OM1Z,OM2Z,CDOM,Si,OM1BC,OM2BC,Alk,Tr]

SIT = {
"var" : "SIT",
"name" : "SIT",
"clim" : 1,
"cmin" : 0,
"cmax" : 3.,
"cmap" : "turbo"
}

RPOP = {
"var" : "RPOP",
"name" : "RPOP",
"clim" : 1,
"cmin" : 0,
"cmax" : 0.02,
"cmap" : "turbo"
}

PO4T = {
"var" : "PO4T",
"name" : "PO4T",
"clim" : 1,
"cmin" : 0,
"cmax" : 0.1,
"cmap" : "turbo"
}


#Python dictionary for variables
#for example...
#cgem_vars = [A1,Qn1,Qp1,Z1,Z2,NO3,NH4,PO4,DIC,O2,OM1A,OM2A,OM1Z,OM2Z,CDOM,Si,OM1BC,OM2BC,Alk,Tr]
leem_vars = [SIT,RPOP,PO4T]
which_plots = ["3D","2Dslice","transect"]
#If debug is True, it will plot only the first dbreak+1 timesteps
debug = True
dbreak = 5 
