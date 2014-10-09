#import socket module
from socket import *

#620065811

def create_server():
    global serverSocket, connectionSocket, address, message, filename, f, output_data, i
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(('localhost', 21000))
    serverSocket.listen(1)
    while True:

        #Prepare a server socket

        #Establish the connection
        print 'Ready to serve...'
        connectionSocket, address = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            output_data = f.readlines()
            #Send one HTTP header line into socket

            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')

            #Send the content of the requested file to client

            for i in range(0, len(output_data)):
                connectionSocket.send(output_data[i])
            connectionSocket.close()
        except IOError:
            #Send response message for file not found

            connectionSocket.send('HTTP/1.1 404 NOT FOUND\r\n\r\n')
            connectionSocket.send('File not found: ' + message.split()[1][1:])

            connectionSocket.close()
    serverSocket.close()
create_server()