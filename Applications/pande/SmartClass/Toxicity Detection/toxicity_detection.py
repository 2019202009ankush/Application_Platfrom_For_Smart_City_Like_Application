import sys
sys.path.insert(0,"platform/communication_module")

import communication_module
import statistics
import os

display=""
import os

def run(loc,topic,id):
	global display
	print("Toxic level detection algorithm is running")
	curpath=str(os.path.dirname(os.path.realpath(__file__)))
	cmd="python3 '"+curpath+"/dashboard.py' &"
	os.system(cmd)

	mess={}
	mess['UserId']=sys.argv[1]
	mess['AppName']=sys.argv[2]
	mess['ServiceName']=sys.argv[3]
	curpath=str(os.path.dirname(os.path.realpath(__file__)))



	for val in communication_module.Sersor_Stream(topic,id):

		scale=int(val['data'])


		if scale>=3 and scale<=6:
			mess["ActionType"]="Control"
			mess["Output"]=str("Toxic content in air is moderate at "+str(loc)+" and scale value is"+str(scale))
			f=open(curpath+"/display.txt",'w')
			f.write(mess["Output"])
			f.close()


		elif scale>=1 and scale<=2:
			mess["ActionType"]="Control"
			mess["Output"]=str("Toxic content in air is very low at "+str(loc)+" and scale value is"+str(scale))
			f=open(curpath+"/display.txt",'w')
			f.write(mess["Output"])
			f.close()


		elif scale>=7 and scale<=8:
			mess["ActionType"]="Notification"
			mess["Action"]=["email"]
			mess["Output"]=str("Toxic content in air is high "+str(loc)+" and scale value is"+str(scale))	
			f=open(curpath+"/display.txt",'w')
			f.write(mess["Output"])
			f.close()


		elif scale>=9:
			mess["ActionType"]="Notification"
			mess["Action"]=["email"]
			mess["Output"]=str("Toxic content in air is very high "+str(loc)+" and scale value is"+str(scale))			
			f=open(curpath+"/display.txt",'w')
			f.write(mess["Output"])
			f.close()



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
