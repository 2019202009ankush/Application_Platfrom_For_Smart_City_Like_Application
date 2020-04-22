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
import producer_json

server_details={}

def handle_service(msg):
	service_id=msg['service_id']
	code=msg['code']
	logmsg={}
	logmsg['component']='Server_lifecycle'
	logmsg['msg']=msg
	cm.common_Logger_Producer_interface(logmsg)
	producer_json.send_message(service_id,code)


def handle_runtime():
	while(1):
		cm.DeployManager_to_RuntimeServer_interface(handle_service)


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

	server_details[i]['active']==1
	cwd = os.getcwd()
	logmsg={}
	logmsg['component']='Server_lifecycle'
	logmsg['msg']=str(_server)+" has been started"
	cm.common_Logger_Producer_interface(logmsg)
	print("Logmsg!!!!!!",logmsg)
	print(server_details[_server],_server,server_details[_server]['ip'],server_details[_server]['port'])
	cmd="gnome-terminal -- python3 -i "+"'"+cwd+"/server.py' "+str(_server)+" "+str(server_details[_server]['ip'])+" "+str(server_details[_server]['port'])
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
	logmsg={}
	logmsg['component']='Server_lifecycle'
	logmsg['msg']=msg
	cm.common_Logger_Producer_interface(logmsg)
	cm.ServerLifeCycle_to_ServiceLifeCycle_Producer_interface(msg)
	print("\nmsg sended")


def handle_service():
	while(1):
		cm.ServiceLifeCycle_to_ServerLifeCycle_interface(handle_service_LC_msg)


get_all_server_details()
start_server()
start_server()
t1 = threading.Thread(target=handle_runtime, args=()) 
t1.start() 
t2 = threading.Thread(target=handle_service , args=()) 
t2.start()  
t1.join()
t2.join()
print("Bye!") 


