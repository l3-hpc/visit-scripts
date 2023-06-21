# ffmpeg on Windows

To install ffmpeg on Windows, using an AWS EC2 instance (VM) with Windows Server, I did the following:

**Install miniconda**

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

Open MobaXterm.  If you had it open before doing the above, exit and reopen.

In MobaXterm, check that you have ffmpeg by doing
```
which ffmpeg
```

The ffmpeg scripts in visit-scripts/sample-movie-scripts have extra options, which all work at NCSU, and only some work on atmos.  
You can just remove most of those arguments.  I did a test by creating ~120 png images named movie0XXX.png, and from the directory that had the images, did the following simplified ffmpeg command:
ffmpeg -framerate 15 -i movie%04d.png movie.mp4

Windows Media Player wouldn't play it, but Media Player classic did, and in trying to figure why it wasn't working (in WMP), I found this website, which led me to install this thing:
https://www.mediaplayercodecpack.com/standard/

I'm not even sure the ffmpeg command worked before I installed that codec.  I'd have to create a new VM and redo everything else (Moba, Conda, etc.) to test it, and then retest all of these steps.  You-Windows-Users please try this and compare notes.  It's going to depend on many things, all of them specific to Windows.  I'm a let y'all troubleshoot further, if you don't mind.

