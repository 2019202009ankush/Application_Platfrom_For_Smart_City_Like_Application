import sys
sys.path.insert(0, "../communication_module")

import communication_module

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




def threaded_sc():
	print ("In thread check scheduler")
	while True:
		sleep(2)
		print("find latest timestamp")
		mynew = mydb["sch_mon"] 
		lts= mynew.find().sort("timestamp", -1)
		lts=lts[0]["timestamp"]
		cts=time.time()
		print("cts",cts)
		print("lts",lts)
		print("diff",(float(cts)-float(lts)))
		if(float(cts) - float(lts))>25:
			print("scheduler failed\n")
			communication_module.TopoManager_to_ServerLifeCycle_Producer_interface("scheduler_failed")

			break
			#perform action
			####send msg to service lifecycle
			###log service
			## mon server

		else:
			print("scheduler correct\n")

def threaded_dep():
	print ("In thread check deployer")
	while True:
		sleep(2)
		print("find latest timestamp")
		mynew = mydb["dep_mon"] 
		lts= mynew.find().sort("timestamp", -1)
		lts=lts[0]["timestamp"]
		cts=time.time()
		print("cts",cts)
		print("lts",lts)
		print("diff",(float(cts)-float(lts)))
		if(float(cts) - float(lts))>25:
			print("deployer failed\n")
			communication_module.TopoManager_to_ServiceLifeCycle_Producer_interface("deployer_failed")
			####send msg to service lifecycle
		else:
			print("deployer correct\n")





def createTopics():
	os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic deploymentMonitoring")
	os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic monitoringDeployment")
	os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic schedulerMonitoring")
	os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic monitoringScheduler")


# createTopics()

start_new_thread(threaded_sc,()) 
start_new_thread(threaded_dep,()) 

start_new_thread(communication_module.TopoManager_to_ServerLifeCycle_interface("None"),())

start_new_thread(communication_module.TopoManager_to_ServiceLifeCycle_interface("None"),())


while(1):
	pass



'''Topics req
	commonLog
deploymentMonitoring
monitoringDeployment

schedulerMonitoring
monitoringScheduler

'''