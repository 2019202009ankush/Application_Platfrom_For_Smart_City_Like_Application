import sys
import sensor
sys.path.insert(0,"../communication_module")
import threading
import communication_module

def event1(msg):
	print('The command is ',msg['command'])

fun=event1
communication_module.Temperature_interface(fun)