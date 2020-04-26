trap "exit" INT TERM ERR
trap "kill 0" EXIT

cd Monitoring_Logging
sudo python3 log_serv.py &
cd ..

cd Monitoring_Logging
sudo python3 mon_ser.py &
cd ..


cd Service_Lifecycle
sudo python3 service_lifecycle.py &
cd ..

echo h

cd Server_Lifecycle
sudo python3 server_lifecycle.py &
cd ..


cd Deployment_Manager
sudo python3 DeploymentManager.py &
cd ..


cd SensorManager
sudo python3 SensorManager.py &
cd ..

cd Action_Manager
sudo python3 actionserver.py &
cd ..

cd Scheduler
sudo python3 sched.py &
cd ..

wait
