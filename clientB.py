# Python TCP Client B
import socket 
import sys

host = socket.gethostname() 
port = int(sys.argv[1])
BUFFER_SIZE = 1024
MESSAGE = raw_input("ClientB: Enter message/ 'exit' to exit:") 
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))

while MESSAGE != 'exit':
    tcpClientB.send(MESSAGE)     
    data = tcpClientB.recv(BUFFER_SIZE)
    print " ClientB received data:", data
    MESSAGE = raw_input("ClientB: Enter message to continue/ Enter exit:")

tcpClientB.close() 