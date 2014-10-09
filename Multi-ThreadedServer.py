__author__ = 'travis'
#import socket module
from socket import *
import thread


def check_port(create_port, port):
    if create_port:
        thread.start_new_thread(create_server, (port + 1, True))
    return False


def create_server(port, create_port):
    global serverSocket, connectionSocket, address, message, filename, f, output_data, i
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(('localhost', port))
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
            create_port = check_port(create_port, port)
        except IOError:
            #Send response message for file not found

            connectionSocket.send('HTTP/1.1 404 NOT FOUND\r\n\r\n')
            connectionSocket.send('File not found: ' + message.split()[1][1:])

            connectionSocket.close()
            create_port = check_port(create_port, port)
    serverSocket.close()
thread.start_new_thread(create_server, (10000, True))

while True:
    pass
