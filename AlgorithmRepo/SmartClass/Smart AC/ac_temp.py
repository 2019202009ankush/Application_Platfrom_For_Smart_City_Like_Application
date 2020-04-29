import sys
sys.path.insert(0,"../communication_module")

import communication_module
import statistics
display=""
import os

def run(loc,topic,id):
	print("AC control Algorithm running")
	global display

	mess={}
	mess['UserId']=sys.argv[1]
	mess['AppName']=sys.argv[2]
	mess['ServiceName']=sys.argv[3]

	for val in communication_module.Sersor_Stream(topic,id):

		temp=int(val['data'])

		if temp<=59 and temp>=10:
			mess["ActionType"]="Conrol"
			mess["Action"]=str('LOW_TEMP :'+(str(val['data'])))			

		elif temp>=60 and temp<=100:
			mess["ActionType"]="Conrol"
			mess["Action"]=str('NORMAL_TEMP :'+str(val['data']))

		elif temp>=101 and temp<=120:
			mess["ActionType"]="Conrol"
			mess["Action"]=str('HIGH_TEMP :'+str(val['data']))			


		display=mess["Action"]
		curpath=str(os.path.dirname(os.path.realpath(__file__)))
		file=open(curpath+"/display.txt","w+")
		file.write(display)

		# print(mess["Action"])
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



#######Run manually by python3 ac_temp.py  user@gmail.com SmartClass SAC obh_112 1 temperature d1
