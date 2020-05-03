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


def get_algo_details():
	global algorihtm_details
	curpath=str(os.path.dirname(os.path.realpath(__file__)))
	curpath=str(os.path.dirname(os.path.realpath(__file__)))
	# print("curpath",curpath)
	ppath=dirname(curpath)
	# print("ppath",ppath)
	ppp_path=dirname(ppath)
	# print("ppp_ath",ppp_path)
	
	f= open(ppp_path+'/Applications/pande/SmartClass/algorithm_metadata.json',) 
	algorihtm_details = json.load(f) 


def bind_algo(msg):

	get_algo_details()
	print("\nBinding to algo",algorihtm_details[msg["algoid"]])
	msg["algoid"]=algorihtm_details[msg["algoid"]]
	return msg

# bind_algo()
