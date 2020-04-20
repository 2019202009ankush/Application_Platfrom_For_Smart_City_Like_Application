#!/usr/bin/env python3
import sys
sys.path.insert(0, "../communication_module")

import communication_module
# import communication_module
import time
import ast 
from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import threading
from _thread import *
import threading 

import json,os
#import communicationmodule.py
user_no=0
#def email_method():
#    import smtplib 
#    s = smtplib.SMTP('smtp.gmail.com', 587) 
#    s.starttls() 
#    s.login("upadhyayyash1712@gmail.com", "9074263059") 
#    message = "HI Yash" 
#    s.sendmail("upadhyayyash1712@gmail.com", "upadhyayyash1712@gmail.com", message)
#    s.quit() 

def action_handler(message):
    print("in action_handler::::",message)
    global user_no
    dict_msg = message
    print(user_no)
    if(dict_msg['Action_type']=='Control'):
        print("Hardware Action to be taken !!!!!!!!",dict_msg['Action'])
    else:
        action_list = dict_msg['Action']
        print("Number of dict accociated "+str(len(action_list)))
        action_tag=[]
        temp_list=action_list[0]
        for key in temp_list:
            action_tag.append(temp_list[key])
        output = dict_msg['Output']
        f = open("action_repo.txt",'r+')
        lines=f.readlines()
        n=len(action_tag)
    #    print("Number of action accociated "+str(n))
        userid=dict_msg['UserID']

        for i in range(n):
            for line in lines:
                name=line.split()
                if(name[0]==action_tag[i]):
    #                print(name[1])
                    call_file=name[1]+" "+userid
                    os.system(call_file)
    #                email_method()
                    
                    break
#     action_list = dict_msg['Action']
#     print("Number of dict accociated "+str(len(action_list)))
#     action_tag=[]
#     temp_list=action_list[0]
#     for key in temp_list:
#         action_tag.append(temp_list[key])
#     output = dict_msg['Output']
#     f = open("action_repo.txt",'r+')
#     lines=f.readlines()
#     n=len(action_tag)
# #    print("Number of action accociated "+str(n))
#     userid=dict_msg['UserID']
#     for i in range(n):
#         for line in lines:
#             name=line.split()
#             if(name[0]==action_tag[i]):
# #                print(name[1])
#                 call_file=name[1]+" "+userid
#                 os.system(call_file)
# #                email_method()
                
#                 break

#topic="actionserver"
#t1 = threading.Thread(target=consumer_t,args=(topic,))
#t1.start()
#import sys
#sys.path.insert(0, "./communication_module")
#
#import communication_module as cm
fun1=action_handler
start_new_thread(communication_module.RuntimeServer_to_ActionServer_interface(fun1),())

# producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))