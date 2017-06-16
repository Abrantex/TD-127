#!/usr/bin/env python
# Echo server program

#ESSE ESTÁ FUNCIONANDO, APARECE A MENSAGEM, PORÉM FICA NO KEEP ALIVE, VI QUE TALVEZ UM SHUTDOWN(1) ENVIA BIT DE FIN

import socket
import time
import os

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
file2 = open("simplehtml4","r")
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data:
	print "data:", data,"fim" 
	break
    print data
    print len(data)
    data = data + "la"
    conn.sendall(str.encode(file2.read()))
    #data = conn.recv(1024)
    #time.sleep(2)
    #conn.shutdown(socket.SHUT_RD)
    
conn.close() #como fazer esse codigo sem ser em loop?
file2.close()
