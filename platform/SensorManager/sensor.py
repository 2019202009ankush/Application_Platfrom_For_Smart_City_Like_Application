from os.path import dirname, realpath
import json
import os
import random
import time
import producer_json
def sensor_run(i,typ,loc,ip,port):
	curpath=str(os.path.dirname(os.path.realpath(__file__)))
	with open(curpath+'/meta.json') as f:
		meta = json.load(f)
	# print(meta[typ])
	rang=meta[typ]['range']
	# frequency=meta[typ]['frequency']
	type_=meta[typ]['type']
	data=None

	if type_ == '4':
		min_max1=meta[typ]['min_max1']
		min_max2=meta[typ]['min_max2']
		min_max3=meta[typ]['min_max3']
		min_max4=meta[typ]['min_max4']
		
		ran=random.randrange(0,100)
		if ran>=min_max1[1] and ran <=min_max1[2]:
			data=random.randrange(min_max1[0][0],min_max1[0][1])
		elif ran>=min_max2[1] and ran <=min_max2[2]:
			data=random.randrange(min_max2[0][0],min_max2[0][1])
		elif ran>=min_max3[1] and ran <=min_max3[2]:
			data=random.randrange(min_max3[0][0],min_max3[0][1])
		elif ran>=min_max4[1] and ran <=min_max4[2]:
			data=random.randrange(min_max4[0][0],min_max4[0][1])

	elif type_=='1':
		# print('here in',type_)
		min_max1=meta[typ]['min_max1']
		ran=random.randrange(0,100)
		# print(ran)
		if ran>=min_max1[1] and ran <=min_max1[2]:
			data=min_max1[0][1]
		else:
			data=min_max1[0][0]


	elif type_=='2':
		# print('here in',type_)
		ran=random.randrange(0,100)

		if ran>=0 and ran<60:
		
				data=''
				data+=str(random.randrange(30,70))
				data+=':'
				data+=str(random.randrange(150,250))
		elif ran>=60 and ran<80:
				data=''
				data+=str(random.randrange(50,100))
				data+=':'
				data+=str(random.randrange(100,150))
		else:
				data=''
				data+=str(random.randrange(30,50))
				data+=':'
				data+=str(random.randrange(80,100))
	
	if typ == 'temperature':
		curpath=str(os.path.dirname(os.path.realpath(__file__)))
		# print("curpath",curpath)
		ppath=dirname(curpath)
		# print("ppath",ppath)
		ppp_path=dirname(ppath)
		f=open(ppp_path+'/Applications/shubham/SmartClass/Emergency Fire Alarm Service/temperature.txt','a+')
		f.write(str(data))
		f.write("\n")
		f.close()

	topic= typ+'_'+i
	# print('#topic=',topic)
	message={}
	message['type']=typ
	message['id']= i
	message['location']=loc
	message['location_type']=None #GPS or room no
	message['range']=rang
	message['data']=data

	producer_json.send_message(topic,message)


def sensor(id,typ,loc,ip,port,start_time=None,end_time=None,itr=None):
	# ff=open('../SensorManager/SensorRegistry.txt','a+')
	# s=loc+'_'+typ

	# meta=typ+'_'+id
	# ff.write(s+':'+meta)
	# ff.write("\n")
	# ff.close()

	if itr is None:
		while 1:
			time.sleep(4)
			sensor_run(id,typ,loc,ip,port)
	else:
		for i in range (itr):
			time.sleep(4)
			sensor_run(id,typ,loc,ip,port)




