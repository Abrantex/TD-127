#!/usr/bin/env python
import socket

HOST = "wiki.ros.org"    # The remote host
PORT = 80             # The same port as used by the server
#HOST =''
#PORT = 50006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
file = open("files/request","r")
file2 = open("files/resposta.txt","w")

data_send = file.read()
data_send = data_send + "GET http://wiki.ros.org/ HTTP/1.1 "
s.sendall(data_send)
while 1:
	data = s.recv(1024)
	if not data: break
	file2.write(data)


s.close()

file.close()
file2.close()
