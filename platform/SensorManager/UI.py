from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))
def UI(topic='Temperature'):
	consumer.subscribe([topic])    
	for message in consumer:
	            print (message.value)
