import os
def start_service(service_name):
	os.system("python3 "+service_name)

start_service('./service1.py')
print("pid of the process : ")
