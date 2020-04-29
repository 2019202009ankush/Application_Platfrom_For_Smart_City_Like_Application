from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',value_deserializer=lambda m: json.loads(m.decode('utf-8')))

consumer.subscribe(['numeric_attandance_d2'])    
for message in consumer:
            print (message.value)
