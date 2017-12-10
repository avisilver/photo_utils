#!/usr/bin/env python3
################################################
# Copyright (c) Avi Silver 2015
# Recursively move all photographs from subdirectories into folders
#  with the creation time of the files
# Licensed under the terms of the GNU General Public License, version 3 (GPL-3.0)
# http://opensource.org/licenses/GPL-3.0

import os
import time
import shutil
import sys
import ntpath

verbose = False

directory = '.'
matches = []
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.gif', '.png', '.avi', '.mp4')):
            full_name = os.path.join(root, filename)
            if os.path.isfile(full_name):
                matches += [full_name]
            
if verbose: print (matches)
                
date_format = """%04d-%02d-%02d"""

for full_name in matches:
    base_name = ntpath.basename(full_name)
    print((full_name, base_name))
    ftime = time.gmtime(os.path.getmtime(full_name))
    #ctime_dir = str(ftime.tm_year) + '-' + str(ftime.tm_mon) + '-' + str(ftime.tm_mday)
    ctime_dir = date_format % (ftime.tm_year, ftime.tm_mon, ftime.tm_mday)
    if not os.path.isdir(ctime_dir):
        os.mkdir(ctime_dir)
    print(ctime_dir)
    dst = os.path.join(ctime_dir, base_name)

    if os.path.realpath(full_name) == os.path.realpath(dst):
        print(('Skipping file' , full_name))
    else:
        shutil.move(full_name, dst)
        print(('File' , full_name , 'has been moved to' , dst))
        




