import json
meta={
  "temperature":
   {
     "type": "real",
     "range" : "10",
     "min" : "20",
     "max" : "40"
     
   },
   "camera" :
   {
     "type" : "Image",
     "range" : "50"
   }
}
with open('meta.json', 'w') as json_file:
  json.dump(meta, json_file)


