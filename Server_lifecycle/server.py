from time import sleep
from json import dumps
import subprocess

import sys
sys.path.insert(0, "../communication_module")

import communication_module as cm

from sys import argv
import psutil
import threading 
from time import sleep
from datetime import datetime
from random import randint

services=[]
service_status={}

import os
def handle_service(msg):
	os.system("python3 "+msg)


def send_server_stats(producer,server_id):
	print("Server id : ",server_id," Started")
	#msg=str(utilization['cpu'])+"|"+str(utilization['ram'])+"|"+utilization['time']
	while(True):
		cpu=randint(1,100)
		ram=randint(1,100)
		utilization=get_system_utilization()
		msg_service=""
		for service in services:
			msg_service=msg_service+service[1]+";"
		msg=str(cpu)+"|"+str(ram)+"|"+utilization['time']+"|"+msg_service
		producer.send('Servers',key=bytes(str(server_id), 'utf8'),value=bytes(str(msg), 'utf8'))
		print("Sent to Server lifecycle manager : ",msg)
		sleep(30)



def get_system_utilization():
    utilization = {}
    utilization['cpu'] = psutil.cpu_percent()
    stats = dict(psutil.virtual_memory()._asdict())
    utilization['ram'] = stats['used'] * 100.0 / stats['total']
    now = datetime.now()
    utilization['time']=str(now)
    return utilization



# Monitoring module code
# t1 = threading.Thread(target=send_server_stats, args=(argv[1])) 
# t1.start()  


from kafka import KafkaConsumer
print('Hii this is ',argv[1])
topic=argv[1]
	
consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message in consumer:
	mess= (message.value)
	print(mess)
	th = threading.Thread(target=handle_service,kwargs={'msg':mess})
	th.start()




	

