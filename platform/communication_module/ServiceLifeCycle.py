import communication_module
def event1():
	print('Recived data from Application Manager now taking the necessary action')

fun=event1
communication_module.ApplicationManager_to_ServiceLifeCycle_interface(fun)