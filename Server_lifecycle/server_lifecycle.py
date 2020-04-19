import psutil
import os
import time
import sys
import json
import threading
from time import sleep
from datetime import datetime


import sys
sys.path.insert(0, "../communication_module")

import communication_module as cm

server_details={}

def run_service(producer,server_id,service_name):
	msg=service_name
	producer.send('ServiceToServer',key=bytes(str(server_id), 'utf8'),value=bytes(str(msg), 'utf8'))
	print("Sent to Server lifecycle manager : ",server_id,msg)



def get_all_server_details():
	global server_details
	f = open('server_details.json',) 
	data = json.load(f) 
	print(data)
	server_details=data


def start_server():
	_server=None
	for i in server_details:
		if server_details[i]['active']==0:
			_server=i
			break

	if(_server==None):
		print("All servers are active")
		return

	cwd = os.getcwd()
	print(server_details[_server],_server,server_details[_server]['ip'],server_details[_server]['port'])
	cmd="gnome-terminal -- python3 -i "+cwd+"/server.py "+str(_server)+" "+str(server_details[_server]['ip'])+" "+str(server_details[_server]['port'])
	os.system(cmd)
	# print(cmd)
	print("Server started with server id : ",_server)


def start_server_with_stats():
	pass

def release_server():
	pass

def get_server_stats(server_id):
	return stats[server_id]

def thershold_check():
	pass


def compute_load(cpu,mm):
	return 2*cpu*mm/(cpu+mm)

def load_balancer():
	loads=[]
	print("Load Balancing")
	for k,v in stats.items():
		print(k,v)
		if(server_details[k]['active']==1):
			ll=v.split('|')
			load=compute_load(float(ll[0]),float(ll[1]))
			loads.append([load,k])

	loads.sort()
	print(loads)
	return loads[0][1]


def handle_service_LC_msg(msg):
	print("receive service life cycle msg-------->\n",msg)
	send_server_details_msg(msg)

def send_server_details_msg(msg):
	msg['server_id']="s1"
	msg['ip']="127.0.0.1"
	msg['port']="9092"
	print("Service to schedule-------->\n",msg)
	cm.ServerLifeCycle_to_ServiceLifeCycle_Producer_interface(msg)
	print("\nmsg sended")


get_all_server_details()
start_server()
cm.ServiceLifeCycle_to_ServerLifeCycle_interface(handle_service_LC_msg)
print("Bye!") 

