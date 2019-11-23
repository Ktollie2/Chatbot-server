# Python TCP Client C
import socket 
import sys

host = socket.gethostname() 
port = int(sys.argv[1])
BUFFER_SIZE = 1024
MESSAGE = raw_input("ClientC: Enter message/ 'exit' to exit:") 
 
tcpClientC = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientC.connect((host, port))

while MESSAGE != 'exit':
    tcpClientC.send(MESSAGE)     
    data = tcpClientC.recv(BUFFER_SIZE)
    print " ClientC received data:", data
    MESSAGE = raw_input("ClientC: Enter message to continue/ Enter exit:")

tcpClientC.close() 