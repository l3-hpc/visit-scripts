#Makes movies of cgem vars

#Plot CGEM
#plot_schism_cgem.py
##--Set path to scripts----
SCRIPT_PATH = "/rsstu/users/l/lllowe/tops/visit-scripts"
#
import os
#So it can find setup_visit.py
import sys
sys.path.append(SCRIPT_PATH)

from cgem_vars import *

#Put the full path, followed by '/'
#SCHISM outputs here: 
#filedir = "/rsstu/users/l/lllowe/cgem/sasj_bay_setup/outputs/"
filedir = "/rsstu/users/l/lllowe/cgem/cgem-real/outputs/"

#databases go here
dbfiles = "/rsstu/users/l/lllowe/tops/databases/"

#Check that output directory exists
if not os.path.exists(filedir):
    sys.exit("The directory " + filedir + " does not exist. Exiting.")
if not os.path.exists(dbfiles):
    sys.exit("The directory " + dbfiles + " does not exist. Exiting.")

istart = 1
iend = 13 

#Images are in separate directories for each varible
for var in cgem_vars:
    datafile = dbfiles + var['name'] + ".visit"
    f = open(datafile,"w")
    f = open(datafile,"a")
    print(datafile)
    for i in range(istart,iend):
        print(i)
        filepath = filedir + var['var'] + "_" + str(i) + ".nc"
        #Python f-string, filepath with newline
        f.write(f"{filepath}\n")
        print(filepath)
