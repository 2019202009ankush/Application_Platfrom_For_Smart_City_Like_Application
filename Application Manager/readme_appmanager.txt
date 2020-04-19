 README FOR APP MANANGER:
 
 1.App manager connects with scheduler and Service lifecycle module via KAFKA so zookeeper should be active and kafka server should be active.
 
 2.user sends credentials, it get verified by user_password repo and if corrects then proceeds.
 
 3.user.py is user/app developer that sends config.zip file to app manager.
 
 4.am.py is app manager, it sends html page link to valid user after schema verification and ask user to upload config.zip on HTML page.
 
 5. HTML page is back ended by python flask that stores it in app manager database.
 
 6. flask uses app.py for flask and templates folder having HTML pages.
 
 7. scheduler.py and service_lifecycle.py for receiving data via kafka consumer.
 
 
