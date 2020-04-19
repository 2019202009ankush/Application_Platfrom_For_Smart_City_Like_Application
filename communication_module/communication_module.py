import producer
import threading
import time
import producer_json


import json
from bson import json_util

# ApplicationManager_to_ServiceLifeCycle

def ApplicationManager_to_ServiceLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='ApplicationManager_to_ServiceLifeCycle'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			#print("mess:",mess)
			th = threading.Thread(target=func_name,kwargs={'m1':mess})
			th.start()
            

def ApplicationManager_to_ServiceLifeCycle_Producer_interface(mess):
	producer_json.send_message('ApplicationManager_to_ServiceLifeCycle',mess)



#common log receiver
def common_Logger_interface(func_name):
	from kafka import KafkaConsumer
	topic='common_Logger'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			# print("mess:",mess)
			th = threading.Thread(target=func_name,kwargs={'m1':mess})
			th.start()
			break

#LOGGING INTERFACE with scheduler

def Scheduler_to_Logger_Producer_interface(mess):
	producer_json.send_message('common_Logger',mess)


#LOGGING INTERFACE with deployer
def Deployer_to_Logger_Producer_interface(mess):
	producer_json.send_message('common_Logger',mess)




##########Monitoring module

#Mon Module scheduler receiver
def Scheduler_to_Monitoring_Module_interface(func_name):
	from kafka import KafkaConsumer
	topic='Scheduler_to_Monitoring_Module'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			# print("mess:",mess)
			th = threading.Thread(target=func_name,kwargs={'m1':mess})
			th.start()
			break

#Mon INTERFACE with scheduler

def Scheduler_to_Monitoring_Module_Producer_interface(mess):
	producer_json.send_message('Scheduler_to_Monitoring_Module',mess)


#Mon Module receiver Deployer
def Deployer_to_Monitoring_Module_interface(func_name):
	from kafka import KafkaConsumer
	topic='Deployer_to_Monitoring_Module'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			# print("mess:",mess)
			th = threading.Thread(target=func_name,kwargs={'m1':mess})
			th.start()
			break

#Mon INTERFACE with scheduler

def Deployer_to_Monitoring_Module_Producer_interface(mess):
	producer_json.send_message('Deployer_to_Monitoring_Module',mess)

########Reverse Mon module comm

#Mon Module - scheduler receiver
def Monitoring_Module_to_Scheduler_interface(func_name):
	from kafka import KafkaConsumer
	topic='Monitoring_Module_to_Scheduler'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			# print("mess:",mess)
			th = threading.Thread(target=func_name,kwargs={'m1':mess})
			th.start()
			break

#Mon INTERFACE with scheduler

def Monitoring_Module_to_Scheduler_Producer_interface(mess):
	producer_json.send_message('Monitoring_Module_to_Scheduler',mess)


#Mon Module receiver Deployer
def Monitoring_Module_to_Deployer_interface(func_name):
	from kafka import KafkaConsumer
	topic='Monitoring_Module_to_Deployer'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			# print("mess:",mess)
			th = threading.Thread(target=func_name,kwargs={'m1':mess})
			th.start()
			break

#Mon INTERFACE with scheduler

def Monitoring_Module_to_Deployer_Producer_interface(mess):
	producer_json.send_message('Monitoring_Module_to_Deployer',mess)



#TOPO MANAGER to Service Lc
def TopoManager_to_ServiceLifeCycle_Producer_interface(mess):
	producer_json.send_message('TopoManager_to_ServiceLifeCycle',mess)

def TopoManager_to_ServiceLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='TopoManager_to_ServiceLifeCycle'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print("failing message2:",msg)
			# print("mess:",mess)
			# th = threading.Thread(target=func_name,kwargs={'m1':mess})
			# th.start()
			# break


#TOPO MANAGER to Server Lc
def TopoManager_to_ServerLifeCycle_Producer_interface(mess):
	producer_json.send_message('TopoManager_to_ServerLifeCycle',mess)

def TopoManager_to_ServerLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='TopoManager_to_ServerLifeCycle'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print("failing mess:",mess)
			# th = threading.Thread(target=func_name,kwargs={'m1':mess})
			# th.start()
			# break

####################ACtion Server
# Action Server

def RuntimeServer_to_ActionServer_interface(func_name):
	from kafka import KafkaConsumer
	topic='RuntimeServer_to_ActionServer'
	num=0
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 
	for message in consumer:
            mess= (message.value)
            num+=1
            print("msg!!!!!",mess)
            # action_handler(mess)
            print("Action # "+str(num))
            print("call threading")
            th = threading.Thread(target=func_name,kwargs={'message':mess})
            th.start()
            # break

def RuntimeServer_to_ActionServer_Producer_interface(mess):
	producer_json.send_message('RuntimeServer_to_ActionServer',mess)



# ServerLifeCycle_to_ServiceLifeCycle

def ServerLifeCycle_to_ServiceLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='ServerLifeCycle_to_ServiceLifeCycle'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def ServerLifeCycle_to_ServiceLifeCycle_Producer_interface(mess):
	producer_json.send_message('ServerLifeCycle_to_ServiceLifeCycle',mess)
    
    

# ServiceLifeCycle_to_ServerLifeCycle

def ServiceLifeCycle_to_ServerLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='ServiceLifeCycle_to_ServerLifeCycle'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def ServiceLifeCycle_to_ServerLifeCycle_Producer_interface(mess):
	producer_json.send_message('ServiceLifeCycle_to_ServerLifeCycle',mess)
    
    

# ServiceLifeCycle_to_Authentication

def ServiceLifeCycle_to_Authentication_interface(func_name):
	from kafka import KafkaConsumer
	topic='ServiceLifeCycle_to_Authentication'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def ServiceLifeCycle_to_Authentication_Producer_interface(mess):
	producer_json.send_message('ServiceLifeCycle_to_Authentication',mess)
    
    

# Authentication_to_ServiceLifeCycle

def Authentication_to_ServiceLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='Authentication_to_ServiceLifeCycle'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def Authentication_to_ServiceLifeCycle_Producer_interface(mess):
	producer_json.send_message('Authentication_to_ServiceLifeCycle',mess)
    

# ServiceLifeCycle_to_DeployManager

def ServiceLifeCycle_to_DeployManager_interface(func_name):
	from kafka import KafkaConsumer
	topic='ServiceLifeCycle_to_DeployManager'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def ServiceLifeCycle_to_DeployManager_Producer_interface(mess):
	producer_json.send_message('ServiceLifeCycle_to_DeployManager',mess)
    
    

# Schedular_to_ServiceLifeCycle

def Schedular_to_ServiceLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='Schedular_to_ServiceLifeCycle'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def Schedular_to_ServiceLifeCycle_Producer_interface(mess):
	producer_json.send_message('Schedular_to_ServiceLifeCycle',mess)

# Topology_to_ServiceLifeCycle

def Topology_to_ServiceLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='Topology_to_ServiceLifeCycle'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def Topology_to_ServiceLifeCycle_Producer_interface(mess):
	producer_json.send_message('Topology_to_ServiceLifeCycle',mess)

# Topology_to_Registry

def Topology_to_Registry_interface(func_name):
	from kafka import KafkaConsumer
	topic='Topology_to_Registry'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def Topology_to_Registry_Producer_interface(mess):
	producer_json.send_message('Topology_to_Registry',mess)
    
    

# HealthManager_to_ServiceLifeCycle

def HealthManager_to_ServiceLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='HealthManager_to_ServiceLifeCycle'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def HealthManager_to_ServiceLifeCycle_Producer_interface(mess):
	producer_json.send_message('HealthManager_to_ServiceLifeCycle',mess)
    
    


# HealthManager_to_Registry

def HealthManager_to_Registry_interface(func_name):
	from kafka import KafkaConsumer
	topic='HealthManager_to_Registry'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def HealthManager_to_Registry_Producer_interface(mess):
	producer_json.send_message('HealthManager_to_Registry',mess)
    

# SensorManager_to_DeployManager
def SensorManager_to_DeployManager_interface(func_name):
	from kafka import KafkaConsumer
	topic='SensorManager_to_DeployManager'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def SensorManager_to_DeployManager_Producer_interface(mess):
	producer_json.send_message('SensorManager_to_DeployManager',mess)
    
# DeployManager_to_SensorManager


def DeployManager_to_SensorManager_interface(func_name):
	from kafka import KafkaConsumer
	topic='DeployManager_to_SensorManager'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
            

def DeployManager_to_SensorManager_Producer_interface(mess):
	producer_json.send_message('DeployManager_to_SensorManager',mess)
    



def DeploymentManager_to_SensorManager_interface(func_name):
	from kafka import KafkaConsumer
	topic='DeploymentManager_to_SensorManager'
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()
		
def ApplicationManager_to_Scheduler_interface(func_name):
	from kafka import KafkaConsumer
	topic='ApplicationManager_to_Scheduler'
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()


def DeploymentManager_to_RuntimeServer_interface(func_name):
	from kafka import KafkaConsumer
	topic='DeploymentManager_to_RuntimeServer'
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name,kwargs={'msg':mess})
			th.start()

		
# def RuntimeServer_to_ActionServer_interface(func_name):
# 	print("in comm module ac")
# 	from kafka import KafkaConsumer
# 	topic='RuntimeServer_to_ActionServer'
# 	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# 	# consumer.subscribe([topic]) 

# 	for message in consumer:
# 			mess= (message.value)
# 			print(mess)
# 			th = threading.Thread(target=func_name,kwargs={'msg':mess})
# 			th.start()

def Sersor_Stream(type):
	from kafka import KafkaConsumer
	topic='RuntimeServer_to_ActionServer'
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',auto_offset_reset='earliest',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			yield mess
	return (get_stream())


# import os
# os.system('docker run --rm -it -p 2181:2181 -p 3030:3030 -p 8081:8081 -p 8082:8082 -p 8083:8083 -p 9092:9092 -e ADV_HOST=127.0.0.1 landoop/fast-data-dev')
# import json	
# with open('topic.json') as f:
# 		meta = json.load(f)
# l=meta['topic']
# for topic in l:
# 	print('Creating topic ', topic)
# 	producer.send_message(topic,"start")
