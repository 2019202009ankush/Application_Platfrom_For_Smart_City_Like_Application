import sys
sys.path.insert(0,"../communication_module")

import communication_module
import statistics

def run(topic,id,loc):
	# lis=[]
	
	# for val in communication_module.Sersor_Stream(topic,id):
	# 		lis.append(int(val['data']))
	lis=[]
	mess={}
	mess['UserID']=sys.argv[1]
	mess['App_Name']=sys.argv[2]
	mess['Action_type']=sys.argv[3]
	mess['Output']=None
	global count_high
	count_high=0

	for val in communication_module.Sersor_Stream(topic,id):
		if int(val['data']) > 200: #For 5 value > 200 F 
			count+=1
			# print(len(lis),val)
			if(count>=5):
					mess['algorithm']=str('algorithm2')
					mess['Action']=str('ON_FIRE_ALRAM_'+loc)
					#print("Sending",mess)
					communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)
		else:
			count-=1
			if(count<5):
					mess['algorithm']=str('algorithm2')
					mess['Action']=str('OFF_FIRE_ALRAM_'+loc)
					#print("Sending",mess)
					communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)

			
			

#print("UserID",sys.argv[1])##abc@gmail.com
#print("App_Name",sys.argv[2])##
#print("Action_type",sys.argv[3]) ##"Control/Notification"
#print("Output",sys.argv[4])##Output eg temp

print("Algo Started")
run(sys.argv[4],sys.argv[5],sys.argv[6])		



'''
demo json{
  "UserID": "upadhyayyash1712@gmail.com",
  "AppName": "Tempreture",
  "Action_type":"Control/Notifictaion"
  "algorithm":"algo1"
  "ServiceName": "findtemp","component":"server","serverID":"ser_01",
  "Action": [{"type1":"email", "type2":"notification"}],  ### in case of Notification
  "Action":"OFF_AC_'+loc" ##in case of Control
  "Output": "29 degree"
  }
  '''
#######Run manually by python3 algorithm1.py  sg@gm.c app1 Control 32
