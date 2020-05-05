import socket 
from _thread import *
import threading  
import re
import json
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

curpath=str(os.path.dirname(os.path.realpath(__file__)))
filename=curpath+"/name_password.txt"

os.system("python3 "+curpath+"/file_upload.py &")
os.system("python3 "+curpath+"/dynamic_data.py &")

def dev_se_data(fd):
	curpath=str(os.path.dirname(os.path.realpath(__file__)))
	filenam=curpath+"/dynamic.txt"
	with open(filenam) as f1:
		dy1=f1.readlines()
		dy1 = [x.rstrip() for x in dy1] 
		# print(dy1)
		dy=dy1[0]
		tr=dy
		tr=eval(tr)
		#print(tr)
		cm.ApplicationManager_to_Scheduler_Producer_interface(tr)
		# os.remove("./dynamic.txt")

def handler(func, path, exc_info): 
	#print("Inside handler") 
	print(exc_info) 

def main():
	old_stamp=0
	while(1):
		curpath=str(os.path.dirname(os.path.realpath(__file__)))
		filenam=curpath+"/dynamic.txt"
		if os.path.isfile(filenam)==True:
			time.sleep(2) 
			stamp = os.stat(filenam).st_mtime
			if(stamp != old_stamp):
				old_stamp = stamp
				start_new_thread(dev_se_data,(filename,))

		if os.path.isdir(curpath+"/uploads")==True:
			time.sleep(2) 
			x=os.listdir(curpath+"/uploads")
			y=str(x)
			# print(str(y[2:-2]))
			x1=curpath+"/uploads/"+str(y[2:-2])
			# print("1")
			# print("x1",x1)
			file1 = open(curpath+'/file_up.txt', 'r') 
			lines = file1.readlines() 
			l=lines[0]
			l=eval(l)
			file1.close()
			lc="/opt/Applications/"+l['user_id']+"/"
			with ZipFile(x1, 'r') as zipObj:
				zipObj.extractall(lc)
			path = os.path.join(curpath, "uploads") 
			shutil.rmtree(path, onerror = handler)
			print("Done")


if __name__ == '__main__': 
	main()
