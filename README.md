###### RULES 

1. First fork
2. Then before uploading any file make sure your file has proper name
3. Make the pull request
--------------------------------------------------------------------------------------------------------------------------------

# Welcome to the Application_Platfrom_For_Smart_City_Like_Application 

-------------------------------------------------------------------------------------------------------------------------------
###### Rules to run Communication Module
1. Download and setup docker , docker compose
2. Now goto the bootstrap module and run init.py (it is doing docker-compose up for kafka)
3. Goto the communation_module directory and import communication module
4. Call the Sample producer interface
     communication_module.ApplicationManager_to_ServiceLifeCycle_Producer_interface(mess) [ see ApplicationManger.py ]
5. Call the Sample consumer interface
   communication_module.ApplicationManager_to_ServiceLifeCycle_interface(fun) [see ServiceLifeCycle.py ]
6. Videolink: https://www.youtube.com/watch?v=rixFLCBNLao&t=333s
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###### Rules to visulaize any kafka topic
1. cd SensorManger
2. python3 (open python terminal)
3. import UI
4. UI.UI(topic_name)
----------------------------------------------------------------------------------------------------------------------------
#### Important commands

1. docker run --rm --network=host new
2. sudo docker kill $(sudo docker ps -q)

----------------------------------------------------------------------------------------------------------------------------
### Drop all databases

var dbs = db.getMongo().getDBNames()
for(var i in dbs){
    db = db.getMongo().getDB( dbs[i] );
    print( "dropping db " + db.getName() );
    db.dropDatabase();
}

save it to dropall.js and then execute:

mongo dropall.js

--------------------------------------------------------------------------------------------------------------------------
#### IP and Port to see the dashboard of various service
1. All kafka topic data visualization https://localhost:3030



