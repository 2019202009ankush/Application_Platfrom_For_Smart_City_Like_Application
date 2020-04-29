import socket 
from _thread import *
import threading  
import re
import json
import jsonschema
from jsonschema import validate
from kafka import KafkaProducer
from zipfile import ZipFile
import os
import sys
import shutil
# sys.path.insert(0, "../communication_module")
# import communication_module as cm


configschema = {
    "type": "object",
    "properties": {
        "userid": {"type": "string"},
        "reqid": {"type": "string"},
        "appid": {"type": "string"},
        "algoid": {"type": "string"},
        "action":{"type": "string"},
        "location":{"type": "string"},
        "sensortype":{"type": "string"},
        "old/runningservice":{"type":"string"},
    },
}

filename="name_password.txt"


# def dev_se_data(fd):
#     filenam="./dynamic.txt"
#     with open(filenam) as f1:
#         dy1=f1.readlines()
#         dy1 = [x.rstrip() for x in dy1] 
#     print(dy1)
#     dy=dy1[0]
#     tr=dy
#     tr=eval(tr)
#     print(tr)
    # os.remove("./dynamic.txt")

def handler(func, path, exc_info): 
    print("Inside handler") 
    print(exc_info) 

def main():
    old_stamp=0
    # while(1):
        # if os.path.isfile("./dynamic.txt")==True:
        #     stamp = os.stat("./dynamic.txt").st_mtime
        #     if(stamp != old_stamp):
        #         old_stamp = stamp
        #         start_new_thread(dev_se_data,(filename,))

    if os.path.isdir("./config")==True:
        x=os.listdir("./config")
        x1=x[0]
        print(x1)
        x1="./config/"+x1
        lc="../../Applications/user/app_name/"
        with ZipFile(x1, 'r') as zipObj:
            zipObj.extractall(lc)
        # path = os.path.join("./", "config") 
        # shutil.rmtree(path, onerror = handler)




        
















if __name__ == '__main__': 
    main()






