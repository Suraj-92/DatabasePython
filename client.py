'''
Author - Suraj N Temkar.
Date - 16/04/2021
Title - Socket programming simple program (Connection and print hello message).
'''

# Import socket module
import socket	

def client():
    # Create a socket object
    client = socket.socket()		

    # Define the port on which you want to connect
    port = 12345				

    # connect to the server on local computer
    client.connect(('127.0.0.1', port))

    # receive data from the server  
    print (client.recv(1024).decode() )

    # close the connection
    client.close()	

if __name__ == '__main__':
    client()    # Function call
