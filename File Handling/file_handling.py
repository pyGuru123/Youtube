# File handling with python

# Creating folders
# Changing current working directory
# Listing directory content
# Fetching file information
# Traversing directory

import os  
import time

for path, dir, file in os.walk('D:/pyGuru/Youtube/File handling/'):
	print(path)
	for d in dir:
		print(d)

	for f in file:
		print(f)

	print()