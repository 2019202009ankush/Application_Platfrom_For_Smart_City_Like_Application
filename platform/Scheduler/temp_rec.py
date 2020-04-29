import sys
import json
# import datetime

# import time
# import collections 
topic_own="pandey"

sys.path.insert(0, "../communication_module")

import communication_module as cm

f= open('meta.json',) 
data = json.load(f) 

meta_data={}
for i in data['scheduler']:
     meta_data.update(i)
data=meta_data
print(data)
    # producer.send(topic,value=data)       
    # sleep(1)

cm.ApplicationManager_to_Scheduler_Producer_interface(data)
