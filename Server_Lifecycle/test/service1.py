from time import sleep

print("Service 1 is started")
for i in range(10):
	print("Service 1 is running",i)
	sleep(3)
print("Service 1 is ended")
