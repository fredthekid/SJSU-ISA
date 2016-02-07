#!/usr/bin/env python
import os
import zipfile
import shutil
from os import listdir
from os.path import isfile, join, exists

#Declaring Variables
sub_zip = "submissions.zip"
download_path = "/home/fred/Downloads/"
new_dir = "/home/fred/CmpE126_TA/HW/HW8/"

#Create Desired Directory for files to be moved to
if not os.path.exists(new_dir): 
    os.makedirs(new_dir)

#Move Downloaded Zip into Desired Directory
shutil.copy(download_path+sub_zip, new_dir)

#Unzip Downloaded Zip
with zipfile.ZipFile(new_dir + sub_zip, "r") as z:
    z.extractall(new_dir)

#Remove submissions.zip
os.remove(new_dir+sub_zip)

#Get names of all zip files
zip_files = [ f for f in listdir(new_dir) if isfile(join(new_dir,f)) ]

#Iterate throuh each zip file
#Create dir (if not exists) 
#mv zip file in to dir
#unzip
#remove zip
for zip_file in zip_files:
    name_dir = zip_file.split('_')[0]
    if not os.path.exists(new_dir + name_dir):
        print "Making " + name_dir
        os.makedirs(new_dir + name_dir)

    shutil.move(new_dir+zip_file, new_dir+name_dir)
    try:
        with zipfile.ZipFile(new_dir + name_dir + "/" + zip_file) as z:
            z.extractall(new_dir+name_dir)
    
    except:
        print "Count not unzip " + zip_file

    os.remove(new_dir + name_dir + "/" + zip_file)

