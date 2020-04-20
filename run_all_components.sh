trap "exit" INT TERM ERR
trap "kill 0" EXIT

cd Scheduler_serv
sudo python3 sched.py &
cd ..

cd Service_lifecycle
sudo python3 service_lifecycle.py &
cd ..

echo h

cd Server_lifecycle
sudo python3 server_lifecycle.py &
cd ..

cd Server_lifecycle
sudo python3 runtime_server.py &
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

cd team3_dummy_files
sudo python3 actionserver.py &
cd ..

wait

