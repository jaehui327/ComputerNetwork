# Import socket module
from socket import *
from threading import Thread
from HttpRequest import *

import sys # In order to terminate the program


# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789
thread_num = 1


# Bind the socket to server address and server port
serverSocket.bind(('', serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections

while True:
        print('The server is ready to receive')

        # Set up a new connection from the client
        connectionSocket, addr = serverSocket.accept()
        th = Thread(target=httpReq, args=(connectionSocket, thread_num))
        print('\nThread',thread_num,' started \n')
        th.start()
        thread_num = thread_num+1

        
serverSocket.close()
sys.exit()
