#Makes movies of leem vars
#For the script to work, you must have ffmpeg installed and in the PATH

##--Set path to scripts----
SCRIPT_PATH = "/home/lllowe/visit-scripts"
import subprocess
#
import os
#So it can find setup_visit.py
import sys
sys.path.append(SCRIPT_PATH)

from leem_vars import *
from setpaths import *

#Put the full path, followed by '/'
#Main path to images
#This is in setpaths
#IMAGES = "/rsstu/users/l/lllowe/tops/images_1day/"

#Check that output directory exists
if not os.path.exists(IMAGES):
    sys.exit("The directory " + IMAGES + " does not exist. Exiting.")

#nframes = '1440'
nframes = '6'
start = '0'

#Images are in separate directories for each varible
for var in leem_vars:
    for iplot in which_plots:
        #-r is frame rate, how many images per second.  Increase to make the movie run faster.
        command = 'ffmpeg -y -r 60 -f image2 -s 1200x800 -start_number ' + start
        firstpath = os.path.join(IMAGES,var['name'])
        secondpath = os.path.join(firstpath, (var['name'] + '_' + iplot))
        filename = secondpath + '_%04d.png'
        moviename = os.path.join(IMAGES, (var['name'] + '_' + iplot + '.mp4'))
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
