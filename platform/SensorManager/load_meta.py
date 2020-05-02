import json
meta={
  "temperature":
   {
     "type": "4",
     "range" : "10",
     "min_max1" : [[60,100],0,60],
     "min_max2" : [[10,59],60,80],
     "min_max3" : [[101,120],80,95],
     "min_max4" : [[200,260],95,100]
     
   },
   "camera" :
   {
     "type" : "Image",
     "range" : "50"
   },
   "numeric_attandance":
   {
    "type" : "2",
    "range" : "10",
    "min_max1" : [[0,250]],
    "min_max2" : [[100,500]]
    },
    "doorstep":
    {
      "type" : "1",
      "range" : "10",
      "min_max1" : [[0,1],90,100]
    },
    "heartbeat":
    {
      "type" : "1",
      "range" : "10",
      "min_max1" : [[1,0],90,100]
    },
    "waterlevel":
    {
      "type" : "1",
      "range" : "10",
      "min_max1" : [[0,1],90,100]
    },
    "gas":
    {
      "type": "4",
     "range" : "10",
     "min_max1" : [[3,6],0,60], #60% Avg 3 - 6
     "min_max2" : [[1,2],60,80], #20% good 1 - 2
     "min_max3" : [[7,8],80,95], #15% Not good 7-8
     "min_max4" : [[9,10],95,100] #5% Very bad 9-10
    }
    
 }
with open('meta.json', 'w') as json_file:
  json.dump(meta, json_file)


