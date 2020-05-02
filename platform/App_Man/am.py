import socket 
from _thread import *
import threading  
import re
import json
import jsonschema
from jsonschema import validate
from kafka import KafkaProducer
from zipfile import ZipFile
import os
import sys
import shutil
import time
sys.path.insert(0, "platform/communication_module")
import communication_module as cm


configschema = {
"type": "object",
"properties": {
"userid": {"type": "string"},
"reqid": {"type": "string"},
"appid": {"type": "string"},
"algoid": {"type": "string"},
"action":{"type": "string"},
"location":{"type": "string"},
"sensortype":{"type": "string"},
"old/runningservice":{"type":"string"},
},
}

filename="name_password.txt"


def dev_se_data(fd):
	filenam="./dynamic.txt"
	with open(filenam) as f1:
		dy1=f1.readlines()
		dy1 = [x.rstrip() for x in dy1] 
		# print(dy1)
		dy=dy1[0]
		tr=dy
		tr=eval(tr)
		print(tr)
		cm.ApplicationManager_to_Scheduler_Producer_interface(tr)
		# os.remove("./dynamic.txt")

def handler(func, path, exc_info): 
	print("Inside handler") 
	print(exc_info) 

def main():
	old_stamp=0
	while(1):
		if os.path.isfile("./dynamic.txt")==True:
			time.sleep(2) 
			stamp = os.stat("./dynamic.txt").st_mtime
			if(stamp != old_stamp):
				old_stamp = stamp
				start_new_thread(dev_se_data,(filename,))

		if os.path.isdir("./uploads")==True:
			time.sleep(2) 
			x=os.listdir("./uploads")
			y=str(x)
			# print(str(y[2:-2]))
			x1="./uploads/"+str(y[2:-2])
			# print("1")
			# print("x1",x1)
			file1 = open('file_up.txt', 'r') 
			lines = file1.readlines() 
			l=lines[0]
			l=eval(l)
			file1.close()
			lc="../../Applications/"+l['user_id']+"/"
			with ZipFile(x1, 'r') as zipObj:
				zipObj.extractall(lc)
			path = os.path.join("./", "uploads") 
			shutil.rmtree(path, onerror = handler)
			print("Extracted")


if __name__ == '__main__': 
	main()
