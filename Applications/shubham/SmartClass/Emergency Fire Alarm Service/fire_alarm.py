import sys
sys.path.insert(0,"platform/communication_module")

import communication_module
import statistics
import os
# os.system("python3 dashboard.py &")
# print('hi')

def run(loc,topic,id):
	curpath=str(os.path.dirname(os.path.realpath(__file__)))
	cmd="python3 '"+curpath+"/dashboard.py' &"
	os.system(cmd)
	lis=[]
	mess={}
	mess['UserId']=sys.argv[1]
	mess['AppName']=sys.argv[2]
	mess['ServiceName']=sys.argv[3]

	global count
	count=0
	print(topic,id)
	for val in communication_module.Sersor_Stream(topic,id):
		if int(val['data'])+150 > 200: #For 5 value > 200 F 
			count+=1
			# print(len(lis),val)
			if(count>=5):
				
				mess["ActionType"]="Control"
				mess["Output"]=str('ON_FIRE_ALRAM_'+loc)
				#print("Sending",mess)
				communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)
		else:
			# count-=1
			if(count<5):
				mess["ActionType"]="Control"
				mess["Output"]=str('OFF_FIRE_ALRAM_'+loc)
				#print("Sending",mess)
				communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)

			
			

# #print("UserID",sys.argv[1])##abc@gmail.com
# #print("App_Name",sys.argv[2])##
# #print("Action_type",sys.argv[3]) ##"Control/Notification"
# #print("Output",sys.argv[4])##Output eg temp

print("Algo Started")
run(sys.argv[4],sys.argv[6],sys.argv[7])		



'''
demo json{
  "UserId": "upadhyayyash1712@gmail.com",
  "AppName": "Tempreture",
  "ActionType":"Control/Notifictaion"
  "algorithm":"algo1"
  "ServiceName": "findtemp","component":"server","serverID":"ser_01",
  "Action": [{"type1":"email", "type2":"notification"}],  ### in case of Notification
  "Action":"OFF_AC_'+loc" ##in case of Control
  "Output": "29 degree"
  }
  '''
#######Run manually by python3 illegal_access_detect.py  user@gmail.com SmartClass IAD obh_112 1 temperature d1
