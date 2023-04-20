# visit-scripts
VisIt scripts developed for FVCOM and SCHISM

## Contents

Scripts that define macros:
- setup_visit.py

Commands to cut and paste, starts with good default parameters for the file:
- start_fvcom_lm.py: FVCOM Lake Michigan Data 
- start_schism_mb.py: SCHISM Mobile Bay Data

If you have a different dataset, you'll want to change the default parameters.  Start by making a copy of a start script. It is mandatory that you set `var` to data that is actually in your dataset.  Then, as a starting point, I recommend setting `clim` = 1, and `scale` = 1.  **The data must be 3D.**  Also, if your mesh is called something different from the norm for FVCOM or SCHISM, that will need to be modified in setup_visit.py.  (In that case, let me know, so I can improve that script.  Ideally that script would be universal for 3D data.)

## Instructions for running

Before beginning, modify the start_XXX.py file for the location of these scripts and the data file.  

For example:
```
##-- MODIFY -------------------
##--Set path to scripts----
SCRIPT_PATH = "/Users/lllowe/visit-scripts"
#Put the full path to the file
FILE_NAME = "/Users/lllowe/A-SCHISM/salinity_50.nc"
##-- END MODIFY ---------------
``` 

Keep the script open, as you will cut and paste from it.

Open VisIt.

Launch the command line interface.  In the top VisIt nav bar:
- Controls:Launch CLI

A terminal should open with
```
>>>
```

Copy everything from "BEGIN COPY" to "END COPY".  Paste it in to the terminal.  There is no error checking yet.  (Sorry.)

Choose one of the plots.  Start with
```
create_pseudocolor_3Dplot(setvars)
```

## Notes and troubleshooting
- On my Mac, I need to open VisIt from the command line, i.e., type `visit &` in the terminal, or it won't open the CLI from VisIt.  I suspect Xcode is the culprit, but I'm not sure.
- For SCHISM, the plugin needs to be installed.  For Windows, [download them from the VIMS website](http://ccrm.vims.edu/w/index.php/Visualization_with_VisIT). For Linux or Mac, follow my instructions on a fork of the [schism_visit_plugin](https://github.com/lisalenorelowe/schism_visit_plugin).
- For SCHISM, the starting date is hard coded to November 11, 2019.  I'll change it when I figure out how to pull that metadata from VisIt.  If you want to change it, it is in setup_visit.py.
- This is a work in progress, and there is little to no error checking so far. Open a GitHub Issue if you have questions, comments, concerns.  So far, my most common error is forgetting to put a comma after the variable in setvars when I change something.  Using wrong types (adding decimal to integer or mixing strings/bools/numbers) will also cause problems.


**These instructions have only been tested on my Mac Studio with M1 chip for SCHISM MB and FVCOM LM.**
