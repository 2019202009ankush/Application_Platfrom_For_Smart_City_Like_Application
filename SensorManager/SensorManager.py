import sys
import sensor
sys.path.insert(0,"../communication_module")
import threading
import communication_module

def event1(msg):
	loc=msg['location']
	sensors=msg['algoid']['sensors']
	
	print(loc)
	print(sensors)  
	
	import json 
	with open('SensorRegistry.txt') as f:
			lines = f.read().splitlines()
	ids=[]
	topics=[]
	if loc != 'all':
		sensors_obj=loc+'_'+sensors[0]
		for l in lines:
			if(l.split(':')[0]==sensors_obj):
				ids.append(l.split(':')[1].split('_')[1])
				topics.append(l.split(':')[1].split('_')[0])
	else:
		
		sensors_obj=sensors[0]
		for l in lines:
			if(l.split(':')[0].split('_')[2]==sensors_obj):
				ids.append(l.split(':')[1].split('_')[1])
				topics.append(l.split(':')[1].split('_')[0])
	
	msg['topics']=topics
	msg['ids']=ids
	print("Sensor Manager",msg)
	th1 = threading.Thread(target=sensor.sensor,kwargs={'id':ids[0],'typ':topics[0],'loc':loc,'ip':'0.0.0.0','port':'9557'})
	th1.start()
	communication_module.SensorManager_to_DeployManager_Producer_interface(msg)


	# Input format
	# {
	#   "location":"obh_112",
	#   "sensors": ["temparature","humidity"]
	# }
	# Output format
	# { 
	#   "topics" : ["temparature","humidity"],
	#   "ids"    : ["temp1","hum12"]
	# }

fun=event1
communication_module.DeployManager_to_SensorManager_interface(fun)
