import communication_module
def event1(msg):
    loc=msg['location']
    sensors=msg['sensors']
    import json	
    with open('SensorRegistry.json') as f:
 		meta = json.load(f)
    ids=[]
    topics=[]
    for  topic in sensors:
        ids.append(meta[str(loc+':'+topic)]
    mess={}
    mess['topics']=topic
    mess['ids']=ids
    communication_module.SensorManager_to_DeployManager_Producer_interface(mess)
	# Input format
    # {
    #   "location":"obh_112",
    #   "sensors": ["temparature","humidity"]
    # }
    # Output format
    # { 
    #   "topics" : ["temparature","humidity"],
    #   "ids"    : ["temp1","hum12"]
    # }

fun=event1
communication_module.DeployManager_to_SensorManager_interface(fun)