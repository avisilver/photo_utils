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
import glob

class DATE_FORMATS:
    DATE='date'
    MONTH='month'
    YEAR='yaer'


def main(date_format=DATE_FORMATS.DATE, verbose = False, merge=True):
    print ("Running with options date_format={0}, merge={1}, verbose={2}".format(
        date_format, merge, verbose))
    directory = '.'
    matches = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.gif', '.png', '.avi', '.mp4', '.thm', '.mov')):
                full_name = os.path.join(root, filename)
                if os.path.isfile(full_name):
                    matches += [full_name]

    if verbose:
        print ("matches:\n{0}".format(matches))


    date_formatters = {
        DATE_FORMATS.DATE: lambda t: "%04d-%02d-%02d" % (t.tm_year, t.tm_mon, t.tm_mday),
        DATE_FORMATS.MONTH: lambda t: "%04d-%02d" % (t.tm_year, t.tm_mon),
        DATE_FORMATS.YEAR: lambda t: "%04d" % (t.tm_year),
    }
    date_format_fn = date_formatters[date_format]

    for full_name in matches:
        base_name = ntpath.basename(full_name)
        if verbose:
            print ("-" * 45 + '\n')
            print("Full name={0}, basename={1}".format(full_name, base_name))
        ftime = time.gmtime(os.path.getmtime(full_name))
        #ctime_dir = str(ftime.tm_year) + '-' + str(ftime.tm_mon) + '-' + str(ftime.tm_mday)
        ctime_dir = date_format_fn(ftime)

        if merge:
            # Merge into a single directory that matches the beginning of the generated
            # date directory, eg 2017-12*
            matching_dirs = glob.glob(ctime_dir + '*')
            if len(matching_dirs) == 1:
                dest_dir = matching_dirs[0]
            else:
                dest_dir = ctime_dir

        # Create a new directory if it does not exist
        if not os.path.isdir(dest_dir):
            os.mkdir(dest_dir)
            print ("Created destination directory", dest_dir)

        print(dest_dir)
        dest_path = os.path.join(dest_dir, base_name)

        if os.path.realpath(full_name) == os.path.realpath(dest_path):
            print('Skipping file' , full_name)
        else:
            shutil.move(full_name, dest_path)
            print('File' , full_name , 'has been moved to' , dest_path)



if __name__ == '__main__':
    if '-h' in sys.argv:
        print ("""
        -h    Print this help
        -m    Month folder format (default is date including day)
        -y    Year folder format (default is date including day)
        -n    New folder mode - do not merge in to a single prefix matching date folder
        """)
        exit
    date_format = 'date'
    if '-m' in sys.argv:
        date_format = DATE_FORMATS.MONTH
    elif  '-y' in sys.argv:
        date_format = DATE_FORMATS.YEAR
    verbose = '-v' in sys.argv
    merge = '-n' not in sys.argv

    main(date_format=date_format, verbose=verbose, merge=merge)
