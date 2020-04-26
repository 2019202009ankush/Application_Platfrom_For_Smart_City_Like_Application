import json
service={
"service": {
  "Communication_Module":
   {
     "ip": "127.0.0.1",
     "port" : "6010"
     
   },
   "Server_LifeCycle":
   {
     "ip": "127.0.0.1",
     "port" : "9090"
   },
   "Service_LifeCycle" :
   {
     "ip": "127.0.0.1",
     "port" : "9090"
   },
   "Schedular" :
   {
     "ip": "127.0.0.1",
     "port" : "9090"
   },

   "backup_ip_pool" : ['1.2.3.4:3030','10.10.10.10:3030','12.14.13.25:4545','192.168.0.1:3456','44.44.44.44:6060'],

   "dependency" : ['Communication_Module','Server_LifeCycle','Service_LifeCycle','Schedular']
}
}
with open('config.json', 'w') as json_file:
  json.dump(service, json_file)