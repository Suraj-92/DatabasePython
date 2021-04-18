'''
Author - Suraj N Temkar.
Date - 16/04/2021
Title - Socket programming simple program (Connection and print hello message).
'''

# import socket library
import socket			

def server():
    # create a socket object
    server = socket.socket()		
    print ("Socket successfully created")

    # reserve a port on your computer in our case it is 12345 but it can be anything
    port = 12345				

    # bind to the port
    # we have not typed any ip in the ip field instead we have inputted an empty string this makes the server listen to requests
                                        # coming from other computers on the network
    server.bind(('', port))		
    print ("socket binded to %s" %(port))

    # put the socket into listening mode
    server.listen(5)	
    print ("socket is listening")			

    # a forever loop until we interrupt it or an error occurs
    while True:

        # Establish connection with client.
        connetion, address = server.accept()	
        print ('Got connection from', address )

        # send a thank you message to the client.
        data = input(' -> Thanks For Connecting \n ->')
        connetion.send(data.encode())  # send data to the client

    # Close the connection with the client
    connetion.close()

# Main method
if __name__ == '__main__':
    server()    # function call
