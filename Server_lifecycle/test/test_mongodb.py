from pymongo import MongoClient 
import json
  
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn['server_life_cycle']
col=db['server_details']

f = open('server_details.json') 
data = json.load(f) 
print(data)
#
for k,v in data.items():
	print(k)
	col.insert_one(v)

for c in col.find():
	print(c)

t='45|4|2020-04-07 21:48:14.988608'
ll=t.split("|")
print(ll)
d={'s1':'45|4|2020-04-07 21:48:14.988608','s2':'45|4|2020-04-07 21:48:14.988608','s3':'45|4|2020-04-07 21:48:14.988608'}

tt={}
for k,v in d.items():
	tt[k]={}
	ll=v.split("|")
	tt[k]["id"]=k
	tt[k]["cpu"]=ll[0]
	tt[k]["ram"]=ll[1]
	tt[k]["time"]=ll[2]
print(tt)


t='54|3|2021-04-07 21:48:14.9823608'
ll=t.split("|")
print(ll)

result = col.update_one( 
        {"id":"s1"}, 
        	{ 
                "$set":{ 
                        "cpu":ll[0],
                        "ram":ll[1],
                        "time":ll[2]
                       }
                  
            } 
        ) 

for c in col.find():
	print(c)





#col.insert_many(list(data))

# print(db)
  
# # Created or Switched to collection names: my_gfg_collection 
# collection = db['server_details']
  
# emp_rec1 = { 
#         "name":"Mr.Geek", 
#         "eid":24, 
#         "location":"delhi"
#         } 
# emp_rec2 = { 
#         "name":"Mr.Shaurya", 
#         "eid":14, 
#         "location":"delhi"
#         } 
  
# # Insert Data 
# rec_id1 = collection.insert_one(emp_rec1) 
# rec_id2 = collection.insert_one(emp_rec2) 
  
# print("Data inserted with record ids",rec_id1," ",rec_id2) 
  
# # Printing the data inserted 
# cursor = collection.find() 
# for record in cursor: 
#     print(record) 