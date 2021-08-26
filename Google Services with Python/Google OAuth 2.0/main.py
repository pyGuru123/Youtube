# Google OAuth 2.0 and OAuth consent screen

# authetication to google api services
# create oauth client secret file

# https://console.cloud.google.com/

# pip install pydrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1y5UdK6rIgLPp8vTR22323LCcbDbBIozzcJ'

file1 = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : 'hello2.txt'})
file1.SetContentString('Hello world!, this is my second file')
file1.Upload()