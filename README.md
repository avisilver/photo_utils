# photo_utils
Simple photo file utility

## Usage:


|OS|command|status|
|--------|-----------------------------------------------------|----|
|Windows | python move_files-to_date_folders.py|Working|
|Linux   | ./move_files-to_date_folders.py|Untested|

## Effects

Creates a folder per day at the directory of execution, with the format YYYY-MM-DD
Moves all files with the common photograph extensions '.jpg', '.jpeg', '.gif', '.png', '.avi' from all recursive subdirectories of the execution directory to the day folder corresponding to the file's modification time



## TODO:

 1. Option to use photograph date per exif data in file
 2. Option to choose date format of output directories, including month or year groupings as well as day
 3. Input and output directory options.
