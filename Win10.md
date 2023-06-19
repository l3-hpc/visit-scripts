# Test start_ scripts on AWS Windows VM

## Install MobaXterm

Install MobaXterm: see these text instructions which include a link to a video tutorial. [Install MobaXterm](https://hpc.ncsu.edu/Documents/mobaxterm.php?ref=login)

Follow the instructions or video to change the MobaXterm perisistent home directory to `C:\Users\yourusername` (change yourusername to your actual username).

After opening MobaXterm for the first time, install nano:
```
apt install nano -y
```

## Install VisIt

These scripts were tested with VisIt 3.1.4.  Download [VisIt 3.1.4 for Windows](https://github.com/visit-dav/visit/releases/download/v3.1.4/visit3.1.4_x64.exe) and install.

## Clone this repo

From MobaXterm, do:
```
cd
git clone https://github.com/l3-hpc/visit-scripts.git
```

Change to the visit-scripts directory and check the contents
```
cd visit-scripts
ls
```

## Get sample Lake Michigan data

From MobaXterm, do:
```
wget https://renc.osn.xsede.org/ees210015-bucket01/testvisit/mi_0013.nc
```

Check size, it should be 383.4M
```
ls -lh mi_0013.nc
```

## Run example script for LM

For full instructions on using the 'start' scripts, see the [README](README.md).

To test, for your convienience, just copy and paste these, after modifying yourusername.  This should open a 3D plot.
```
SCRIPT_PATH = "C:\\Users\\yourusername\\visit-scripts\\"
FILE_NAME = "C:\\Users\\yourusername\\visit-scripts\\mi_0013.nc"
import sys 
sys.path.append(SCRIPT_PATH)
from visit import *
from setup_visit import *
setvars = {"db" : FILE_NAME,"var" : "TP","clim" : 1,"cmin" : 0.002,"cmax" : 0.008,"cmap" : "turbo","scale" : 1000,"percent" : 35,"from_x" : 560998.31,"from_y" : 4767358.50,"to_x" : 539195.69,"to_y" : 4765827.50,"model" : "fvcom"}
open_file(setvars)
create_pseudocolor_3Dplot(setvars)
```

And then you can try:
```
create_pseudocolor_2Dslice(setvars)
create_pseudocolor_2Dtransect(setvars)
transect_against_3D(setvars)
```

After confirming the above works, close VisIt, and try again using the instructions in the [README](README.md).

Use the text editor nano to modify the start_ scripts, i.e.,
```
cd
cd visit-scripts
nano start_fvcom_lm.py
```
Then edit the following lines, substituting your username.
```
SCRIPT_PATH = "C:\\Users\\yourusername\\visit-scripts\\"
FILE_NAME = "C:\\Users\\yourusername\\visit-scripts\\mi_0013.nc"
```
From nano, to save, do `Ctrl X`,`Y`,`Enter`.

## Troubleshooting

If you aren't sure what your username is, from MobaXterm, do
```
whoami
```

Make sure that you have set the MobaXterm 'home' directory properly to `C:\Users\yourusername` by checking the Windows File folders. 

If everything went according to plan, you will see the git-cloned visit-scripts in `C:\Users\yourusername` , and mi_0013.nc will be in the visit-scripts directory.  

See below for what this should look like.  I am using a Windows VM from AWS, so my username is "Administrator".  (You should not run as administrator on your machine.). 

![](windowsdir.png)
