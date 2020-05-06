# Requirement denpends on user


import json
with open('config.json') as f:
		meta = json.load(f)

report={}

l=meta['service']['dependency']
for item in l:
	ip=meta['service'][item]['ip']
	port=meta['service'][item]['port']

	#try: ping
	print("[+][Starting ",item,"]"," on ip=",ip," port=",port)

	report[item]={}
	report[item]['ip']=ip
	report[item]['port']=port

	#except: choose form ip pool meta['service']['backup_ip_pool']


with open('report.json', 'w') as json_file:
  json.dump(report, json_file)



# Genereric requirment

import os
import time
#os.system('sudo bash build.sh')
os.system('sudo bash start.sh &')
time.sleep(45)
os.system('sudo bash run.sh')



