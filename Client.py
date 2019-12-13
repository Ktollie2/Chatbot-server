# Python TCP Client A
import socket 
import sys

host = socket.gethostname() 
port = int(sys.argv[1])
BUFFER_SIZE = 1024
MESSAGE = raw_input("tcpClientA: Enter message/ 'exit' to exit:") 
 
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))

while MESSAGE != 'exit':
    tcpClient.send(MESSAGE)
    data = tcpClient.recv(BUFFER_SIZE)
    print data
    MESSAGE = raw_input("ClientA: Enter message to continue/ Enter exit:")

tcpClient.close() 
