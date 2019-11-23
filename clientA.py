# Python TCP Client A
import socket 
import sys

host = socket.gethostname() 
port = int(sys.argv[1])
BUFFER_SIZE = 1024
MESSAGE = raw_input("tcpClientA: Enter message/ 'exit' to exit:") 
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE)     
    data = tcpClientA.recv(BUFFER_SIZE)
    print " ClientA received data:", data
    MESSAGE = raw_input("ClientA: Enter message to continue/ Enter exit:")

tcpClientA.close() 