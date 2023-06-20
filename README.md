# visit-scripts
VisIt scripts developed for FVCOM and SCHISM

There are 2 different things you can use the github scripts for:
1. Setting up the environment with a *start_* script so you can start off with good plot without having to click a bunch of stuff in the GUI
  - Try *start_fvcom_lm.py* using instructions for [Windows](Win10.md) or [Mac](MacStartup.md).
2. Creating images in batch mode for different types of plots for each variable (actually, SIT, RPOP, PO4T for now) at every single time step and making a movie from the images.  That can get very specific, and this github mostly holds 'my' stuff, usually in-progress.  The only thing tested and documented for use by others is [Instructions for running VisIt in batch mode to create images and movies for LEEM.](sample-movie-scripts/README_LE.MD)


## Contents

Scripts that define macros:
- setup_visit.py

Commands to cut and paste, starts with good default parameters for the file:
- start_fvcom_lm.py: FVCOM Lake Michigan Data.  Expected outputs are shown in [LM](LM.md). 
- start_fvcom_le.py: FVCOM Lake Erie Data.
- start_schism_mb.py: SCHISM Mobile Bay Data  Expected outputs are shown in [MB](MB.md). 
- start_schism_toy.py: SCHISM toy grid (from ECO-TOY)
- start_efdc_slre.py: EFDC-CGEM for St. Louis River Estuary
*Have a different dataset?  Scroll to the bottom for a Note.*

notes directory
- dates_reference has starting days of months
- ffmpeg.txt has ffmpeg command
- vars_reference.txt: how to define comparison variables, e.g., TP as a function of other variables

sample-movie-scripts directory
- [Instructions for running VisIt in batch mode to create images and movies for LEEM.](sample-movie-scripts/README_LE.MD)
- Other scripts are likely specific to my own files and without documentation on modifying them.

## Instructions for running

### Get the scripts
From the terminal (macOS or Linux) or MobaXterm (Windows), do
```
git clone https://github.com/l3-hpc/visit-scripts.git
cd visit-scripts
```

Here are more detailed [Windows instructions](Win10.md).

### Modify the paths
Before beginning, modify the start_XXX.py file for the location of these scripts and the data file.

For example, on Linux or Mac
```
##-- MODIFY -------------------
##--Set path to scripts----
SCRIPT_PATH = "/Users/yourusername/visit-scripts"
#Put the full path to the file
FILE_NAME = "/Users/yourusername/path-to-output-files/salinity_50.nc"
##-- END MODIFY ---------------
``` 

On Windows, it will look more like this:
```
##-- MODIFY -------------------
##--Set path to scripts----
SCRIPT_PATH = "C:\\Users\\yourusername\\visit-scripts\\"
#Put the full path to the file
FILE_NAME = "C:\\Users\\yourusername\\path-to-output-files\\salinity_50.nc"
##-- END MODIFY ---------------
``` 

Keep the script open, as you will cut and paste from it.

### Using VisIt
Open VisIt.

Launch the command line interface.  In the top VisIt nav bar:
- Controls:Launch CLI

A terminal (CLI command line) will pop up, looking something like (yours will probably be black):
![](VisItCLI.png)

From the start_ file, copy everything from `##----After modifying paths, BEGIN COPY---------------------` to `##---END COPY----------------##`.  Paste it in to the terminal at the prompt `>>>`.

Choose one of the plots.  Start with
```
create_pseudocolor_3Dplot(setvars)
```

Note: copy/paste to VisIt CLI doesn't work when using a VM.  Maybe you can fix the settings to make it work.  (If you do, let me know how.). Otherwise, you'll have to type.  It is not actually that much to type, if you ignore the comments.  See [Windows Instructions](Win10.md), **Run example script for LM**, to see the commands without comment lines and extra whitespace.

## Notes and troubleshooting
- On my Mac, I need to open VisIt from the command line, i.e., type `visit &` in the terminal, or it won't open the CLI from VisIt.  I suspect Xcode is the culprit, but I'm not sure.
- For SCHISM, the plugin needs to be installed.  For Windows, [download them from the VIMS website](http://ccrm.vims.edu/w/index.php/Visualization_with_VisIT). For Linux or Mac, follow my instructions on a fork of the [schism_visit_plugin](https://github.com/lisalenorelowe/schism_visit_plugin).
- For SCHISM, the starting date is hard coded to November 11, 2019.  I'll change it when I figure out how to pull that metadata from VisIt.  If you want to change it, it is in setup_visit.py.
- This is a work in progress, and there is little to no error checking so far. Open a GitHub Issue if you have questions, comments, concerns.  So far, my most common error is forgetting to put a comma after the variable in setvars when I change something.  Using wrong types (adding decimal to integer or mixing strings/bools/numbers) will also cause problems.

## Different dataset?

First: **The data must be 3D.**  

For SCHISM and FVCOM:
- Start by making a copy of a start_fvcom or start_schism file, rename it.
- You'll want to change the default parameters.  
-   Start by making a copy of a start_fvcom or start_schism file, rename it. 
-   It is mandatory that you set `var` to data that is actually in your dataset.  
-   Then, as a starting point, I recommend setting `clim` = 1, and `scale` = 1.

For **not** SCHISM or FVCOM
- create_pseudocolor_3Dplot will probably work, and probably create_psudocolor_2Dslice.
- Transects use the 3D mesh coordinate, the name of your mesh will be different. That would need to be modified in setup_visit.py.  Or comment out the mesh parts.  (In that case, let me know, so I can improve that script.  Ideally that script would be universal for common 3D data.)


**These instructions have only been tested on my Mac Studio with M1 chip for the 'start_' files provided.**
