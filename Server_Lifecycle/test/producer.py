from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

while(1):
    inp=input()
    producer.send('Servers', value=inp)
    if(inp=='quit'):
        break
    sleep(1)
