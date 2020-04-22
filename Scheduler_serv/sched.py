# importing the required module 
# 
from kafka import KafkaConsumer
from json import loads
from time import sleep
from json import dumps
from kafka import KafkaProducer
from _thread import *
import json 
import schedule 
import sys
import datetime

import time
import collections 
# topic_own="pandey"

sys.path.insert(0, "/home/dell/Pictures/course_work/ias/group3_team1/cm/communication_module")

import communication_module as cm





dq = collections.deque() 
# consumer = KafkaConsumer(
#      topic_own,
#      bootstrap_servers=['localhost:9092'],
#      auto_offset_reset='latest',
#      enable_auto_commit=True,
#      value_deserializer=lambda x: loads(x.decode('utf-8')))


# producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
#                          value_serializer=lambda x: 
#                          dumps(x).encode('utf-8'))




queue=[]

def algo1(): 
    print("algo1 is running") 
  
def algo2(): 
    print("algo2 is running") 
  
def algo3(): 
    print("algo3 is running")
global x,y,z,a

def regular(days,start_time,duration,algo):
    global x
    x=schedule.every(int(duration)).day.at(start_time).do(eval(algo))


def notregular(start_time,end_time,duration,algo):
    global y
    y=schedule.every(int(duration)).tuesday.at(start_time).do(eval(algo)) 


def immediate(duration,algo):
    global z
    print("here")
    # z=schedule.every(int(duration)).seconds.do(eval(algo))
    z=schedule.every(int(duration)).seconds.do(algo1) 


def period(duration,start,algo):
    global a

    name=algo
    this_module = sys.modules[__name__]
    
    a=schedule.every(int(duration)).hour.do(getattr(this_module, name)) 


def inputq(msg):
    global dq
    msg= json.loads(msg) 
    print(type(msg))
    cm.Schedular_to_ServiceLifeCycle_Producer_interface(msg)

    # for message in consumer:
        
    #     print("inside dequeue")
    #     # start_new_thread(recv_thread,())
    #     message = message.value
    if(msg["priority"]=="high"):
        print("hey ya")
        dq.appendleft(msg)
    else:
        dq.append(msg)
    print("message",msg)

def to_recv():
    # start_new_thread(inputq,())
    print("yaha")
    cm.ApplicationManager_to_Scheduler_interface(inputq)

    
    
def to_send():
    global topic_own
    
    print("to whom?")
    topic=input()
    data=input()
    data=topic_own+" "+data
    producer.send(topic,value=data)
    sleep(1)
    


def pending():
    while True: 
              
        schedule.run_pending() 
        time.sleep(1)   

i=0
start_new_thread(to_recv,())
def main():
    while(1):

        global dq
        # global loq
        while(len(dq)>0):
            # print("length of queue",loq)
            global i
            i=i+1
            meta_data=dq.pop()
            # loq=loq-1
            print("in while",meta_data)
            print(i)
            if(meta_data["form"]=="run"):


                if (meta_data["days"]=="everyday"):
                    # strg="geeks"
                    # schedule.every(1).seconds.do(eval("geeks"))
                    regular(meta_data["days"],meta_data["start_time"],meta_data["duration"],meta_data["algo"])
                   

                elif (meta_data["days"]!="everyday" and meta_data["days"]!=""):
                    notregular(meta_data["days"],meta_data["start_time"],meta_data["duration"],meta_data["algo"])

                elif(meta_data["request_type"]=="immediate"):
                    print("Scheduling immediately")
                    immediate(meta_data["duration"],meta_data["algo"])

                elif(meta_data["request_type"]=="periodic"):
                    print("in periodic scheduling")
                    period(meta_data["duration"],meta_data["start_time"],meta_data["algo"])

                start_new_thread(pending,())


            else:

                schedule.cancel_job(eval(meta_data["algo"]))



            

            
if __name__ == "__main__":
    main()

        



    
