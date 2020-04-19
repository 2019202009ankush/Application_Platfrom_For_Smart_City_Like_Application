from kafka import KafkaConsumer

def consume_message(topic):
	consumer = KafkaConsumer(topic)
	for mess in consumer:
		key=str(mess.key.decode())
		value=str(mess.value.decode())
		print(key,value)
		print(type(key),type(value))

print(consume_message('Servers'))
# print(consume_message('Servers'))
# print(consume_message('Servers'))
