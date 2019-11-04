from socket import *
import time

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)

for i in range(1, 11):       
    message = 'Ping'
    start = time.time()
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try: 
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print("test " + str(i) + " : " + modifiedMessage.decode())
        end = time.time() - start
        end = float("{0:.5f}".format(end))
        print("RTT: " + str(end) + "sec")
    except socket.timeout:
        print("test " + str(i))
        print("Response timed out")
    print("")
    
clientSocket.close()
                                            
