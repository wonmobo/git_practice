from boxsdk import JWTAuth
from boxsdk import Client
from boxsdk import Client, OAuth2
from boxsdk import LoggingClient
from boxsdk.exception import BoxAPIException
import logging
import sys
import os
# import time

config_path='C:\\Users\\ischlesinger\\Code\\JWT_Server_Auth\\12922821_p90tqhsu_config.json'
sdk = JWTAuth.from_settings_file(config_path)
client = Client(sdk)

###Search automation_user box account for specified search-term:
#word = input("What word are you searching for? ")
#items = client.search().query(query=word, limit=100)
#for item in items:
#	print('The item ID is {0} and the item name is {1}'.format(item.id, item.name))

###Upload files from folder on Disk to Box.com. If file with same name exists, update file:
source = 'C:\\users\\ischlesinger\\Desktop\\_sdkTest\\'
files_in_src = os.listdir(source)
folder_id = '101217738692'

for i in files_in_src:
    try:
        new_file = client.folder(folder_id).upload(source+i)
        print('File "{0}" uploaded to Box with file ID {1}'.format(new_file.name, new_file.id))
    except BoxAPIException as e:
        #print('File #s exists. Updaing contents.' %source+i)
        file_id = e.context_info['conflicts']['id']
        updated_file = client.file(file_id).update_contents(source+i)
        print('File "{0}" has been updated'.format(updated_file.name))
