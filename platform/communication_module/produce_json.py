import json
from bson import json_util
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers = 'localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
def send_message(topic,message):
	for i in range (2):
		producer.send('ApplicationManager_to_ServiceLifeCycle',message)