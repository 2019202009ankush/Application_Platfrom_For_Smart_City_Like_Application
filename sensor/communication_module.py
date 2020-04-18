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
			print(mess)
			th = threading.Thread(target=func_name)
			th.start()
            

def ApplicationManager_to_ServiceLifeCycle_Producer_interface(mess):
	producer_json.send_message('ApplicationManager_to_ServiceLifeCycle',mess)

# ServerLifeCycle_to_ServiceLifeCycle

def ServerLifeCycle_to_ServiceLifeCycle_interface(func_name):
	from kafka import KafkaConsumer
	topic='ServerLifeCycle_to_ServiceLifeCycle'
	
	consumer = KafkaConsumer(topic,bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

	# consumer.subscribe([topic]) 

	for message in consumer:
			mess= (message.value)
			print(mess)
			th = threading.Thread(target=func_name)
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
			th = threading.Thread(target=func_name)
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
			th = threading.Thread(target=func_name)
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
			th = threading.Thread(target=func_name)
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
			th = threading.Thread(target=func_name)
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
			th = threading.Thread(target=func_name)
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
			th = threading.Thread(target=func_name)
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
			th = threading.Thread(target=func_name)
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
			th = threading.Thread(target=func_name)
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
			th = threading.Thread(target=func_name)
			th.start()
            

def HealthManager_to_Registry_Producer_interface(mess):
	producer_json.send_message('HealthManager_to_Registry',mess)
    

# Sensor_Stream

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