'''
Author - Suraj N Temkar.
Date - 16/04/2021
Title - Chat Application using socket programming.
'''

from socket import *
from time import *

class server:
    def server_program(self):
    
        self.server = socket(AF_INET,SOCK_STREAM)   # AF_INET- address family IPV4 and SOCK_STREAM-Connection oriented i.e TCP/IP

        self.server.bind(('localhost',2000))

        self.server.listen()
        print("Server listening at 2000")

        connection, address = self.server.accept()
        print("Connected to client",str(address))
    
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = connection.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("from connected Client: " + str(data))
            data = input(' -> ')
            connection.send(data.encode())  # send data to the client

        connection.close()  # close the connection


if __name__ == '__main__':
    serverobject = server() # create class object
    serverobject.server_program()   # function call/method call through class object
