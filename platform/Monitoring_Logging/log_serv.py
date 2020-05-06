import sys
sys.path.insert(0, "platform/communication_module")

import communication_module
# import communication_module
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

# producerSch = KafkaProducer(bootstrap_servers=['localhost:9092'],
#                          value_serializer=lambda x: 
#                          dumps(x).encode('utf-8'))


commonLog = KafkaConsumer(
    'commonLog',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group'	,
     value_deserializer=lambda x: loads(x.decode('utf-8')))



def eventReceiveLogData(m1):
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!receieved log data:::",m1)
    message = m1
    res=m1
   
    # if (isinstance(message, dict) ):
    # 	res=message
    # else:
    # 	res = ast.literal_eval(message) 
   
    # print("Message receieved in log:",(res),type(res))
    # print("table to store:",res['component'])
    

    # if res["component"]=="server":
    mydb = myclient["server_db"]

    for i in m1:
        cur_collection="log_"+i['server_id']
        #print("cur_collection",cur_collection)
        #print("res insert in db@@@@@@@@@@", i,cur_collection)
        mycol = mydb[cur_collection]
        mycol.insert_one(i)

    # mycol = mydb[res['component']]
	# mydict = { "name": "John", "address": "Highway 37" }
    # x = mycol.insert_one(res)
    # print("stored in table\n\n")


fun=eventReceiveLogData



def threaded():
	# print ("In thread!!!!!!!!!!!!")
	while True:
		# sleep(2)
		# print("hi")
		communication_module.common_Logger_interface(fun)
		'''for message in commonLog:
		    message = message.value
		    res = ast.literal_eval(message) 
		    print("Message receieved:",(res),type(res))
		    print("table to store:",res['component'])
		    # mycol = mydb["logtable"]
		    mycol = mydb[res['component']]
			# mydict = { "name": "John", "address": "Highway 37" }
		    x = mycol.insert_one(res)'''


# def handle_restart_service(msg):
#     print("restart server!!!!!!!!!!!!")
#     print(msg)
    # t=r.randint(1,2)
    #s=load_balancer()
    # if msg["server_id"]=="s1":
    #     sv="s2"
    # else:
    #     sv="s1"

    # # sv="s"+str(t)
    # msg['server_id']=sv
    # msg['ip']="127.0.0.1"
    # msg['port']="8090"

    # print("Service to schedule-------->\n",sv)
    # logmsg={}
    # logmsg['component']='Server_lifecycle'
    # logmsg['msg']=msg
    # # cm.common_Logger_Producer_interface(logmsg)
    # cm.ServerLifeCycle_to_ServiceLifeCycle_Producer_interface(msg)
    # print("\nmsg sended")


# def restart_service():
#     while(1):
#         communication_module.ApplicationManager_to_ServiceLifeCycle_interface2(handle_restart_service)
#         print("end while!!!!")


start_new_thread(threaded,()) 

# t3 = threading.Thread(target=restart_service, args=()) 
# t3.start() 






# createTopics()
print("\n[Logging-Module] - started\n")

while(1):
	pass
