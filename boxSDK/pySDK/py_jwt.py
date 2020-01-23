from boxsdk import JWTAuth
from boxsdk import Client
from boxsdk import Client, OAuth2
from boxsdk import LoggingClient
import logging
import sys
import os
# import time

config_path='C:\\Users\\ischlesinger\\Code\\JWT_Server_Auth\\12922821_p90tqhsu_config.json'
sdk = JWTAuth.from_settings_file(config_path)
client = Client(sdk)

#Search automation_user box account for specified search-term:
word = input("What word are you searching for? ")
items = client.search().query(query=word, limit=100)
for item in items:
	print('The item ID is {0} and the item name is {1}'.format(item.id, item.name))

#Upload files from folder on Disk to Box.com:
source = 'C:\\users\\ischlesinger\\Desktop\\_sdkTest\\'
files = os.listdir(source)
folder_id = '101207809995'
for i in files:
    new_file = client.folder(folder_id).upload(source+i)
    print('File "{0}" uploaded to Box with file ID {1}'.format(new_file.name, new_file.id))
