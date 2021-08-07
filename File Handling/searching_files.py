# Searching Files

# Using String methods
# Using fnmatch
# Uisng glob
# Using Pathlib

import os 
import fnmatch
import glob
from pathlib import Path

folder = "D:/pyGuru/Youtube/File handling/sample/"

p = Path(folder)
for file in p.glob('*set*'):
	print(file)