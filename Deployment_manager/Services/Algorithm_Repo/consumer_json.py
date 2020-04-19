from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

consumer.subscribe(['ApplicationManager_to_ServiceLifeCycle'])        
for message in consumer:
            print (message.value)