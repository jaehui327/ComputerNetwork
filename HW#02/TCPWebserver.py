from socket import *
import sys
import io
from PIL import Image
import cv2

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 6789

serverSocket.bind(("", serverPort))

serverSocket.listen(1)

while True:
    print('The server is ready to receive')

    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        
        filename = message.split()[1]
        filename = filename[1:]
        extension = filename.split('.')[1]
        print(extension)

        if extension == 'html':
                f = open(filename)
                outputdata = f.read()
                connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) 

                for i in range(0, len(outputdata)):  
                        connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
                
        if extension == 'jpeg':
                outputdata = Image.open("./" + filename)
                outputBuffer = io.BytesIO()
                outputdata.save(outputBuffer, format='JPEG')
                connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

                connectionSocket.send(outputBuffer.getvalue())

        if extension == 'mp4':
                cap = cv2.VideoCapture('./' + filename)
                while(cap.isOpened()):
                        ret, frame = cap.read()
                        frame = cv2.cvtColor(frame, 0)
                        cv2.imshow('frame', frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'): break

                connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

                connectionSocket.send(outputBuffer.getvalue())

        connectionSocket.close()

    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send(
            "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        connectionSocket.close()

serverSocket.close()
sys.exit()
