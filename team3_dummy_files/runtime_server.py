#!/usr/bin/env python3
import sys
sys.path.insert(0, "../communication_module")

import communication_module

import time
import ast 

from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import threading
import json

'''

def consumer_t(top):
    print("consumer of runtime server called by thread and running now....")
    global chance
    consumer = KafkaConsumer(top,
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     value_deserializer=lambda x: loads(x.decode('utf-8')))
    
    for message in consumer:
        message = message.value
        action_handler(message)


        '''
#        print((message))

# topic="run"
# t1 = threading.Thread(target=consumer_t,args=(topic,))
# t1.start() 
# producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))

x = {
  "UserID": "upadhyayyash1712@gmail.com",
  "AppName": "Tempreture",
  "ServiceName": "findtemp","component":"server","serverID":"ser_01",
  "Action": [{"type1":"email", "type2":"notification"}],
  "Output": "29 degree"
}
reply_to_monitor_by_server={"component":"server","serverID":"ser_01","ram_usage_in_mb":"500","up_time_in_sec":"600","runtime":"runtime","timestamp":"132434989","ip_address":"localhost"}

y = json.dumps(x)
communication_module.RuntimeServer_to_ActionServer_Producer_interface(y)
# producer.send("RuntimeServer_to_ActionServer_Producer_interface", value=y)
