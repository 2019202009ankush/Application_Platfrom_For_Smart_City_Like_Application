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
import os
# topic_own="pandey"

sys.path.insert(0, "platform/communication_module")

curpath=str(os.path.dirname(os.path.realpath(__file__)))

os.system("python3 "+curpath+"/dashboard/dashboard.py &")

file=open(curpath+"/dashboard/running.txt","w")
file.close()
import communication_module as cm

# file=open("running.txt","a+")

current_process=None
print("\n[Schedular] - started\n")
## using global deque with firstcome first serve schedule.
dq = collections.deque() 

queue=[]
meta_data=None

#funstion to send data to service life cycle module when its turn comes.
def to_servicelifecycle():


    global meta_data
    global dq
    curpath=str(os.path.dirname(os.path.realpath(__file__)))
    file=open(curpath+"/dashboard/running.txt","a")
    file.write(str(meta_data["algoid"])+" at location "+meta_data["location"]+" is running "+ "from "+meta_data["start_time"])
    file.close()
    cm.Schedular_to_ServiceLifeCycle_Producer_interface(meta_data)

global x,y,z,a

#the below functions are called according to the scheduling requirement of the user

def regular(days,start_time,duration,algo):
    global x
    x=schedule.every().days.at(start_time).do((to_servicelifecycle))


def notregular(days,start_time,duration,algo):
    global y
    y=schedule.every().days.at(start_time).do((to_servicelifecycle)) 


# def immediate(duration,algo):
#     global z
#     z=schedule.every().day.do(to_servicelifecycle) 


def period(duration,start,algo):
    global a

    name=algo
    this_module = sys.modules[__name__]
    
    a=schedule.every(int(duration)).minutes.at(start).do((to_servicelifecycle))


#If priority is high push the data in front of the queue
def inputq(msg):
    global dq
    


    if(msg["priority"]=="high"):
        # print("hey ya")
        dq.appendleft(msg)
    else:
        dq.append(msg)
    # print("message",msg)

#function  to receive meta_data from application manager
def to_recv():
	cm.ApplicationManager_to_Scheduler_interface(inputq)


#function to check is there is any pending service to br scheduled . For example a service is to be scheduled on "tuesdays",
#this function will ensure that it pushed in deque and considered 
def pending():
    while True: 
              
        schedule.run_pending() 
        time.sleep(1)   

i=0
start_new_thread(to_recv,())

## Calling respective functions according to the scheduling information received
def main():
    while(1):
        #print("Hello")
        global dq
        global meta_data
    

        while(len(dq)>0):

            #print("Hello 1")
            global i
            i=i+1


            meta_data=dq.popleft()
            # file=open("running.txt","a+")
            # file.write(str(meta_data["algoid"])+" at location "+meta_data["location"]+" is running "+ "from "+meta_data["start_time"])

            
            if(meta_data["form"]=="run"):


                if (meta_data["days"]=="everyday" and meta_data["request_type"]!="immediate" ):
                    regular(meta_data["days"],meta_data["start_time"],meta_data["duration"],meta_data["algo"])
                   

                elif (meta_data["days"]!="everyday" and meta_data["days"]!=""):
                    notregular(meta_data["days"],meta_data["start_time"],meta_data["duration"],meta_data["algo"])

                elif(meta_data["request_type"]=="immediate"):
                    # print("heyyyyyyyyyyyyyy")
                    # global file
                    print("\n [Schedular] : Scheduling immediately Service with id : ",meta_data["algoid"])
                    curpath=str(os.path.dirname(os.path.realpath(__file__)))
                    file=open(curpath+"/dashboard/running.txt","a")
                    # file=open("running.txt","a")
                    
                    file.write(str(meta_data["algoid"])+" at location "+meta_data["location"]+" is scheduled immediately\n")
                    file.close()

                    cm.Schedular_to_ServiceLifeCycle_Producer_interface(meta_data)
                    # immediate(meta_data["duration"],meta_data["algo"])


                elif(meta_data["request_type"]=="periodic"):
                    print("in periodic scheduling")
                    period(meta_data["duration"],meta_data["start_time"],meta_data["algo"])

                start_new_thread(pending,())


            else:
                schedule.cancel_job(eval(meta_data["algo"]))



            

            
if __name__ == "__main__":
    main()

        



    

