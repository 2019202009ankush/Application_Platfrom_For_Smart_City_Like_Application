import socket 
from _thread import *
import threading  
import re
import json
import jsonschema
from jsonschema import validate
from kafka import KafkaProducer
from zipfile import ZipFile
import os

import sys
# sys.path.insert(0,"/home/dell/Pictures/course_work/ias/group3_team1/cm/communication_module")
sys.path.insert(0, "../communication_module")
import communication_module as cm

configschema = {
    "type": "object",
    "properties": {
        "userid": {"type": "string"},
        "reqid": {"type": "string"},
        "appid": {"type": "string"},
        "algoid": {"type": "string"},
        "action":{"type": "string"},
        "location":{"type": "string"},
        "sensortype":{"type": "string"},
        "old/runningservice":{"type":"string"},
    },
}
userid={}
reqid=1



def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=configschema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def threaded(c): 
    # print("rg")
    global reqid
    id=str(c.recv(4).decode('utf-8'))
    id=int(id)
    # print(id)
    c.send(b'hello')
    if(id==1):

        user_name=str(c.recv(40).decode('utf-8'))
        c.send(b'hello')
        pass_word=str(c.recv(40).decode('utf-8'))

        userid[user_name]=pass_word
        c.send(bytes(str(1), 'utf8'))
        c.recv(4)
        c.send(bytes(str("Welcome"), 'utf8'))
        c.recv(4)
        c.send(bytes(str("http://127.0.0.1:1234/"), 'utf8'))
        fil=str(c.recv(40).decode('utf-8'))
        if(fil=="filled"):
            conf={}
            zi="./config/"+user_name+".zip"
            # print(zi)
            with ZipFile(zi, 'r') as zipObj:
                zipObj.extractall("./config/")
            filename="./config/"+user_name+"/"+user_name+"_config.txt"
            con=[]
            # logmsg={}
            # logmsg['component']='Application_Manager'
            # logmsg['msg']="User config recieved"
            # cm.common_Logger_Producer_interface(logmsg)
            with open(filename) as f1:
                con=f1.readlines()
                con = [x.rstrip() for x in con] 

            # print(con)
            for i in range(len(con)):
                s=con[i]
                y=[]
                y=s.split(":")
                if(y[0]=="start_time" or y[0]=="end_time"):
                    y[1]=y[1]+":"+y[2]
                conf[y[0]]=str(y[1])
            conf["reqid"]=str(reqid)
            y_n=conf["old/runningservice"]
            reqid=reqid+1
            y1 = json.dumps(conf)    #Python to JSON
            jsonData = json.loads(y1)       #JSON to Python
            isValid = validateJson(jsonData)
            if isValid:
                print("Given JSON data is Valid")
                confjson=json.dumps(jsonData) 
                # print(confjson)
                c1=confjson
                old_stamp=0
                while(1):
                    stamp = os.stat("./dynamic.txt").st_mtime
                    if(stamp != old_stamp):
                        old_stamp = stamp
                        filenam="./dynamic.txt"
                        with open(filenam) as f1:
                            dy1=f1.readlines()
                            dy1 = [x.rstrip() for x in dy1]
                        print(dy1) 
                        dy=dy1[0]
                        tr=dy
                        tr=eval(tr)
                        print(tr)
                        confjson=c1
                        print(confjson)
                        confjson1=eval(confjson)
                        if(str(tr["app_id"])==str(confjson1["app_id"])):
                            dy2=dy[1:]
                            confjson=confjson[:-1]+", "+dy2
                            confjson=eval(confjson)
                            print(confjson)
                            print(confjson['start_time'])
                            # if(y_n=="yes"):
                            #     cm.ApplicationManager_to_ServiceLifeCycle_Producer_interface(confjson)
                            # else:
                            cm.ApplicationManager_to_Scheduler_Producer_interface(confjson)
                            # logmsg1={}
                            # logmsg1['component']='Application_Manager'
                            # logmsg1['msg']="Config sent to Scheduler"
                            # cm.common_Logger_Producer_interface(logmsg1)
            else:
                print(jsonData)
                print("Given JSON data is InValid")
    if(id==2):
        # print("EXISTING")

        user_name=str(c.recv(40).decode('utf-8'))
        c.send(b'hello')
        pass_word=str(c.recv(40).decode('utf-8'))
        # print(user_name)
        # print(pass_word)
        if user_name in userid and pass_word==userid[user_name]:
            c.send(bytes(str(1), 'utf8'))
            c.recv(4)
            c.send(bytes(str("Welcome"), 'utf8'))
            c.recv(4)
            c.send(bytes(str("http://127.0.0.1:4555/"), 'utf8'))
            fil=str(c.recv(40).decode('utf-8'))
            if(fil=="filled"):
                conf={}
                zi="./config/"+user_name+".zip"
                print(zi)
                with ZipFile(zi, 'r') as zipObj:
                    zipObj.extractall("./config/")
                filename="./config/"+user_name+"/"+user_name+"_config.txt"
                con=[]
                # logmsg={}
                # logmsg['component']='Application_Manager'
                # logmsg['msg']="User config recieved"
                # cm.common_Logger_Producer_interface(logmsg)
                with open(filename) as f1:
                    con=f1.readlines()
                    con = [x.rstrip() for x in con] 
                # print(con)
                for i in range(len(con)):
                    s=con[i]
                    y=[]
                    y=s.split(":")
                    if(y[0]=="start_time" or y[0]=="end_time"):
                        y[1]=y[1]+":"+y[2]
                    conf[y[0]]=str(y[1])
                conf["reqid"]=str(reqid)
                y_n=conf["old/runningservice"]
                reqid=reqid+1
                y1 = json.dumps(conf)    #Python to JSON
                jsonData = json.loads(y1)       #JSON to Python
                isValid = validateJson(jsonData)
                if isValid:
                    print("Given JSON data is Valid")
                    confjson=json.dumps(jsonData) 
                    # print(confjson)
                    c1=confjson
                    old_stamp=0
                    while(1):
                        stamp = os.stat("./dynamic.txt").st_mtime
                        if(stamp != old_stamp):
                            old_stamp = stamp
                            filenam="./dynamic.txt"
                            with open(filenam) as f1:
                                dy1=f1.readlines()
                                dy1 = [x.rstrip() for x in dy1] 
                            dy=dy1[0]
                            tr=dy
                            tr=eval(tr)
                            print(tr)
                            confjson=c1
                            print(confjson)
                            confjson1=eval(confjson)
                            if(str(tr['app_id'])==str(confjson1['app_id'])):
                                dy2=dy[1:]
                                confjson=confjson[:-1]+", "+dy2
                                confjson=eval(confjson)
                                print(confjson)
                                print(confjson['start_time'])
                                # if(y_n=="yes"):
                                #     cm.ApplicationManager_to_ServiceLifeCycle_Producer_interface(confjson)
                                # else:
                                cm.ApplicationManager_to_Scheduler_Producer_interface(confjson)
                                # logmsg1={}
                                # logmsg1['component']='Application_Manager'
                                # logmsg1['msg']="Config sent to Scheduler"
                                # cm.common_Logger_Producer_interface(logmsg1)
                else:
                    print(jsonData)
                    print("Given JSON data is InValid")




        else:
            c.send(bytes(str(11), 'utf8'))
            c.recv(4)
            c.send(bytes(str("Welcome"), 'utf8'))
            c.recv(4)
            c.send(bytes(str("Invalid Credentials"), 'utf8'))

    c.close()


# https://docs.google.com/forms/d/e/1FAIpQLSeLxmpyREIhQcdlaGGZ1jlBF5_pswgYN29JZ4xGWB5Alq7ZSw/viewform?usp=sf_link



filename="name_password.txt"


def Main(): 

    content=[]
    with open(filename) as f:
        content=f.readlines()
        content = [x.rstrip() for x in content] 

    for i in range(len(content)):
        s=content[i]
        y=[]
        y=s.split(":")
        userid[y[0]]=y[1]

    host = "" 
    print("Enter port no:")
    port = int(input())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
    s.listen(5) 
    print("socket is listening") 
    while True: 
        c, addr = s.accept() 
        start_new_thread(threaded, (c,))
    s.close() 
    
if __name__ == '__main__': 
    Main() 
