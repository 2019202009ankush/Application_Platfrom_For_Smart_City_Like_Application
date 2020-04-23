import sys
sys.path.insert(0,"../communication_module")

import communication_module
import statistics
display=""

def run(topic,id1,loc):
	global display
	# lis=[]
	
	# for val in communication_module.Sersor_Stream(topic,id):
	# 		lis.append(int(val['data']))
	lis=[]
	mess={}
	print("AC control Algorithm running")
	mess['UserID']=sys.argv[1]
	mess['App_Name']=sys.argv[2]
	mess['Action_type']=sys.argv[3]
	mess['Action']='ON_AC'+loc
	mess['Output']=None
	mess['algorithm']=str('ac_control')
	for val in communication_module.Sersor_Stream(topic,id1):
		lis.append(int(val['data']))
		temp=int(val['data'])
		# print(lis)
		# print(val)
		if temp<=59 and temp>=10:
			mess['Output']=str('LOW_TEMP :'+(str(val['data'])))
		elif temp>=60 and temp<=100:
			mess['Output']=str('NORMAL_TEMP :'+str(val['data']))
		elif temp>=101 and temp<=120:
			mess['Output']=str('HIGH_TEMP :'+str(val['data']))
		display=mess["Output"]
		file=open("display.txt","w+")
		file.write(display)

		# print(mess["Output"])
		communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)
			

#print("UserID",sys.argv[1])##abc@gmail.com
#print("App_Name",sys.argv[2])##
#print("Action_type",sys.argv[3]) ##"Control/Notification"
#print("Output",sys.argv[4])##Output eg temp

# print("Algo Started")
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
