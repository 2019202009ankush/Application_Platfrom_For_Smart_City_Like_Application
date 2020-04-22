import sys
sys.path.insert(0,"../communication_module")

import communication_module

def run(topic,id,loc):
	print("Algo Started",topic,id)
	mess={}
	mess['UserID']=sys.argv[1]
	mess['App_Name']=sys.argv[2]
	mess['Action_type']=sys.argv[3]
	mess['Output']=None

	for val in communication_module.Sersor_Stream(topic,id):
		#print(val)
		if(int(val['data'])==1):
			mess['algorithm']=str('Illegal Access Detection')
			mess["Action"]=str("Illegal Access Detection at "+loc)
			print("Sending",mess)
			communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)

			

#print("UserID",sys.argv[1])##abc@gmail.com
#print("App_Name",sys.argv[2])##
#print("Action_type",sys.argv[3]) ##"Control/Notification"
#print("Output",sys.argv[4])##Output eg temp


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
