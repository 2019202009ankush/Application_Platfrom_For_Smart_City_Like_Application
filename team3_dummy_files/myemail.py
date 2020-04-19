#!/usr/bin/env python3
import smtplib 
import sys

mailto=sys.argv[1]
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("upadhyayyash1712@gmail.com", "9074263059") 
message = "HI Yash" 
s.sendmail("upadhyayyash1712@gmail.com", mailto, message)
s.quit() 
