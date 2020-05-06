from time import sleep
from json import dumps
import json
import threading

import sys
sys.path.insert(0, "platform/communication_module")

import communication_module as cm


def handle_servicelc_msg(msg):

	# print("Service Recieved to deploy:-\n")

	request_sensor(msg)


		


def generate_dockerfile(msg):
	f=open('Services/'+str(msg['reqid'])+'.dockerfile',"w")
	f.write("FROM python:3.7-alpine\n")
	f.write("COPY . /src\n")
	f.write("WORKDIR /src/\n")
	f.write(" CMD ['"' pyhton3 '"'," +'"'+  msg["algoid"]["path"]  +'"'+","+'"'+msg["algoid"]["sensor"][1]["topic"] +'"'+"]")

def send_to_server(data):
	cmd=""
	#cmd=cmd+'"'+str(data['algoid']['path'])+'"'+" "
	cmd=cmd+'"'+'/Applications/'+str(data['DevName'])+'/'+str(data['algoid']['path'])+'"'+" "
	cmd=cmd+" "+str(data['UserId'])+" "+'"'+str(data['AppName'])+'"'+" "+'"'+str(data['algoid']['ServiceName'])+'"'+" "+'"'+str(data['location'])+'"'+" "
	cmd=cmd+str(len(data['topics']))+" "
	for i in range(len(data['topics'])):
		cmd=cmd+str(data['topics'][i])+" "+str(data['ids'][i])+" "

	# mess={}
	data['service_id']=str(data['server_id'])
	data['code']=str(cmd)
	cm.DeployManager_to_RuntimeServer_Producer_interface(data)
	print("\n[Deployment-Manager] - ",data['algoid']['ServiceName']," deployed")


def request_sensor(data):

	# print("\nSending to Sensor mgr :-\n")
	cm.DeployManager_to_SensorManager_Producer_interface(data)
		


def handle_sensor_mgr_msg(msg):
	# print("Recived Sensor details")
	# generate_dockerfile(msg)
	send_to_server(msg)

def msg_recieved_sensor_mgr():
	return sensor_id_returned


#print("-------- Deployment Manager ---------------")
print("\n[Deployment-Manager] - started\n")
th=threading.Thread(target=cm.ServiceLifeCycle_to_DeployManager_interface,kwargs={'func_name':handle_servicelc_msg})
th.start()


th=threading.Thread(target=cm.SensorManager_to_DeployManager_interface,kwargs={'func_name':handle_sensor_mgr_msg})
th.start()
# cm.ServiceLifeCycle_to_DeployManager_interface(handle_servicelc_msg)
