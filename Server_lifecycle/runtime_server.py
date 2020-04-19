import sys
sys.path.insert(0, "../communication_module")

import producer_json

import communication_module as cm
import threading 

def handle_service(msg):
	service_id=msg['service_id']
	code=msg['code']
	producer_json.send_message(service_id,code)


while(1):
	cm.DeployManager_to_RuntimeServer_interface(handle_service)