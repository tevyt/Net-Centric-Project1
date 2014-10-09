__author__ = '620065811'
from socket import*


def create_client():
    global serverName, serverPort, input, f, clientSocket, response
    serverName = 'localhost'
    serverPort = 21000
    input = raw_input('Enter a file name(hello.html)(Type exit to end): ')
    f = 'GET /' + input
    while input != 'exit':
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(f)
        response = clientSocket.recv(1024)

        if response.split()[1] == "200":
            print(response)
            while not "</html>" in response:
                response = clientSocket.recv(1024)
                print(response)
        elif response.split()[1] == "404":
            print(response)
            response = clientSocket.recv(1024)
            print(response)

        input = raw_input('Enter a file name(Type exit to end): ')
        f = 'GET /' + input


create_client()





