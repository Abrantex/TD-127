
#!


### ******************************#### 
'''
                                    SERVER COM ARRAY DE GET PARA TENTAR ELIMINAR PROBLEMAS COM MULT GETS


'''
import socket
import thread


import time

global conta_thread

def set_get_array():
    global get_array
    get_array =[]

def existe_get(name):
    for i in range(len(get_array)):
        if name == get_array[i]:
            return 1
    return 0


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

def acha_httpflag(string):

    #inicio_get = string.find("HTTP")
    inicio_get = string.find(" ")
    fim_get = string.find(" ",inicio_get+1,len(string))

    code_r = string[inicio_get+1:fim_get]

    return code_r

def escreve_log(file,addrs,get,resposta):
    file.write(str(addrs))
    file.write(" ")
    file.write(get)

    code_r = acha_httpflag(resposta)

    escreve = "\t"+code_r+"\t\t"+str(len(resposta)) + "\n"

    #file_log.write("\t",)
    #file_log.write(str(len(resposta)))
    #file_log.write("\n")
    file.write(escreve)


def conectado(con, cliente):
    print 'Conectado por', cliente
    
    while 1:
        #socket_request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        file_request = open("files/request_byserver","w")
        file_log = open("files/log","a")

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
            dado_envia = file_tobrowser.read()
            #conn.sendall(str.encode(file_tobrowser.read()))
            #conn.sendall(str.encode("<html>\n<body>\n\n<h1>Site Nao Altorizado pelo proxy</h1>\n<p>Favor, use outro site</p>\n\n</body>\n</html>"))
            file_tobrowser.close()

            escreve_log(file_log,cliente,string_get,dado_envia)
            conn.sendall(str.encode(dado_envia))
            file_log.close()
            #break


        #elif para teste
        #elif (string_get=="http://netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css") + (string_get == "http://wiki.ros.org/"):
        elif  (existe_get(string_get)==0) + (string_get != "NECT"):
            get_array.append(string_get)
            #caso seja uma requisicao valida
            HOST2 = acha_host(data)
            #if HOST2 != []:
            #socket_request.connect((HOST2, 80))
            socket_request = socket.create_connection((HOST2,80),100)
            socket_request.sendall(data)
            total_data_rcv = ""
            while 1:
                data_rcv = socket_request.recv(1024)
                if not data_rcv: break
                total_data_rcv = total_data_rcv + data_rcv
            #socket_request.close()

            file_resp = open("files/resposta.txt","w")
            file_resp.write(total_data_rcv)
            file_request.write(data)


            escreve_log(file_log,cliente,string_get,total_data_rcv)
            conn.sendall(total_data_rcv)
            file_log.close()
            #conn.shutdown(0)
            
            #break
        else:
            break

    print 'Finalizando conexao do cliente', cliente
    #get_array.remove(string_get)
    conn.close()
    #conta_thread = conta_thread-1
    thread.exit()









### **************************************####
#### PROGRAMAAAAAAAAAA#####

# *****************************************##
set_get_array()

HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 50007            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

file_log = open("files/log","a")


conta_thread =  0
while True:
    conn, cliente = s.accept()
    ##if (conta_thread <2):
        ##print "thread"
        ##conta_thread = conta_thread +1
    thread.start_new_thread(conectado, tuple([conn, cliente]))
        #conta_thread = conta_thread -1


s.close()
