#!/usr/bin/env python3
import smtplib 
import sys


print("@@@@@@@@@Send email",sys.argv[1],"to ",sys.argv[2])
mailto=sys.argv[1]
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("upadhyayyash1712@gmail.com", "9074263059") 
message = sys.argv[2] 
s.sendmail("upadhyayyash1712@gmail.com", mailto, message)
s.quit() 
