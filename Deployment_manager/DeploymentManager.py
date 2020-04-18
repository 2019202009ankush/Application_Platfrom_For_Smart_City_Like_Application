from time import sleep
from json import dumps
import json

import sys
sys.path.insert(0, "../communication_module")

import communication_module as cm



sensor_id_returned={	1:{"topic":"Temperatue",
						"id":"s104"},

						2:{"topic":"Humidity",
						"id":"t808"},
					}



def handle_servicelc_msg(msg):

	print("Service Recieved to deploy:-\n",msg)

	request_sensor(msg)

	sensors=msg_recieved_sensor_mgr()

	msg['algoid']['sensor']=sensors

	send_to_server(msg)	


def send_to_server(data):
	key=data['reqid']
	msg=data
	print("\nSending to Run Time server :-\n",key,msg)


def request_sensor(data):
	msg={}
	msg['location']=data['location']
	msg['sensor']=data['algoid']['sensor']

	key=data['reqid']

	print("\nSending to Sensor mgr :-\n",key,msg)


def msg_recieved_sensor_mgr():
	return sensor_id_returned



cm.ServiceLifeCycle_to_DeployManager_interface(handle_servicelc_msg)
