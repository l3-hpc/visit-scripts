#Makes movies of cgem vars

#Plot CGEM
#plot_schism_cgem.py
##--Set path to scripts----
SCRIPT_PATH = "/rsstu/users/l/lllowe/tops/visit-scripts"
import subprocess
#
import os
#So it can find setup_visit.py
import sys
sys.path.append(SCRIPT_PATH)

from cgem_vars import *
from setpaths import *

#Put the full path, followed by '/'
#Main path to images
#This is in setpaths
#IMAGES = "/rsstu/users/l/lllowe/tops/images_1day/"

#Check that output directory exists
if not os.path.exists(IMAGES):
    sys.exit("The directory " + IMAGES + " does not exist. Exiting.")

#nframes = '1440'
nframes = '13700'
start = '0'
which_plots = ['']

#Images are in separate directories for each varible
for var in cgem_vars:
    for iplot in which_plots:
        #-r is frame rate, how many images per second.  Increase to make the movie run faster.
        command = 'ffmpeg -y -r 60 -f image2 -s 1200x800 -start_number ' + start
        filename = IMAGES + var['name'] + "/" + var['name'] + iplot + '_%06d.png'
        moviename = IMAGES + var['name'] + iplot + '.mp4'
        command = command + ' -i ' + filename
        command = command + ' -vframes ' + nframes + ' -vcodec libx264 -crf 25 -pix_fmt yuv420p '
        command = command + moviename 
        print(command)
        exitcode = subprocess.call(command,shell=True)
        if exitcode != 0:
            print('Error, exit code:',exitcode)
            print('Command:')
            print(command)
            sys.exit()
    
 
#ffmpeg -y -r 15 -f image2 -s 1200x800 -start_number $start -i $dirname/$filename%04d.$suffix -vframes $nframes -vcodec libx264 -crf 25  -pix_fmt yuv420p ./$filename.mp4
