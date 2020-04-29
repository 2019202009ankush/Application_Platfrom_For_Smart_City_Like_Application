#!/usr/bin/env python3

import sys
from twilio.rest import Client 
  
# Your Account Sid and Auth Token from twilio.com / console 
print("@@@@@@@@@Send sms",sys.argv[1],"to ",sys.argv[2])

account_sid = 'AC2d26f36edf92cb63af054fce24390892'
# auth_token = '405def9013bc2fac351053244d0dfbda'
auth_token = '9315e8468a9fcc021c43cf98f7b586b2'

  
client = Client(account_sid, auth_token) 
  
''' Change the value of 'from' with the number  
received from Twilio and the value of 'to' 
with the number in which you want to send message.'''
arg1=sys.argv[1]
arg2=sys.argv[2]
body2="alert recieved"+sys.argv[2]
print(body2)
message = client.messages.create( 
                              from_='+19852314195', 
                              body =body2, 
                              to ='+918839455048'
                          ) 
  
print(message.sid)