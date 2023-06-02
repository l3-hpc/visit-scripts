
# Run LEEM for Lake Erie

## Get the repo
To run scripts to plot some variables from Baseline, first, get this repo and cd to it:
```
git clone https://github.com/l3-hpc/visit-scripts
cd visit-scripts
```

## Change paths

**visit-scripts/setpaths.py**

Open the file `setpaths.py`, and change these.  Script path is wherever you cloned this repo, OUTPUTS is where Baseline file is, and IMAGES is where you want the images to go.  The directory will be created if it does not exist, and will be written over if it does exist.
```
SCRIPT_PATH = "/Users/lllowe/visit-scripts"
OUTPUTS = "/Users/lllowe/LakeErie/DATA/"
IMAGES = "/Users/lllowe/LakeErie/images-leem/"
```

**visit-scripts/sample-movie-scripts/plot_all_timesteps_le.py**

Go to the sample-movie-scripts directory
```
cd sample-movie-scripts
```
and open `plot_all_timesteps_le.py`.  The SCRIPT_PATH needs to be defined again, so it can find your setpaths.py (sorry).  Modify :
```
##--Set path to scripts----
SCRIPT_PATH = "/Users/lllowe/visit-scripts"
```
If your file is "Baseline_2013_0001.nc", then you don't need to modify anything else!

**visit-scripts/sample-movie-scripts/ffmpeg_leem.py**

Once again, in `ffmpeg_leem.py`, set SCRIPT_PATH:
```
##--Set path to scripts----
SCRIPT_PATH = "/Users/lllowe/visit-scripts"
```

## Check out the variables
You do not need to modify anything to run the script.  I recommend **not** modifying anything until you do a test run.

But open the file `visit-scripts/leem_vars.py` to take a look.  I define a dictionary for 3 leem variables, SIT, RPOP, and PO4T and chose min/max based on the first 6 test plots.  It will plot 3 types of plots for each variable.

The script loops over all timesteps, but for testing, I added a 'debug'.  If debug is True, the loop will break after a specified number of timesteps (dbreak+1).







