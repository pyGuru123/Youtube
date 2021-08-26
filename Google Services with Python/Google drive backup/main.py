# Google drive backup

# Upload files to google drive
# List files in google drive
# Download files from google drive

# pip install pydrive

import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1y5UdK6rIgLPp8vTR2LC1244DbBIozzcJ'

# Upload files
directory = "D:/pyGuru/Youtube/Google services/Google drive backup/data"
for f in os.listdir(directory):
	filename = os.path.join(directory, f)
	gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
	gfile.SetContentFile(filename)
	gfile.Upload()

# Download files
file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
for index, file in enumerate(file_list):
	print(index+1, 'file downloaded : ', file['title'])
	file.GetContentFile(file['title'])