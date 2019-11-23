import socket
from threading import Thread
from SocketServer import ThreadingMixIn
import sys
from thread import *

class ClientThread(Thread):


    def __init__(local,ip,port): 
        Thread.__init__(local) 
    
        local.ip = ip
        local.port = port
        print("User" + ip + "port:" + str(port) + "has joined the chat")

    def run(local):
        while True:
            info = conn.recv(2048)
            print("server has received:" + info)
            msg = raw_input("Enter response from server:")
            if (msg == 'exit'):
                break
            conn.send(msg)
if len(sys.argv) != 3:
    print("Please insert correct number of arguments")
    exit()
IP = str(sys.argv[1])
PORT = int(sys.argv[2])
Buffer_Sz = 2200

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
Server.bind((IP,PORT)) 
threads = [] 

while True: 
    Server.listen(5)
    if(len(threads) < 1):
         print("Waiting for connections from TCP clients...") 
    (conn, (ip,port)) = Server.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for i in threads: 
    i.join() 
                
            
