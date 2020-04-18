import json
def get_all_server_details():
	f = open('server_details.json',) 
	data = json.load(f) 
	# for i in data:
	# 	print(i)
	print(data)
	for i in data:
		print(data[i])
	
get_all_server_details()