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
    return string2

def return_get(string_get):

    #file_name = "files/simplehtml4"
    file_name =[]
    if(string_get == "http://www.facebook.com.br/"):
        file_name = "files/blacklisthttp"
    elif(string_get == "http://www.youtube.com.br/"):
        file_name = "files/blacklisthttp"
    elif(string_get == "http://www.netflix.com.br/"):
        file_name = "files/blacklisthttp"

    return file_name

def  acha_host(data):
    pos = data.find("Host: ")
    pos_end = data.find("\n",pos,len(data))

    host = data[pos+6:pos_end-1]


    return host
    
#DEFININDO O SERVIDOR
HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()


#DEFININDO REQUISIcoES
socket_request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

file_request = open("files/request_byserver","w")
print 'Connected by', addr
''''
data = conn.recv(1024)
HOST2 = acha_host(data)
if HOST2 != []:
    socket_request.connect((HOST2, 80))
    '''
while 1:
    data = conn.recv(1024)
    if not data:
	   print "data:", data,"fim" 
	   break

    #acha link desejado   
    string_get = acha_get(data)
    print "get eh: ",string_get,"a"
    file_return = return_get(string_get)
    print "file: ",file_return
    if file_return !=[]:
        file_tobrowser = open(file_return,"r")
        conn.sendall(str.encode(file_tobrowser.read()))
        file_tobrowser.close()
    else:
        #caso seja uma requisicao valida
        HOST2 = acha_host(data)
        #if HOST2 != []:
        socket_request.connect((HOST2, 80))
        socket_request.sendall(data)
        total_data_rcv = ""
        while 1:
            data_rcv = socket_request.recv(1024)
            if not data_rcv: break
            total_data_rcv = total_data_rcv + data_rcv
        socket_request.close()

        file_resp = open("files/resposta.txt","w")
        file_resp.write(total_data_rcv)
        file_request.write(data)

        conn.sendall(total_data_rcv)


    #file_request.write(data)        #escreve requisicao no no arquivo files/request_byserver
    
conn.close() #como fazer esse codigo sem ser em loop?
s.close()
file_request.close()
file_resp.close()
