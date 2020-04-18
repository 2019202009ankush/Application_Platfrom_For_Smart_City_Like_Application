import json
topic={
  "topic":[
    "ApplicationManager_to_ServiceLifeCycle",
    "ApplicationManager_to_Scheduler",
    "ServiceLifeCycle_to_DeployManager",
    "DeploymentManager_to_SensorManager",
    "DeploymentManager_to_RuntimeServer",
    "RuntimeServer_to_ActionServer",
    "Sensor_Stream"
  ]
}
with open('topic.json', 'w') as json_file:
  json.dump(topic, json_file)