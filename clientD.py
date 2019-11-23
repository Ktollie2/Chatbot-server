# Python TCP Client D
import socket 
import sys

host = socket.gethostname() 
port = int(sys.argv[1])
BUFFER_SIZE = 1024 
MESSAGE = raw_input("ClientD: Enter message/ 'exit' to exit:") 
 
tcpClientD = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientD.connect((host, port))

while MESSAGE != 'exit':
    tcpClientD.send(MESSAGE)     
    data = tcpClientD.recv(BUFFER_SIZE)
    print " ClientD received data:", data
    MESSAGE = raw_input("ClientD: Enter message to continue/ Enter exit:")

tcpClientD.close() 