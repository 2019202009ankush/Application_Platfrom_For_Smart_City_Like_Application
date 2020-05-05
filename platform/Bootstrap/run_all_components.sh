trap "exit" INT TERM ERR
trap "kill 0" EXIT

# cd Monitoring_Logging
sudo python3 platform/Monitoring_Logging/log_serv.py &
# cd ..

# cd Monitoring_Logging
sudo python3 platform/Monitoring_Logging/mon_ser.py &
# cd ..


# cd Service_Lifecycle
sudo python3 platform/Service_Lifecycle/service_lifecycle.py &
# cd ..


# cd Server_Lifecycle
sudo python3 platform/Server_Lifecycle/server_lifecycle.py &
# cd ..


# cd Deployment_Manager
sudo python3 platform/Deployment_Manager/DeploymentManager.py &
# cd ..


# cd SensorManager
sudo python3 platform/SensorManager/SensorManager.py &
# cd ..

# cd Action_Manager
sudo python3 platform/Action_Manager/actionserver.py &
# cd ..

# cd Scheduler
sudo python3 platform/Scheduler/sched.py &
# cd ..

wait
