# ffmpeg on Windows

To install ffmpeg on Windows, using an AWS EC2 instance (VM) with Windows Server, I did the following:

**Install miniconda**

(BTW I also used miniconda to install ffmpeg on both Linux and Mac.)

Download this installer and click on it to install:
https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

During installation, choose:
- Just Me
- All defaults

**Install ffmpeg and set paths**

From Windows start menu, open Anaconda Prompt.  Use conda to install ffmpeg:
```
conda install ffmpeg
```

Then check the paths to python, conda, and ffmpeg:
```
where python
where conda
where ffmpeg
```

To add python and conda to the system path, (so you can type it in MobaXterm), follow this video: 
https://www.youtube.com/watch?v=Xa6m1hJHba0. Similarly, add the path to ffmpeg, which should be something like
`C:\Users\yourusername\miniconda3\Library\bin`

**Run ffmpeg**

Open MobaXterm.  If you had it open before doing the above, exit and reopen to refresh the Path.

In MobaXterm, check that you have ffmpeg by doing
```
which ffmpeg
```

The ffmpeg scripts in visit-scripts/sample-movie-scripts have extra options, which all work at NCSU, and only some work on atmos.  To run them in different environments, you may need to remove some of the arguments. You can remove almost all of the optional arguments and still get a movie.

You don't need to run a script to make a movie. For example, if you have a directory ~/images filled with images with naming convention movieXXXX.png, with XXXX in logical numerical order, to make an mp4 movie named movie.mp4, you can do
```
cd ~/images
ffmpeg -framerate 15 -i movie%04d.png movie.mp4
```

Windows Media Player doesn't recognize the mp4 created avove, but Media Player Classic did - right click on the mp4 file and choose Open with Media Player Classic. In trying to figure out why it wasn't working (in WMP), I found a website which suggested I install this thing:
https://www.mediaplayercodecpack.com/standard/

Since I couldn't open the mp4 file, and I deleted the mp4 file before running ffmpeg again, I'm not even sure ffmpeg worked prior to installing that codec; the ffmpeg command seemed to run longer after that codec was installed. I also don't remember seeing the Media Player Classic option before installing it. I'd have to create a new VM and redo everything else (Moba, VisIt, Conda, ffmpeg, etc.) to test it, and then retest all of these steps.  Instead, You-Windows-Users please try this and compare notes.  The steps will likely vary between Windows software/OS versions.  Please open a GitHub issue and leave comments if you have suggestions on the topic, and I will add them to these instructions.

