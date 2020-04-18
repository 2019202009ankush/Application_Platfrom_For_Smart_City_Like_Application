import json
from bson import json_util
import producer_json
import random

def sensor_run(id,typ,loc,range,ip,port):
	
	with open('meta.json') as f:
		meta = json.load(f)
	# print(meta[typ])
	rang=meta[typ]['range']
	# frequency=meta[typ]['frequency']
	type_=meta[typ]['type']
	if type_ == 'real':
		min_limit_of_data=meta[typ]['min']
		max_limit_of_data=meta[typ]['max']


	topic= typ

	message={}
	message['type']=typ
	message['id']= id
	message['location']=loc
	message['location_type']=None #GPS or room no
	message['range']=rang
	message['data']=random.randrange(int(min_limit_of_data), int(max_limit_of_data))

	producer_json.send_message(topic,message)

def sensor(id,typ,loc,range,ip,port,start_time=None,end_time=None,itr=None):
	if itr is None:
		while 1:
			sensor_run(id,typ,loc,range,ip,port)
	else:
		for i in range (itr):
			sensor_run(id,typ,loc,range,ip,port)




