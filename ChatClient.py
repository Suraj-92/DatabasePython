'''
Author - Suraj N Temkar.
Date - 16/04/2021
Title - Chat Application using socket programming.
'''

# Importing libraries
from socket import *
from time import *

def client_program():
    
    client = socket()
    client.connect(('localhost',2000))
    print("Connected to server")
    message = input(" -> ")  # take input


    while message.lower().strip() != 'bye': # strip()-Remove spaces at the beginning and at the end of the string
        client.send(message.encode())  # send message
        data = client.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal
        
        message = input(" -> ")  # again take input

    client.close()  # close the connection

# main function
if __name__ == '__main__':
    client_program()    
