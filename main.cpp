#include <iostream>
#include <string>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <netdb.h>
#include <sys/uio.h>
#include <sys/time.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <fstream>
using namespace std;

int main(int argc, const char * argv[]) {
    
    if (argc != 1)
    {
        cerr << "Error please enter port number" << endl;
        exit(0);
    }
    
    // get the port number from arguments
    int port = atoi(argv[1]);

    // Buffer for messages that are sent
    char message[1000];
    
    // Establishing server connection
    sockaddr_in serverAddress;
    bzero((char*)&serverAddress, sizeof(serverAddress));
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = htonl(INADDR_ANY);
    serverAddress.sin_port = htons(port);
    
    int serverSide = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSide < 0)
    {
        cerr << "ERROR couldn't connect to server" << endl;
        exit(0);
    }
    
    bind(serverSide,(struct sockaddr_in*)&serverAddress, sizeof(serverAddress));
    
    listen(serverSide, 5);
    sockaddr_in newSocketAddress;
    socklen_t newSocketAddressSize = sizeof(newSocketAddress);
    
    int newServerSide = accept(serverSide,(struct sockaddr*)&newSocketAddress, &newSocketAddressSize);
    
    if (newServerSide < 0)
    {
        cerr << "ERROR could'nt accept request from client" << endl;
        exit(1);
    }
    cout << "Connected with the client" << endl;
    
    int bytesRead, bytesWritten = 0;
    
    while(true)
    {
        cout << "Waiting for client response" << endl;
        memset(&message, 0, sizeof(message));
        bytesRead += recv(newServerSide, (char*)&message, sizeof(message), 0);
        if(!strcmp(message, "exit"))
        {
            cout << "The client has quit this session" << endl;
            break;
        }
        
    }
    
    

    
    
}

