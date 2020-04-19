import sys
sys.path.insert(0,"../communication_module")

import communication_module

def event1(msg):
	loc=msg['location']
	sensors=msg['algoid']['sensors']
	
	print(loc)
	print(sensors)	
	
	import json	
	with open('SensorRegistry.txt') as f:
    		lines = f.read().splitlines()
	print(lines)
	ids=[]
	topics=[]
	sensors_obj=loc+'_'+sensors[0]
	for l in lines:
		print (l)
		if(l.split(':')[0]==sensors_obj):
			ids.append(l.split(':')[1].split('_')[1])
			topics.append(l.split(':')[1].split('_')[0])

	msg['topics']=topics
	msg['ids']=ids
	print(msg)
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
