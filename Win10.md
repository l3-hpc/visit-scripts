# Test on Windows VM

## Install MobaXterm

Install MobaXterm, see these text instructions which include a link to a video tutorial. [Install MobaXterm](https://hpc.ncsu.edu/Documents/mobaxterm.php?ref=login)

After opening MobaXterm for the first time, install nano:
```
apt-get install nano -y
```

Follow the instructions in the MobaXterm video to change the home directory

## Install VisIt

These scripts were tested with VisIt 3.1.4.  Download [VisIt 3.1.4 for Windows](https://github.com/visit-dav/visit/releases/download/v3.1.4/visit3.1.4_x64.exe).

## Clone this repo

From MobaXterm, do:
```
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



