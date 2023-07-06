import subprocess
import os
from pathlib import Path
import os , os.path
import sys
import shutil

os.chdir("..")
dir = os.getcwd()

#####################  Delete previous files  ###############################################################################
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

"""
os.system("rm -r /mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM/data/berlin/undistorted/images/*")
os.system("rm -r /mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM/data/berlin/reports/features/*")
os.system("rm -r /mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM/data/berlin/matches/*")
os.system("rm -r /mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM/data/berlin/features/*")
os.system("rm -r /mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM/data/berlin/exif/*")
os.system("rm -r /mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/json/reconstruction.json")


os.system("rm -r /mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM/data/berlin/images/*")
os.system("cp -R /mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/img/* /mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM/data/berlin/images")

os.chdir('/mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM')

os.system("/mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM/bin/opensfm_run_all data/berlin")
os.system("/mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM/bin/opensfm undistort data/berlin")
os.system("/mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM/bin/opensfm compute_depthmaps data/berlin")

os.system("cp /mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM/data/berlin/reconstruction.json /mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/json")


os.chdir('/mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/py')
os.system("python3 ./extractJson.py")

os.system("python3 ./estimateCoordinate.py")

os.chdir('/mnt/c/Users/Quentin/Desktop/Cours/Stage_USA/Summer23/Pannellum/Opensfm/OpenSfM')

os.system("python3 viewer/server.py -d data/berlin")

"""