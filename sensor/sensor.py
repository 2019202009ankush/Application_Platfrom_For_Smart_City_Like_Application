import json
from bson import json_util
import producer_json
import random
import time

def sensor_run(i,typ,loc,ip,port):
	
	with open('meta.json') as f:
		meta = json.load(f)
	# print(meta[typ])
	rang=meta[typ]['range']
	# frequency=meta[typ]['frequency']
	type_=meta[typ]['type']
	if type_ == 'real':
		min_limit_of_data=meta[typ]['min']
		max_limit_of_data=meta[typ]['max']


	topic= typ+'_'+i
	# print('#topic=',topic)
	message={}
	message['type']=typ
	message['id']= i
	message['location']=loc
	message['location_type']=None #GPS or room no
	message['range']=rang
	message['data']=random.randrange(int(min_limit_of_data), int(max_limit_of_data))

	producer_json.send_message(topic,message)


def sensor(id,typ,loc,ip,port,start_time=None,end_time=None,itr=None):
	ff=open('../SensorManager/SensorRegistry.txt','a+')
	s=loc+'_'+typ

	meta=typ+'_'+id
	ff.write(s+':'+meta)
	ff.write("\n")
	ff.close()

	if itr is None:
		while 1:
			time.sleep(4)
			sensor_run(id,typ,loc,ip,port)
	else:
		for i in range (itr):
			time.sleep(4)
			sensor_run(id,typ,loc,ip,port)




