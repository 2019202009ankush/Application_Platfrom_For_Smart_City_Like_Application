import sys
sys.path.insert(0,"platform/communication_module")

import communication_module
import statistics
import os


def run(loc,topic,id):
	print("Water level Algo Started",topic,id)
	curpath=str(os.path.dirname(os.path.realpath(__file__)))
	cmd="python3 '"+curpath+"/dashboard.py' &"
	os.system(cmd)

	mess={}
	mess['UserId']=sys.argv[1]
	mess['AppName']=sys.argv[2]
	mess['ServiceName']=sys.argv[3]

	for val in communication_module.Sersor_Stream(topic,id):
		# print(int(val['data']))
		if(int(val['data'])==1):
			mess["ActionType"]="Notification"
			mess["Action"]=["email"]
			status = "Overflow "
			mess["Output"]=str("Water Level Status at "+loc+" is "+status+" kindly take neccessary action")

			print("Action Initiated : - ",mess)

			f=open(curpath+"/display.txt",'w')
			f.write(mess["Output"])
			f.close()
			
			communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)

		elif(int(val['data'])==0):
			mess["ActionType"]="Control"
			mess["Action"]=["email"]
			status = "Normal "
			mess["Output"]=str("Water Level Status at "+loc+" is "+status+" kindly take neccessary action")

			print("Action Initiated : - ",mess)
			f=open(curpath+"/display.txt",'w')
			f.write(mess["Output"])
			f.close()
			communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)

		elif(int(val['data'])==2):
			mess["ActionType"]="Notification"
			mess["Action"]=["email"]
			status = " Quite Low "
			mess["Output"]=str("Water Level Status at "+loc+" is "+status+" kindly take neccessary action")

			print("Action Initiated : - ",mess)
			f=open(curpath+"/display.txt",'w')
			f.write(mess["Output"])
			f.close()
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