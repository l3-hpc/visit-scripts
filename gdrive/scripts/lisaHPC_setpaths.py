#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4
##macOS paths on local machine

#Now set the paths!:
#This is probably 'mi_', but can be anything where the FVCOM output is for example
## [file_prefix_epa][4 integers padded by zeros].nc
file_prefix_epa = "mi_"
file_prefix_compare = "mi_"

#The directory where the mi_XXXX.nc files are located.  The slash at the end of the directory name is required.
EPA_directory = "/rsstu/users/l/lllowe/ord/WORK/fvcom/run/output.0/"
COMPARE_directory = "/rs1/researchers/l/lllowe/ORD/FVCOM/ftp/mi_gem_archive/041820163/"
#The directory to write images to.  The slash at the end of the directory name is required.
IMGS_DIR =  "/rsstu/users/l/lllowe/cgem/IMG_BATCH/"


#----- Do not modify unless developing code --------
#These are based on previous definitions, do not modify
base_EPA_database = EPA_directory + file_prefix_epa
base_COMPARE_database = COMPARE_directory + file_prefix_compare
base_conn_string = r"conn_cmfe(<" + EPA_directory + file_prefix_epa

#from pathlib import Path, for Python 3
#Path(IMGS_DIR).mkdir(parents=True, exist_ok=True)

#But now VisIt is using Python2
import os
import sys

#Check that all the directories exist
if not os.path.exists(EPA_directory):
    sys.exit("The directory " + EPA_directory + " does not exist.  Check definition of EPA_directory in setpaths.py. Exiting.")
    if not os.path.exists(COMPARE_directory):
        sys.exit("The directory " + COMPARE_directory + " does not exist.  Check definition of COMPARE_directory in setpaths.py. Exiting.")

#Create a directory for images if one doesn't exist.
#Note, existing files will be overwritten
if not os.path.exists(IMGS_DIR):
    os.makedirs(IMGS_DIR)

def set_EPA_path():
    return base_EPA_database

def set_COMPARE_path():
    return base_COMPARE_database

def set_conn_string():
    return base_conn_string

def set_image_path():
    return IMGS_DIR

#To edit with Vim, use this
#:set tabstop=8 expandtab shiftwidth=4 softtabstop=4

