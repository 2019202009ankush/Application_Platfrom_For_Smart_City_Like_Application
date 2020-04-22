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
    }
    
 }
with open('meta.json', 'w') as json_file:
  json.dump(meta, json_file)


