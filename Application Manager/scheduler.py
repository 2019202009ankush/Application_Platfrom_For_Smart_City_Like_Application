# from kafka import KafkaConsumer

# def consume_message(topic):
# 	consumer = KafkaConsumer(topic)
# 	for mess in consumer:
# 		return str(mess.value.decode())
# 		break


from kafka import KafkaConsumer


consumer = KafkaConsumer("ApplicationManager_to_Scheduler")
for mess in consumer:
	s= str(mess.value.decode())
	print(s)
	break
