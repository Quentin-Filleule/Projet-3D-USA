import subprocess
import os
from pathlib import Path
import os , os.path
import sys
import shutil

############################################ Disclaimer !!!! #############################################################################
# Befor start this pipeline, you have to be use the virtual env
# To do that you have to be in the main directory (Pannellum)
# source 3dproj/bin/activate
# 3dproj is the name of my Venv
##########################################################################################################################################
os.chdir("..")

dir = os.getcwd()

#####################  Delete previous files  ############################################################################################
modif = "Opensfm/OpenSfM/data/berlin/undistorted/depthmaps/*"
temp = os.path.join(dir,modif) 
fct =  "rm -r " + temp
os.system(fct)

modif = "Opensfm/OpenSfM/data/berlin/undistorted/images/*"
temp = os.path.join(dir,modif) 
fct =  "rm -r " + temp
os.system(fct)

modif = "Opensfm/OpenSfM/data/berlin/reports/features/*"
temp = os.path.join(dir,modif) 
fct =  "rm -r " + temp
os.system(fct)

modif = "Opensfm/OpenSfM/data/berlin/matches/*"
temp = os.path.join(dir,modif) 
fct =  "rm -r " + temp
os.system(fct)

modif = "Opensfm/OpenSfM/data/berlin/features/*"
temp = os.path.join(dir,modif) 
fct =  "rm -r " + temp
os.system(fct)

modif = "json/reconstruction.json*"
temp = os.path.join(dir,modif) 
fct =  "rm -r " + temp
os.system(fct)

modif = "Opensfm/OpenSfM/data/berlin/exif/*"
temp = os.path.join(dir,modif) 
fct =  "rm -r " + temp
os.system(fct)

modif = "Opensfm/OpenSfM/data/berlin/images/*"
temp = os.path.join(dir,modif) 
fct =  "rm -r " + temp
os.system(fct)

##########################################################################################################################################


# Copy the images in the directory img in Opensf
modif = "img/*"
modif1 = "Opensfm/OpenSfM/data/berlin/images"
temp = os.path.join(dir,modif) 
temp1 = os.path.join(dir,modif1) 
fct =  "cp -R " + temp + " " + temp1
os.system(fct)

# Use the OpenSFM script 
os.chdir(dir)
os.chdir('Opensfm/OpenSfM')

os.system("bin/opensfm_run_all data/berlin")
os.system("bin/opensfm undistort data/berlin")
os.system("bin/opensfm compute_depthmaps data/berlin")

os.chdir(dir)

# Copy the reconstruction file in our json direcory
modif = "Opensfm/OpenSfM/data/berlin/reconstruction.json"
modif1 = "json"
temp = os.path.join(dir,modif) 
temp1 = os.path.join(dir,modif1) 
fct =  "cp " + temp + " " + temp1
os.system(fct)


# Extract all the Data that we need in a new json
os.chdir("py")

# Extract all the shots' names
os.system("python3 ./extractJson.py")

# Save coordinate of neightbor in json
os.system("python3 ./sortPoints.py")

# Estimate coordinate of cameras
os.system("python3 ./estimateCoordinate.py")



# In case we need to see the result in OpenSFM viewver
"""
os.chdir(dir)
os.chdir('Opensfm/OpenSfM')

# Open local server to use the OpenSFM viewer
os.system("python3 viewer/server.py -d data/berlin")

"""