import sensor

import threading 
th1 = threading.Thread(target=sensor.sensor,kwargs={'id':'d1','typ':'waterlevel','loc':'OBH','ip':'0.0.0.0','port':'9557'})
th2 = threading.Thread(target=sensor.sensor,kwargs={'id':'d2','typ':'waterlevel','loc':'NBH','ip':'0.0.0.0','port':'9557'})
th3 = threading.Thread(target=sensor.sensor,kwargs={'id':'d10','typ':'waterlevel','loc':'BAKUL','ip':'0.0.0.0','port':'9557'})
th4 = threading.Thread(target=sensor.sensor,kwargs={'id':'d3','typ':'waterlevel','loc':'PARIJAT','ip':'0.0.0.0','port':'9557'})

th1.start()
th2.start()
th3.start()
th4.start()

