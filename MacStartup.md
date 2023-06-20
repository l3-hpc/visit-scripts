# Test Lake Michigan startup script

## Install VisIt

These scripts were tested with VisIt 3.1.4.  Download [VisIt 3.1.4 for Mac](https://github.com/visit-dav/visit/releases/download/v3.1.4/visit3.1.4.darwin-x86_64-10_14.dmg) and install.

## Clone this repo

From Terminal, do:
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

From Terminal, do:
```
wget https://renc.osn.xsede.org/ees210015-bucket01/testvisit/mi_0013.nc
```

If your Mac doesn't have `wget`, then do:
```
curl https://renc.osn.xsede.org/ees210015-bucket01/testvisit/mi_0013.nc -o mi_0013.nc
```

Check size, it should be 383.4M
```
ls -lh mi_0013.nc
```

## Run example script for LM

For full instructions on using the 'start' scripts, see the [README](README.md), but to test, use the commands below.  

Make sure you are in the correct directory, and check your path by doing:
```
cd ~/visit-scripts
pwd
```

The following commands are meant to be pasted in the VisIt CLI.  To get that, open VisIt and launch the command line interface by doing the following:
- In the top VisIt nav bar, click Controls:Launch CLI

A terminal (CLI command line) will pop up, looking something like (yours will probably be black):
![](VisItCLI.png)

To test, for your convienience, just copy and paste these, after modifying `yourusername`.  (Check the PATH matches what you found above.)  This should open a 3D plot, similar to the first image on [LM](LM.md).
```
SCRIPT_PATH = "/Users/yourusername/visit-scripts"
FILE_NAME = "/Users/yourusername/visit-scripts/mi_0013.nc"
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

Use the text editor nano to modify the start_ scripts, e.g.,
```
cd
cd visit-scripts
nano start_fvcom_lm.py
```
Then edit the following lines, substituting your actual username for `yourusername`.
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

See below for what this should look like, sorted by Size.  I am using a Windows VM from AWS, so my username is "Administrator".  (You should not run as administrator on your machine.). 
