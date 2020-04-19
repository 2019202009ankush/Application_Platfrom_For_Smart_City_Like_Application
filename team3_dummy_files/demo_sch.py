import sys
sys.path.insert(0, "../communication_module")

import communication_module
# import communication_module
from _thread import *
import threading 

import time
import ast 

from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer

from kafka import KafkaConsumer
from json import loads
from json import dumps
from kafka import KafkaProducer

producerMon = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

consumerMon = KafkaConsumer(
    'monitoringScheduler',
     bootstrap_servers=['localhost:9092'],
     # auto_offset_reset='latest',
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group'	,
     value_deserializer=lambda x: loads(x.decode('utf-8')))




stats='{"component":"scheduler","ramusageinmb":"500","uptimeinsec":"600","servname":"s_name","runtime":"runtime","timestamp":"132434989"}'

logstats='{"Component":"deployer_log","App_Name":"App_1","User_name":"Yash","Service_Name":"Send_Tempreture","server_assigned":"serverID","serverIP":"localhost","timestamp":"132434989","ip":"localhost"}'

def eventSchToMon(m1):
	print("Ping Message receieved:",(m1))
	print("again\n")
	# return


fun1=eventSchToMon

def threadedMon(): 
	print ("In thread Mon")
	while True:
		# print("111nnn")

		communication_module.Monitoring_Module_to_Scheduler_interface(fun1)
		# for message in consumerMon:
		# 	message = message.value
		# 	print("Ping Message receieved:",(message))
		# 	break
		# sleep(4)
		print("sending ping reply")
		msg=stats

		res = ast.literal_eval(msg)
		res["timestamp"] =str(int(time.time()))
		res=str(res)
		print(res)
		time.sleep(2)

		communication_module.Scheduler_to_Monitoring_Module_Producer_interface(res)
		# producerMon.send('schedulerMonitoring', value=res)
		print("msg sent from scheduler")

		# producerMon.send('schedulerMonitoring', value=msg)
		# print("msg sent")


def threadedLog(): 
	print ("In thread log")
	while True:
		sleep(4)
		print("sending log")
		msg=logstats
		# producerMon.send('commonLog', value=msg)
		communication_module.Scheduler_to_Logger_Producer_interface(msg)

		print("msg sent in common log")


start_new_thread(threadedMon,()) 
# start_new_thread(threadedLog,()) 
while(1):
	pass 
