import threading
from socket import *
from time import sleep
import sys

def httpReq(connectionSocket, thread_num):
        try: 
                # Receives the request message from the client
                message = connectionSocket.recv(2048).decode()
                print(message)

                # Extract the path of the requested object from the message
                # The path is the second part of HTTP header, identified by [1]
                filename = message.split()[1]
                print(filename)

	        # Because the extracted path of the HTTP request includes 
	        # a character '\', we read the path from the second character
                myfile = open(filename[1:],'rb')

	        # Store the entire contenet of the requested file in a temporary buffer
                response = myfile.read()
                myfile.close()
		
		# Send the HTTP response header line to the connection socket
                header = 'HTTP/1.1 200 OK\n'

                if(filename.endswith(".jpg")):
                        filetype = 'image/jpg'
                elif(filename.endswith(".mp4")):
                        filetype = 'video/mp4'
                else:
                        filetype = 'text/html'

                header += 'Content-Type: '+str(filetype)+'\n\n'
                print(header)

                connectionSocket.send(header.encode())
                connectionSocket.send(response)
                connectionSocket.close()

                for i in range(1,10):
                        sleep(1)
                        print('thread number=', thread_num,'count=', i)                        

        except IOError:
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode() 

                print(header)
                connectionSocket.send(header.encode())
                connectionSocket.send(response)
                connectionSocket.close()
