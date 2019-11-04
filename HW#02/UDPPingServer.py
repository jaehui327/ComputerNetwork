from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print("The server is ready to receive")
i = 1

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    print("test " + str(i) + ": " + modifiedMessage)
    sendMessage = 'Pong'
    serverSocket.sendto(sendMessage.upper().encode(), clientAddress)
    i += 1
