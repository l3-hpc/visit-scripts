#!/bin/bash
#BSUB -n 32 
#BSUB -R span[hosts=1]
#BSUB -W 2:00 
#BSUB -q short
#BSUB -J ffmpeg 
#BSUB -o ffmpeg_out.%J
#BSUB -e ffmpeg_err.%J
#module load ffmpeg
python ffmpeg.py
