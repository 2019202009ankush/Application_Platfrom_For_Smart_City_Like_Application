#!/usr/bin/env python3
import smtplib 
import sys


#print("@@@@@@@@@Send email",sys.argv[1],"to ",sys.argv[2])
mailto=sys.argv[1]

s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("application.platform.smartcity@gmail.com", "smartcity@1234") 
message = sys.argv[2] 

#print("@@@mal to send",message)
s.sendmail("application.platform.smartcity@gmail.com","shanu.gandhi@students.iiit.ac.in", message)
s.quit() 
