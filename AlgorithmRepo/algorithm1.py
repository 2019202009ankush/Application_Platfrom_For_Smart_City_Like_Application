import sys
sys.path.insert(0,"../communication_module")

import communication_module
import statistics

def run(topic,id,loc):
	lis=[]
	print(topic,id,loc)
	for val in communication_module.Sersor_Stream(topic,id):
		lis.append(int(val['data']))
    lis=[]
    mess={}
    mess['UserID']=sys.argv[1]
    mess['App_Name']=sys.argv[2]
    mess['Action_type']=sys.argv[3]
    mess['Output']=None
    for val in communication_module.Sersor_Stream(topic,id):
        lis.append(int(val['data']))
        if(len(lis)%120==0):
            x = statistics.mean(lis)
            if x>=35:
                mess['algorithm']=str('algorithm1')
                mess['Action']=str('OFF_AC_'+loc)
                communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)
            elif x<35 and x>=25:
                mess['algorithm']=str('algorithm1')
                mess['Action']=None
                communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)
            else:
                mess['algorithm']=str('algorithm1')
                mess['Action']=str('ON_AC_'+loc)
                communication_module.RuntimeServer_to_ActionServer_Producer_interface(mess)

print("UserID",sys.argv[1])##abc@gmail.com
print("App_Name",sys.argv[2])##
print("Action type",sys.argv[3]) ##"Control/Notification"
print("Output",sys.argv[4])##Output eg temp


run(sys.argv[1],sys.argv[2],sys.argv[3])		


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
