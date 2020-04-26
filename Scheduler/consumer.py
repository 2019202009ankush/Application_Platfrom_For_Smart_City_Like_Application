# importing the required module 
# 
from kafka import KafkaConsumer
from json import loads
from time import sleep
from json import dumps
from kafka import KafkaProducer
from _thread import *
import json


#print("Create Topic")
#topic=input()
file1=open("login.txt","r+")
# file2=open("contact.txt","r+")

def register(varify):
    print("Type id")
    file1.write("\n")
    file1.write(varify)
#    file
    print("Registered.")
    
    
def validation(varify):
    

    validate=False
    varify=varify+" :"
    lines1=file1.readlines()
    print(lines1)
    for line1 in lines1:
#        print(line1)
        print(line1.strip())
        if(line1.strip()==varify):
            validate=True
            
    if validate==False:
        print("Invalid User")
        print("Do you want to register?")
        answer=input()
        if(answer=="yes"):
            register(varify)
        else:    
            exit()
    else:
        print("validated")


print("Enter Id")
topic_own=input()
validation(topic_own)

consumer = KafkaConsumer(
     topic_own,
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     value_deserializer=lambda x: loads(x.decode('utf-8')))


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


    
    
def add_contact():
    global topic_own
    print("Enter details")
    details=input()
    lines1=file1.readline()
    req=topic_own + " :"
    print(req)
    for line in lines1:
        print(line)
        file1.seek(0)
        if(line.strip()==req):
            file1.write(details)
            
    
    
    
def to_recv():
    for message in consumer:
        message = message.value
#        print(lst)
        lst=message.split(' ',1)
        print(lst)
#        print(lst)
        if(len(lst)<2):
            print("Two arguments req.")
            return
        first=lst[0]
        sec=lst[1]
        print(first,":",sec)
        if(str(sec)=="bye"):
            return
    
def to_send():
    global topic_own
    
    # print("to whom?")
    # topic=input()
    # data=input()
    # data=topic_own+" "+data
    topic="pandey"
    # with open('meta.json') as f:
    #     for line in f:
    #         d = yaml.safe_load(line)
    #         jd = json.dumps(d)
    #         producer.send_messages(b'zeus_metrics',jd)
    f= open('meta.json',) 
    data = json.load(f) 

    meta_data={}
    for i in data['scheduler']:
         meta_data.update(i)
    data=meta_data
    producer.send(topic,value=data)       
    sleep(1)
    
start_new_thread(to_recv,())
while(1):
    
    print("What to do?")
    inp=input()
    
    if(inp=="send"):
        to_send()
        
    if(inp=="add_contact"):
        add_contact()
        
    
#    if(inp=="recv"):
#        to_recv()
        



    
