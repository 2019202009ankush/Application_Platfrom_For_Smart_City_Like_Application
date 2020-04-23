import sensor
sensor.sensor('temp1','temperature','obh_112','0.0.0.0','9557')
import thread
th1 = threading.Thread(target=sensor.sensor,kwargs={'d1':id,'temperature':typ,'obh_112':loc,'0.0.0.0':ip,'9557':port})
th2 = threading.Thread(target=sensor.sensor,kwargs={'d2':id,'temperature':typ,'obh_113':loc,'0.0.0.0':ip,'9557':port})
th3 = threading.Thread(target=sensor.sensor,kwargs={'d3':id,'temperature':typ,'obh_114':loc,'0.0.0.0':ip,'9557':port})
th4 = threading.Thread(target=sensor.sensor,kwargs={'d4':id,'temperature':typ,'obh_115':loc,'0.0.0.0':ip,'9557':port})
th5 = threading.Thread(target=sensor.sensor,kwargs={'d5':id,'temperature':typ,'obh_116':loc,'0.0.0.0':ip,'9557':port})
th6 = threading.Thread(target=sensor.sensor,kwargs={'d6':id,'temperature':typ,'obh_117':loc,'0.0.0.0':ip,'9557':port})
th7 = threading.Thread(target=sensor.sensor,kwargs={'d7':id,'temperature':typ,'obh_118':loc,'0.0.0.0':ip,'9557':port})
th8 = threading.Thread(target=sensor.sensor,kwargs={'d8':id,'temperature':typ,'obh_119':loc,'0.0.0.0':ip,'9557':port})
th9 = threading.Thread(target=sensor.sensor,kwargs={'d9':id,'temperature':typ,'obh_111':loc,'0.0.0.0':ip,'9557':port})
th10 = threading.Thread(target=sensor.sensor,kwargs={'d10':id,'temperature':typ,'obh_110':loc,'0.0.0.0':ip,'9557':port})
# sensor.sensor('d1','numeric_attandance','obh_112','0.0.0.0','9557')
th1.start
th2.start
th3.start
th4.start
th5.start
th6.start
th7.start
th8.start
th9.start
th10.start