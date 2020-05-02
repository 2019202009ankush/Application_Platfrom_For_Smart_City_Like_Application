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
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!receieved log data:::",m1)
    message = m1
    if (isinstance(message, dict) ):
    	res=message
    else:
    	res = ast.literal_eval(message) 
    # print("Message receieved:",(res),type(res))
    # print("table to store:",res['component'])
    # mycol = mydb["logtable"]
    mycol = mydb[res['component']]
	# mydict = { "name": "John", "address": "Highway 37" }
    x = mycol.insert_one(res)
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




start_new_thread(threaded,()) 

def createTopics():
	os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic commonLog")


# createTopics()

print("---------- Logging --------------")
while(1):
	pass
