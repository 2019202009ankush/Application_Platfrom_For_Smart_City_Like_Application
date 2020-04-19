from kafka import KafkaConsumer

def consume_message(topic):
	consumer = KafkaConsumer(topic)
	for mess in consumer:
		return str(mess.value.decode())
		break

