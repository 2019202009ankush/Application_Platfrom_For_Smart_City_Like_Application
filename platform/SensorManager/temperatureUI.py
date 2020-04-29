import sys
import sensor
sys.path.insert(0,"../communication_module")
import threading
import communication_module
import producer_json
mess={}
print('Enter the command')
com=input()
mess['command']=com
# print(mess)
producer_json.send_message('Temperature',mess)