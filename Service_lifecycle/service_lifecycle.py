from time import sleep
from json import dumps
import json

from algorith_binder import *

import sys
sys.path.insert(0, "../communication_module")

import communication_module as cm


def get_scheduler_msg():

	f = open('scheduler_msg.json',) 
	data = json.load(f)
	print("Service to schedule",data)
	send_request_serverLC(data)
	service_data=bind_algo(data)

	server=recieved_server_details()
	print("\nRecieved Server details:- ",server)
	service_data['server']=server[service_data['reqid']]

	print("\nSending Service details to Deployment Manager\n",service_data)

	send_service_to_deployment(service_data)

	return data

def handle_scheduler_msg(msg):

	send_request_serverLC(msg)

	service_data=bind_algo(msg)

	server=recieved_server_details()
	print("\nRecieved Server details:- ",server)

	service_data['server']=server[service_data['reqid']]

	print("\nSending Service details to Deployment Manager\n",service_data)

	send_service_to_deployment(service_data)

def send_service_to_deployment(msg):
	cm.ServiceLifeCycle_to_DeployManager_Producer_interface(msg)


def send_request_serverLC(data):
	msg=str("Request")
	print("\nSending to ServerLC :-",data['reqid'],msg)
	cm.ServiceLifeCycle_to_ServerLifeCycle_Producer_interface(msg)


def recieved_server_details():
	msg={1:
	{
		"server_id":"s1",
		"ip":'127.0.0.1',
		"port":8090
	}}
	return msg

cm.Schedular_to_ServiceLifeCycle_interface(handle_scheduler_msg)