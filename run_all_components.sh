trap "exit" INT TERM ERR
trap "kill 0" EXIT

cd monitoring_logging
sudo python3 log_serv.py &
cd ..

cd monitoring_logging
sudo python3 mon_ser.py &
cd ..


cd Service_lifecycle
sudo python3 service_lifecycle.py &
cd ..

echo h

cd Server_lifecycle
sudo python3 server_lifecycle.py &
cd ..



cd Deployment_manager
sudo python3 DeploymentManager.py &
cd ..

cd sensor
sudo python3 sensor_up.py &
cd ..

cd SensorManager
sudo python3 SensorManager.py &
cd ..

cd action_manager
sudo python3 actionserver.py &
cd ..

cd Scheduler_serv
sudo python3 sched.py &
cd ..

wait