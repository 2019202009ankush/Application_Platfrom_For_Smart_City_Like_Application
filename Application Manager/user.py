import socket 
import subprocess
import sys
def Main():  
	host = '127.0.0.1'
	print("Enter Server port no:")
	port = int(input())
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	s.connect((host,port)) 
	print("1.NEW USER/ 2.EXISTING USER:")
	one2=int(input())
	print("Enter user_name")
	user_name=input()
	print("Enter password")
	password=input()

	# print("dss",one2)
	s.send(bytes(str(one2), 'utf8'))
	s.recv(10)
	s.send(bytes(str(user_name), 'utf8'))
	s.recv(10)
	s.send(bytes(str(password), 'utf8'))

	valid=str(s.recv(40).decode('utf-8'))
	valid=int(valid)
	s.send(b'hell')
	if(valid==1):
		wel=str(s.recv(40).decode('utf-8'))
		s.send(b'hell')
		link=str(s.recv(400).decode('utf-8'))
		print(wel)
		print("click on link to open:")
		print(link)
		# opens link
		# subprocess.call(['gnome-terminal', '-x', 'python3 app.py'])
		print("Type filled if sent config.json")
		x=input()
		if(x=="filled"):
			s.send(bytes(str("filled"), 'utf8'))








	else:
		wel=str(s.recv(40).decode('utf-8'))
		s.send(b'hell')
		we1=str(s.recv(40).decode('utf-8'))
		print(we1)

	



	s.close() 

if __name__ == '__main__': 
	Main() 

