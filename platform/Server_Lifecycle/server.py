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

import os

def handle_service(msg):
	os.system("python3 "+msg)


def send_server_stats(server_id):
	print("Server id : ",server_id," Started")
	while(True):
		cpu=randint(1,100)
		ram=randint(1,100)
		utilization=get_system_utilization()
		utilization['server_id']=server_id
		cm.Runtime_Servers_to_Monitoring_Module_Producer_interface(utilization)
		print("Sent status to Monitoring manager : ",utilization)
		sleep(30)



def get_system_utilization():
    utilization = {}
    utilization['cpu'] = psutil.cpu_percent()
    stats = dict(psutil.virtual_memory()._asdict())
    utilization['ram'] = stats['used'] * 100.0 / stats['total']
    #now = datetime.now()
    #d=now.total_seconds()
    d = time.time()
    utilization['time']=d
    return utilization



#Monitoring module code
print(os.getcwd())
from kafka import KafkaConsumer
print('Hii this is ',argv[1])

topic=str(argv[1])

t1 = threading.Thread(target=send_server_stats, args=(argv[1],)) 
t1.start()  

consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message in consumer:
	mess= (message.value)
	print("Running this process : ",mess)
	th = threading.Thread(target=handle_service,kwargs={'msg':mess})
	th.start()

t1.join() 




	

