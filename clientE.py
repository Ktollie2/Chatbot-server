# Python TCP Client E
import socket 
import sys

host = socket.gethostname() 
port = int(sys.argv[1])
BUFFER_SIZE = 1024 
MESSAGE = raw_input("ClientE: Enter message/ 'exit' to exit:") 
 
tcpClientE = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientE.connect((host, port))

while MESSAGE != 'exit':
    tcpClientE.send(MESSAGE)     
    data = tcpClientE.recv(BUFFER_SIZE)
    print " ClientE received data:", data
    MESSAGE = raw_input("ClientE: Enter message to continue/ Enter exit:")

tcpClientE.close() 