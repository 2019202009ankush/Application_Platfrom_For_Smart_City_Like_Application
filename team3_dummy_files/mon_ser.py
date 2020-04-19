import sys
sys.path.insert(0, "../communication_module")


import communication_module
##server
import time
import os
import ast 
import pymongo
from _thread import *
import threading 

from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer

from kafka import KafkaConsumer
from json import loads
from json import dumps
from kafka import KafkaProducer


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["hackdb"]

producerSch = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

consumerSch = KafkaConsumer(
    'schedulerMonitoring',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     # auto_offset_reset='earliest',
     # enable_auto_commit=True,
     # group_id='my-group'	,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

producerDep = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

consumerDep = KafkaConsumer(
    'deploymentMonitoring',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     # auto_offset_reset='earliest',
     # enable_auto_commit=True,
     # group_id='my-group'	,
     value_deserializer=lambda x: loads(x.decode('utf-8')))



def eventReceiveSchToMon(m1):
    print("receieved:::",m1)
    message = m1
    res = ast.literal_eval(message) 
    print("Message receieved:",(res),type(res))
    mycol = mydb["sch_mon"]
	# mydict = { "name": "John", "address": "Highway 37" }

    x = mycol.insert_one(res)


fun1=eventReceiveSchToMon

def threaded_sc():
	print ("In thread scheduler")
	while True:
		sleep(1)
		print("send ping to sch")
		msg="ping to scheduler"
		# producerSch.send('monitoringScheduler', value=msg)
		communication_module.Monitoring_Module_to_Scheduler_Producer_interface(msg)
		print("sent msg")
		# time.sleep(2)

		communication_module.Scheduler_to_Monitoring_Module_interface(fun1)
		print("msg received mm")
		# for message in consumerSch:
		#     message = message.value
		#     res = ast.literal_eval(message) 
		#     print("Message receieved:",(res),type(res))
		#     mycol = mydb["sch_mon"]
		# 	# mydict = { "name": "John", "address": "Highway 37" }

		#     x = mycol.insert_one(res)
		#     break

def eventReceiveDepToMon(m1):
    print("receieved:::",m1)
    message = m1
    res = ast.literal_eval(message) 
    print("Message receieved:",(res),type(res))
    mycol = mydb["dep_mon"]
	# mydict = { "name": "John", "address": "Highway 37" }

    x = mycol.insert_one(res)
    
    

fun2=eventReceiveDepToMon

def threaded_dep():
	print ("In thread deployer")
	while True:
		sleep(1)
		print("send ping to deployer")
		msg="ping to deployer"
		# producerDep.send('monitoringDeployment', value=msg)
		communication_module.Monitoring_Module_to_Deployer_Producer_interface(msg)
		communication_module.Deployer_to_Monitoring_Module_interface(fun2)
		# for message in consumerDep:
		#     message = message.value
		#     res = ast.literal_eval(message) 
		#     print("Message receieved:",(res),type(res))
		#     mycol = mydb["dep_mon"]
		# 	# mydict = { "name": "John", "address": "Highway 37" }

		#     x = mycol.insert_one(res)
		#     break





def createTopics():
	os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic deploymentMonitoring")
	os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic monitoringDeployment")
	os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic schedulerMonitoring")
	os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic monitoringScheduler")


# createTopics()

start_new_thread(threaded_sc,()) 
start_new_thread(threaded_dep,()) 



while(1):
	pass



'''Topics req
commonLog
deploymentMonitoring
monitoringDeployment

schedulerMonitoring
monitoringScheduler

'''