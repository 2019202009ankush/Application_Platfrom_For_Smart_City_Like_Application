from datetime import datetime
from time import sleep


now3=datetime.strptime("2020-04-08 14:03:48.706342","%Y-%m-%d %H:%M:%S.%f")
print(now3)
# now1 = datetime.now()
# sleep(5)
now2 = datetime.now()
# print(now1)
print(now2)
d=(now2-now3).total_seconds()
print('diffference : ',now2-now3,d,type(d))
# print(now2.total_seconds())
import time
seconds = time.time()
sleep(3)
seconds2 = time.time()
print("Seconds since epoch =", seconds-seconds2)	