#!/usr/bin/env python3

import sys
from twilio.rest import Client 
  
# Your Account Sid and Auth Token from twilio.com / console 
account_sid = 'AC2d26f36edf92cb63af054fce24390892'
auth_token = '405def9013bc2fac351053244d0dfbda'
  
client = Client(account_sid, auth_token) 
  
''' Change the value of 'from' with the number  
received from Twilio and the value of 'to' 
with the number in which you want to send message.'''
body2="alert recieved"
print(body2)
message = client.messages.create( 
                              from_='+19852314195', 
                              body =body2, 
                              to ='+918839455048'
                          ) 
  
print(message.sid)