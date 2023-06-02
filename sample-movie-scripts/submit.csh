#!/bin/tcsh
#BSUB -n 2
#BSUB -q short
#BSUB -R span[ptile=2]
#BSUB -W 2:00 
#BSUB -J visit 
#BSUB -o stdout.%J
#BSUB -e stderr.%J
module load visit/3.1.4-mesa
visit -cli -nowin -s hazel_plot_cgem.py
