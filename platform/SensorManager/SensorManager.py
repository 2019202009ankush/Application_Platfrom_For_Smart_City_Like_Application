import sys
import sensor
sys.path.insert(0, "platform/communication_module")
import threading
import communication_module
import os

def event1(msg):
	# print("pwdddd!!!!!!!!!",os.system(pwd))
	# print("mgdddd",msg)
	loc=msg['location']
	sensors=msg['algoid']['sensors']
	
	#print(loc)
	#print(sensors)
	curpath=str(os.path.dirname(os.path.realpath(__file__)))  
	
	import json 
	with open(curpath+'/SensorRegistry.txt') as f:
			lines = f.read().splitlines()
	ids=[]
	topics=[]
	# print("lines!!!!!",lines)
	if loc != 'all':
		# print("Not all!!!!!!!!!!!!!!")
		sensors_obj=loc+'_'+sensors[0]
		for l in lines:
			if(l.split(':')[0]==sensors_obj):
				ids.append(l.split(':')[1].split('_')[1])
				topics.append(l.split(':')[1].split('_')[0])
	else:
		sensors_obj=sensors[0]
		# print("All!!!!!!!!!!!!!!")
		print("sensobj",sensors_obj)
		for l in lines:
			# print("!!@@llll",l.split(':')[0].split('_')[2])
			try:
				if(sensors_obj.startswith(l.split(':')[0].split('_')[2])):
					if sensors_obj.startswith("numeric"):
						ids.append(l.split(':')[1].split('_')[2])
						topics.append(l.split(':')[1].split('_')[0]+"_"+l.split(':')[1].split('_')[1])
					else:
						ids.append(l.split(':')[1].split('_')[1])
						topics.append(l.split(':')[1].split('_')[0])
			except:
				pass
	msg['topics']=topics
	msg['ids']=ids
	#print("Sensor Manager",msg)
	# print("iiii",ids)
	# print("tttt",topics)
	
	for i in range(len(topics)):
		th1 = threading.Thread(target=sensor.sensor,kwargs={'id':ids[i],'typ':topics[i],'loc':loc,'ip':'0.0.0.0','port':'9557'})
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


print("\n[Sensor Manager] : started\n")
fun=event1
communication_module.DeployManager_to_SensorManager_interface(fun)
