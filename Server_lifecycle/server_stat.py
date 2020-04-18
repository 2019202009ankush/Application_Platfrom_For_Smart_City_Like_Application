from time import sleep
from json import dumps
from kafka import KafkaProducer
import subprocess

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


from kafka import KafkaConsumer

def consume_message(topic,server_id):
	consumer = KafkaConsumer(topic)
	for mess in consumer:
		key=str(mess.key.decode())
		value=str(mess.value.decode())
		if(key==server_id):
			break
	return value


from sys import argv
import psutil
import threading 
from time import sleep
from datetime import datetime
from random import randint

#list_of_services=['service1.py','service2.py','service3.py']
services=[]
service_status={}

import os
def start_service(service_name):
	os.system("python3 "+service_name)


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
    # print("Time : ",utilization['time'])
    # print("CPU : ",utilization['cpu'])
    # print("RAM : ",utilization['ram'])
    return utilization

if __name__ == '__main__':
	print(argv)
	t1 = threading.Thread(target=send_server_stats, args=(producer,argv[1])) 
	t1.start()  

	# for service in services:
	# 	start_service(service)

	while(True):
		print("------>\n")
		#inp=input()
		msg=consume_message('ServiceToServer',argv[1])
		print(msg)
		ss=threading.Thread(target=start_service, args=(msg,)) 
		ss.start()
		services.append([ss,msg])

	t1.join() 
	print("Bye!") 
	

