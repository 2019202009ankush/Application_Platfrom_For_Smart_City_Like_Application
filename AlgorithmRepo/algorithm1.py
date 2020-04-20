import sys
sys.path.insert(0,"../communication_module")

import communication_module
import statistics

def run(topic,id,loc):
	lis=[]
	print(topic,id,loc)
	for val in communication_module.Sersor_Stream(topic,id):
		lis.append(int(val['data']))

		if(len(lis)%120==0):
			x = statistics.mean(lis)
			if x>=35:
				mess={}
				mess['algorithm']=str('algorithm1')
				mess['command']=str('OFF_AC_'+loc)
				communication_module.Algorithm_to_ActionManager_Producer_interface(mess)
			elif x<35 and x>=25:
				mess={}
				mess['algorithm']=str('algorithm1')
				mess['command']=None
				communication_module.Algorithm_to_ActionManager_Producer_interface(mess)
			else:
				mess={}
				mess['algorithm']=str('algorithm1')
				mess['command']=str('ON_AC_'+loc)
				communication_module.Algorithm_to_ActionManager_Producer_interface(mess)

run(sys.argv[1],sys.argv[2],sys.argv[3])		
