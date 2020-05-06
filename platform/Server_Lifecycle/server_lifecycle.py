import psutil
import os
import time
import sys
import json
import threading
from time import sleep
from datetime import datetime
import random as r

import sys
sys.path.insert(0, "platform/communication_module")

print('\n[Server life cycle] : started \n')
import communication_module as cm
import producer_json

server_details={}

flag=0

def handle_service(msg):
	#print("#######",msg['service_id'],"for Logging")
	service_id=msg['service_id']
	code=msg['code']
	logmsg={}
	logmsg['component']='Server_lifecycle'
	logmsg['msg']=msg
	# cm.common_Logger_Producer_interface(logmsg)
	producer_json.send_message(service_id,msg)


def handle_runtime():
	while(1):
		cm.DeployManager_to_RuntimeServer_interface(handle_service)


def get_all_server_details():
	global server_details
	curpath=str(os.path.dirname(os.path.realpath(__file__)))
	f = open(curpath+'/server_details.json',) 
	data = json.load(f) 
	#print(data)
	server_details=data


def start_server():
	global server_details
	_server=None
	for i in server_details:
		if server_details[i]['active']==0:
			_server=i
			break

	if(_server==None):
		print("All servers are active")
		return

	server_details[i]['active']=1
	cwd=str(os.path.dirname(os.path.realpath(__file__)))
	# cwd = os.getcwd()
	logmsg={}
	logmsg['component']='Server_lifecycle'
	logmsg['msg']=str(_server)+" has been started"
	# cm.common_Logger_Producer_interface(logmsg)
	# print("Logmsg!!!!!!",logmsg)
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
	#print("Load Balancing")
	for k,v in stats.items():
		#print(k,v)
		if(server_details[k]['active']==1):
			ll=v.split('|')
			load=compute_load(float(ll[0]),float(ll[1]))
			loads.append([load,k])

	loads.sort()
	#print(loads)
	return loads[0][1]


def handle_service_LC_msg(msg):
	#print("receive service life cycle msg \n",msg)
	send_server_details_msg(msg)

def send_server_details_msg(msg):
	global flag
	t=r.randint(1,2)
	#s=load_balancer()
	sv="s"+str(t)
	msg['server_id']=sv
	msg['ip']="127.0.0.1"
	msg['port']="8090"

	if(msg['priority']=="high"):
		if(flag==0):
			msg['server_id']='s3'
			flag=1
		else:
			msg['server_id']=None
	print("\n[Server life cycle]: Recevied msg and sent (Server id) - ",msg['server_id'], '\n')
	logmsg={}
	logmsg['component']='Server_lifecycle'
	logmsg['msg']=msg
	# cm.common_Logger_Producer_interface(logmsg)
	cm.ServerLifeCycle_to_ServiceLifeCycle_Producer_interface(msg)
	#print("\nmsg sended")


def handle_service_LC():
	while(1):
		cm.ServiceLifeCycle_to_ServerLifeCycle_interface(handle_service_LC_msg)

def handle_restart_service(msg):
	print('\n[Server life cycle] : ',end=" ")
	print("restart server!!!!!!!!!!!!")
	# t=r.randint(1,2)
	#s=load_balancer()
	if msg["server_id"]=="s1":
		sv="s2"
	else:
		sv="s1"

	# sv="s"+str(t)
	msg['server_id']=sv
	msg['ip']="127.0.0.1"
	msg['port']="8090"

	#print("Service to schedule-------->\n",sv)
	logmsg={}
	logmsg['component']='Server_lifecycle'
	logmsg['msg']=msg
	# cm.common_Logger_Producer_interface(logmsg)
	cm.ServerLifeCycle_to_ServiceLifeCycle_Producer_interface(msg)
	#print("\nmsg sended")



# def restart_service():
# 	cm.ApplicationManager_to_ServiceLifeCycle_interface2(handle_restart_service)
# 	print("end while!!!!")

get_all_server_details()
#start_server()
#start_server()



# start_server()
t1 = threading.Thread(target=handle_runtime, args=()) 
t1.start() 
t2 = threading.Thread(target=handle_service_LC , args=()) 
t2.start()

# t3 = threading.Thread(target=restart_service, args=()) 
# t3.start() 

th=threading.Thread(target=cm.ApplicationManager_to_ServiceLifeCycle_interface2,kwargs={'func_name':handle_restart_service})
th.start()


t1.join()
t2.join()
# t3.join()

# print("Bye!") 


