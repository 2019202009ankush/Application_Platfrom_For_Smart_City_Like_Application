from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers = 'localhost:9092')

def send_message(topic,msg):
		producer.send(topic, msg.encode('utf-8'))
