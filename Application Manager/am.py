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
configschema = {
    "type": "object",
    "properties": {
        "userid": {"type": "number"},
        "reqid": {"type": "number"},
        "appid": {"type": "number"},
        "algoid": {"type": "number"},
        "priority":{"type": "string"},
        "action":{"type": "string"},
        "start":{"type": "number"},
        "end":{"type": "number"},
        "duration":{"type": "number"},
        "location":{"type": "string"},
        "frequency":{"type": "number"},
        "freq_days":{"type": "number"},
        "sensortype":{"type": "string"},
        "requesttype":{"type": "string"},
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
    	c.send(bytes(str("http://127.0.0.1:4555/"), 'utf8'))
    	fil=str(c.recv(40).decode('utf-8'))
    	if(fil=="filled"):
    		conf={}
    		zi="/home/srg/Desktop/2sem/IAS/hack2/config/"+user_name+".zip"
    		print(zi)
    		with ZipFile(zi, 'r') as zipObj:
    			zipObj.extractall("/home/srg/Desktop/2sem/IAS/hack2/config/")
    		filename="/home/srg/Desktop/2sem/IAS/hack2/config/"+user_name+"/"+user_name+"_config.txt"
    		con=[]
    		with open(filename) as f1:
    			con=f1.readlines()
    			con = [x.rstrip() for x in con] 

    		# print(con)
    		for i in range(7):
    			s=con[i]
    			y=[]
    			y=s.split(":")
    			conf[y[0]]=int(y[1])
    		for i in range(7,len(con)):
    			s=con[i]
    			y=[]
    			y=s.split(":")
    			conf[y[0]]=y[1]
    		conf["reqid"]=reqid
    		y_n=conf["old/runningservice"]
    		reqid=reqid+1
    		y1 = json.dumps(conf)    #Python to JSON
    		jsonData = json.loads(y1)       #JSON to Python
    		isValid = validateJson(jsonData)
    		if isValid:
    			print("Given JSON data is Valid")
    			confjson=json.dumps(jsonData) 
    			print(confjson)
    			producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
    			if(y_n=="yes"):
    				producer.send("ApplicationManager_to_ServiceLifeCycle", confjson.encode('utf-8'))
    			else:
    				producer.send("ApplicationManager_to_Scheduler", confjson.encode('utf-8'))
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
    			zi="/home/srg/Desktop/2sem/IAS/hack2/config/"+user_name+".zip"
    			print(zi)
    			with ZipFile(zi, 'r') as zipObj:
    				zipObj.extractall("/home/srg/Desktop/2sem/IAS/hack2/config/")
    			filename="/home/srg/Desktop/2sem/IAS/hack2/config/"+user_name+"/"+user_name+"_config.txt"
    			con=[]
    			with open(filename) as f1:
    				con=f1.readlines()
    				con = [x.rstrip() for x in con] 

    		# print(con)
    			for i in range(7):
    				s=con[i]
    				y=[]
    				y=s.split(":")
    				conf[y[0]]=int(y[1])
    			for i in range(7,len(con)):
    				s=con[i]
    				y=[]
    				y=s.split(":")
    				conf[y[0]]=y[1]
    			conf["reqid"]=reqid
    			y_n=conf["old/runningservice"]
    			reqid=reqid+1
    			y1 = json.dumps(conf)    #Python to JSON
    			jsonData = json.loads(y1)       #JSON to Python
    			isValid = validateJson(jsonData)
    			if isValid:
    				print("Given JSON data is Valid")
    				confjson=json.dumps(jsonData) 
    				print(confjson)
    				producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
    				if(y_n=="yes"):
    					producer.send("ApplicationManager_to_ServiceLifeCycle", confjson.encode('utf-8'))
    				else:
    					producer.send("ApplicationManager_to_Scheduler", confjson.encode('utf-8'))
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
