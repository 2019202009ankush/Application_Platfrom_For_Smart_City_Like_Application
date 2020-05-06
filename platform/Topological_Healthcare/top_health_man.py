import ast
import sys
sys.path.insert(0, "platform/communication_module")

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

curpath=str(os.path.dirname(os.path.realpath(__file__)))
path=curpath+"/dropall.js"
#os.system("python3 "+path)


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

def threaded_server(serverid):
	print ("In thread check server:",serverid)
	flg=1
	log_db = myclient["server_db"]
	while True:
		# pass
		sleep(2)
		# print("find latest timestamp")
		mynew = log_db[serverid] 
		lts= mynew.find().sort("timestamp", -1)
		lts=lts[0]["timestamp"]
		cts=time.time()
		# print("cts",cts)
		# print("lts",lts)
		print("diff :",(float(cts)-float(lts)))


		if(float(cts) - float(lts))>30:
			print("server failed :",serverid)
			if flg==1:
				rescedule_services=""

				cur_collection=log_db["log_"+serverid]

				# msg_to_slc= cur_collection.find_one().sort("timestamp", -1)
				msg_to_slc= cur_collection.find().sort("timestamp", -1)

				if msg_to_slc:

					ts=msg_to_slc[0]

					msg_to_slc=msg_to_slc[0]
					print("ts to send to SLC:",msg_to_slc,type(msg_to_slc))

					# msg_to_slc=msg_to_slc['cur_running_services']
					print("msg to send to SLC:",msg_to_slc)
					
					# communication_module.TopoManager_to_ServiceLifeCycle_Producer_interface(msg_to_slc)
					# dict1={"a":"a1","b":"b1"}
					dict1={}
					
					dict1['UserId']=msg_to_slc['UserId']
					dict1['AppName']=msg_to_slc['AppName']
					dict1['priority']=msg_to_slc['priority']
					dict1['duration']=msg_to_slc['duration']
					dict1['algoid']=msg_to_slc['algoid']

					dict1['start_time']=msg_to_slc['start_time']
					dict1['request_type']=msg_to_slc['request_type']
					dict1['location']=msg_to_slc['location']

					dict1['server_id']=msg_to_slc['server_id']
					dict1['UserId']=msg_to_slc['UserId']
					dict1['UserId']=msg_to_slc['UserId']



					# communication_module.ApplicationManager_to_ServiceLifeCycle_Producer_interface2(msg_to_slc)
					communication_module.ApplicationManager_to_ServiceLifeCycle_Producer_interface2(dict1)

					print("message sended!!!!!!!!!!!!",dict1)

					flg=0
			####send msg to service lifecycle
		else:
			flg=1
			print("server correct",serverid)






# createTopics()

# start_new_thread(threaded_sc,()) 
# start_new_thread(threaded_dep,()) 

start_new_thread(threaded_server,("s1",)) 
start_new_thread(threaded_server,("s2",)) 
#start_new_thread(threaded_server,("s3",)) 


# start_new_thread(communication_module.TopoManager_to_ServerLifeCycle_interface("None"),())

# start_new_thread(communication_module.TopoManager_to_ServiceLifeCycle_interface("None"),())

print('\n[Topological-Manager] : started \n')

while(1):
	pass



'''Topics req
	commonLog
deploymentMonitoring
monitoringDeployment

schedulerMonitoring
monitoringScheduler

'''
