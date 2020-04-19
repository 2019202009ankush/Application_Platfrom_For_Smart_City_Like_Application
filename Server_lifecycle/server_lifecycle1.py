# import producer
# import consumer
from kafka import KafkaConsumer
from kafka import KafkaProducer
import psutil
import os
import time
import sys
import json
import threading
from time import sleep
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

mutex=1

stats={}

server_details={}

from pymongo import MongoClient 
  
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB")


db = conn['server_life_cycle']
db_serv_det=db['server_details']
db_serv_stats=db['server_stats']


def consume_message(topic):
	consumer = KafkaConsumer(topic)
	for mess in consumer:
		key=str(mess.key.decode())
		value=str(mess.value.decode())
		print(type(key),type(value))


def update_stats():
	global stats
	global mutex
	consumer = KafkaConsumer("Servers")
	for mess in consumer:
		key=str(mess.key.decode())
		value=str(mess.value.decode())
		#lock
		while(mutex==0):
			pass
		mutex=0
		stats[key]=value
		ll=value.split("|")
		result = db_serv_stats.update_one( 
			        {"id":key}, 
			        	{ 
			                "$set":{ 
			                        "cpu":ll[0],
			                        "ram":ll[1],
			                        "time":ll[2],
			                        "services":ll[3]
			                       }
			            } 
			        )
		
		now=datetime.now()
		for k,v in stats.items():
			l=v.split("|")
			parsed_time=datetime.strptime(l[2],"%Y-%m-%d %H:%M:%S.%f")
			diff=(now-parsed_time).total_seconds()
			print(k,diff)
			if(diff>=90):
				server_details[k]['active']=0
				db_serv_det.update_one(
					{"id":k}, 
			        	{ 
			                "$set":{ 
			                        "active":0,
			                       }
			                  
			            }
					)
				fault_tolerant(producer,k,l[3])
			else:
				print("Updated : ",key,value)

		#unlock
		mutex=1


def run_service(producer,server_id,service_name):
	msg=service_name
	producer.send('ServiceToServer',key=bytes(str(server_id), 'utf8'),value=bytes(str(msg), 'utf8'))
	print("Sent to Server lifecycle manager : ",server_id,msg)


def fault_tolerant(producer,server_id,value):
	print("Server with ",server_id," went down with the service running",value)
	ids=value.split(';')
	print(ids)
	#load_balance()
	s_id=load_balancer()
	for id in ids:
		if(id==""):
			continue
		run_service(producer,s_id,id)



def get_all_server_details():
	global server_details
	f = open('server_details.json',) 
	data = json.load(f) 
	# for i in data:
	# 	print(i)
	print(data)
	server_details=data

	for k,v in data.items():
		print(k)
		db_serv_det.insert_one(v)
		tt={}
		tt["id"]=k
		db_serv_stats.insert_one(tt)

def start_server():
	global server_details
	_server=None
	for i in server_details:
		if server_details[i]['active']==0:
			_server=i
			break

	if(_server==None):
		print("All servers are active")
		return

	server_details[_server]['active']=1
	db_serv_det.update_one(
		{"id":_server}, 
        	{ 
                "$set":{ 
                        "active":1,
                       }
                  
            }
		)
	cwd = os.getcwd()
	print(server_details[_server],_server,server_details[_server]['ip'],server_details[_server]['port'])
	cmd="gnome-terminal -- python3 -i "+cwd+"/server_stat.py "+str(_server)+" "+str(server_details[_server]['ip'])+" "+str(server_details[_server]['port'])
	os.system(cmd)
	# print(cmd)
	print("Server started")


def start_server_with_stats():
	pass

def release_server():
	pass

def get_server_stats(server_id):
	return stats[server_id]

def thershold_check():
	pass


def compute_load(cpu,mm):
	def 2*cpu*mm/(cpu+mm)

def load_balancer():
	loads=[]
	print("Load Balancing")
	for k,v in stats.items():
		print(k,v)
		if(server_details[k]['active']==1):
			ll=v.split('|')
			load=compute_load(float(ll[0]),float(ll[1]))
			loads.append([load,k])

	loads.sort()
	print(loads)
	return loads[0][1]


if __name__ == '__main__':
	get_all_server_details()
	t1 = threading.Thread(target=update_stats, args=()) 
	t1.start()
	# start_server()
	# start_server()
	# start_server()

	print("Server Details")
	for k,v in server_details.items():
		print(k,v)

	while(1):
		#print("Each server stats : ")
		# #lock
		# while(mutex==0):
		# 	pass
		# mutex=0
		# for k,v in stats.items():
		# 	print(k,v)
		# #unlock
		# mutex=1
		# sleep(20)
		inp=input("Enter command : ")  		##run server_id service_name
		commands=inp.split(" ")
		if(commands[0]=="run"):
			run_service(producer,commands[1],commands[2])
		if(commands[0]=="start_server"):
			start_server()



		
	t1.join() 
	print("Bye!") 
