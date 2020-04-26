from time import sleep

print("Service 2 is started")
for i in range(10):
	print("Service 2 is running",i)
	sleep(3)
print("Service 2 is ended")
