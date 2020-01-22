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
items = client.search().query(query='curl', limit=100)
for item in items:
	print('The item ID is {0} and the item name is {1}'.format(item.id, item.name))

