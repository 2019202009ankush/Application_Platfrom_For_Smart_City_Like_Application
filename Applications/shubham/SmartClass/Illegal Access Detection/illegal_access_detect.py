import sys
sys.path.insert(0,"platform/communication_module")

import communication_module

def run(loc,topic,id):
	print("Algo Started",topic,id)
	mess={}
	mess['UserId']=sys.argv[1]
	mess['AppName']=sys.argv[2]
	mess['ServiceName']=sys.argv[3]

	for val in communication_module.Sersor_Stream(topic,id):
		# print(int(val['data']))
		if(int(val['data'])==1):
			mess["ActionType"]="Notification"
			mess["Action"]=["email"]
			mess["Output"]=str("Illegal Access Detection at "+loc)

			print("Action Initiated : - ",mess)
			communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)

			

#print("UserID",sys.argv[1])##abc@gmail.com
#print("App_Name",sys.argv[2])##
#print("Action_type",sys.argv[3]) ##"Control/Notification"
#print("Output",sys.argv[4])##Output eg temp


run(sys.argv[4],sys.argv[6],sys.argv[7])		



'''
demo json{
  "UserId": "upadhyayyash1712@gmail.com",
  "AppName": "Tempreture",
  "ActionType":"Control/Notifictaion"
  "ServiceName": "findtemp","component":"server","serverID":"ser_01",
  "Action": [{"type1":"email", "type2":"notification"}],  ### in case of Notification
  "Action":"OFF_AC_'+loc" ##in case of Control
  "Output": "29 degree"
  }
  '''



#######Run manually by python3 illegal_access_detect.py  user@gmail.com SmartClass IAD obh_112 1 temperature d1
