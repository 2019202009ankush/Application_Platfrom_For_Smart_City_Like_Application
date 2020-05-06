from os.path import dirname, realpath
from time import sleep
import json
import subprocess

import sys
sys.path.insert(0, "platform/communication_module")

import communication_module as cm

from sys import argv
import psutil
import threading 
from time import sleep
from datetime import datetime
from random import randint
import time

services=[]
service_status={}

cur_running_services=[]



import os

def handle_service(msg):
	global cur_running_services,topic
	#print("msg",msg)

	curpath=str(os.path.dirname(os.path.realpath(__file__)))
	# print("curpath",curpath)
	ppath=dirname(curpath)
	# print("ppath",ppath)
	ppp_path=dirname(ppath)
	msg_to_send={}

	msg['code']='"'+ppp_path+msg['code'][1:]

	print("Service ",msg['algoid'],"running")
	
	# msg_to_send["component"]="server"
	# msg_to_send["server_id"]=topic
	# msg_to_send["cur_running_services"]=cur_running_services

	msg["component"]="server"
	msg["server_id"]=topic
	# msg["cur_running_services"]=cur_running_services

	d = time.time()
	msg['timestamp']=d

	cur_running_services.append(msg)

	#print("msg to send@@@@@@!!!",cur_running_services)

	# cm.common_Logger_Producer_interface("this is demo msg!!!!!!!!!!!!!!!!!!!!!!!!!")

	cm.common_Logger_Producer_interface(cur_running_services)

	os.system("python3 "+msg['code'])
	#to logging

	#print("this service finished!!!!!!!!!!!!!!!",msg)

	cur_running_services.remove(msg)

	d = time.time()
	
	# cur_running_services['timestamp']=d


	# msg["cur_running_services"]=cur_running_services

	cm.common_Logger_Producer_interface(cur_running_services)

	#to logging





def send_server_stats(server_id):
	global cur_running_services

	#print("Server id : ",server_id," Started")
	while(True):
		cpu=randint(1,100)
		ram=randint(1,100)
		utilization=get_system_utilization()
		utilization['server_id']=server_id
		utilization['component']="server"
		cm.Runtime_Servers_to_Monitoring_Module_Producer_interface(utilization)
		#print("Sent status to Monitoring manager : ",utilization)
		sleep(10)



def get_system_utilization():
    utilization = {}
    utilization['cpu'] = psutil.cpu_percent()
    stats = dict(psutil.virtual_memory()._asdict())
    utilization['ram'] = stats['used'] * 100.0 / stats['total']
    #now = datetime.now()
    #d=now.total_seconds()
    d = time.time()
    utilization['timestamp']=d
    return utilization



#Monitoring module code
#print(os.getcwd())
from kafka import KafkaConsumer
print('[Server ',argv[1]," ] started")

topic=str(argv[1])

t1 = threading.Thread(target=send_server_stats, args=(argv[1],)) 
t1.start()  

consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message in consumer:
	mess= (message.value)
	#print("Running this process : ",mess)
	th = threading.Thread(target=handle_service,kwargs={'msg':mess})
	th.start()

t1.join() 




	

