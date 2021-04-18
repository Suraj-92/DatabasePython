'''
Author - Suraj N Temkar.
Date - 17/04/2021
Title - Chat Application using socket programming(One server and multiple clients).
'''

# importing libraries
import socket
import pickle   # Create portable serialized representations of Python objects.
import threading    # Thread module emulating a subset of Java's threading model.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET- address family IPV4 and SOCK_STREAM-Connection oriented i.e TCP/IP

client.connect(('localhost',9026))

message = client.recv(1024).decode()
print("The message from server: ",message)
name = input("Please provide your name: ")

client.send(bytes(name,"utf-8"))
message = client.recv(1024).decode()
print("Message from server: ", message)

def NewChatMessage():
    message = client.recv(1024)
    print(message)

aStarted = False
 
# while message.lower().strip() != 'bye':
while True:
    if aStarted == False:
        threading._start_new_thread(NewChatMessage, ())
        bStarted = True

    message = input("Your Message: ")
    to = input("Send To: ")
    msgToSend = [message, to]
    messagePickle = pickle.dumps(msgToSend) # loads Deserialize data stream  and dumps() - Serialize object
    client.send(messagePickle)
