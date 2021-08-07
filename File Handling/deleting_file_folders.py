# Deleting files and folders

# Deleting files
# Deleting empty folders
# Deleting directory tree
# safely deleting files with send2trash

# Installing send2trash :  pip install send2trash

import os   
import shutil
import send2trash

file= os.path.normpath("D:/pyGuru/Youtube/File handling/sample/alpha/")
send2trash.send2trash(file)

