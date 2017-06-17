#!/usr/bin/env python
# Echo server program

#ESSE ESTA FUNCIONANDO, APARECE A MENSAGEM, POREM FICA NO KEEP ALIVE, VI QUE TALVEZ UM SHUTDOWN(1) ENVIA BIT DE FIN

import socket
import time

def acha_get(string):
    b = string.find("GET")
    string2 = ""
    for conta_string in range(b+4,len(string)):
        if string[conta_string] == ' ':
            print string2
            break
        string2+=string[conta_string]
    return string2;

def return_get(string_get):

    file_name = "simplehtml4"
    if(string_get == "http://www.facebook.com.br/"):
        file_name = "blacklisthttp"
    elif(string_get == "http://www.youtube.com.br/"):
        file_name = "blacklisthttp"
    elif(string_get == "http://www.netflix.com.br/"):
        file_name = "blacklisthttp"

    return file_name
    

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
#file2 = open("simplehtml3","r")
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data:
	   print "data:", data,"fim" 
	   break
    string_get = acha_get(data)
    print "get eh: ",string_get,"a"
    file_return = return_get(string_get) 
    print "file: ",file_return 
    file2 = open(file_return,"r") 
    #print data
    #print len(data)
    data = data + "la"
    conn.sendall(str.encode(file2.read()))
    #time.sleep(2)
    #conn.shutdown(1)
    
conn.close() #como fazer esse codigo sem ser em loop?
file2.close()
