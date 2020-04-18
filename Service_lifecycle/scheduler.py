from time import sleep
from json import dumps
import json

import sys
sys.path.insert(0, "../communication_module")

import communication_module as cm

def send_scheduler_msg():

	f = open('scheduler_msg.json',) 
	data = json.load(f)
	print("Service to schedule\n",data)
	cm.Schedular_to_ServiceLifeCycle_Producer_interface(data)
	print("\nmsg sended")

send_scheduler_msg()