from os.path import dirname, realpath
from kafka import KafkaConsumer
import psutil
import os
import time
import sys
import json
import threading
from time import sleep

algorihtm_details={}


def get_algo_details(msg):
	global algorihtm_details
	curpath=str(os.path.dirname(os.path.realpath(__file__)))
	f= open('Applications/'+msg['DevName']+'/'+msg['AppName']+'/algorithm_metadata.json',) 
	algorihtm_details = json.load(f) 


def bind_algo(msg):
	get_algo_details(msg)
	print("\nBinding to algorithm and sensors",algorihtm_details[msg["algoid"]]['sensors'])
	msg["algoid"]=algorihtm_details[msg["algoid"]]
	return msg

# bind_algo()
