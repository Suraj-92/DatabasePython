'''
Author - Suraj N Temkar.
Date - 17/04/2021
Modified Date - 18/04/2021
Title - Chat Application using socket programming(One server and multiple clients).
'''

# Importing libraries
import socket
import threading    # """Thread module emulating a subset of Java's threading model."""
import pickle   # Create portable serialized representations of Python objects.
import mysql.connector 

connectedlist = []  # Store data in the list 

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # AF_INET- address family IPV4 and SOCK_STREAM-Connection oriented i.e TCP/IP
print("Opened the server socket to listen to new connections")
print("server socket....",serversocket)
print(dir(serversocket))

ret = serversocket.bind(('localhost',9026))
print("Bind to the local port", ret)

serversocket.listen(5)
print("Started listening to the local port ")

def chatbackup(clientname, message, cursor):
    mySql_insert_query = """INSERT INTO chat_app (client_name, chat) 
                            VALUES 
                            (%s, %s) """
    values = (clientname, message)

    cursor.execute(mySql_insert_query, values)
    connection.commit()
    print(cursor.lastrowid, "Record inserted successfully into table")
    # cursor.close()


def NewChatClient(client, ip, cursor):
    while True:
        message = client.recv(1024)
        messagepickle = pickle.loads(message) # loads()- Deserialize data stream  and dumps()-Serialize object

        print(messagepickle[0]) # Actual message send from one cleint to another
        chatbackup(messagepickle[1],messagepickle[0], cursor)
        print(messagepickle[1]) # name of the client who send the msg

        for l1 in connectedlist:
            if l1[0] == messagepickle[1]: # check name of the client is available or not
                l1[1].send(bytes(messagepickle[0],"utf-8")) # send the msg to other client
                break

 
    
try:
    connection = mysql.connector.connect(host='localhost',
                                            database='chatapplication',
                                            user='root',
                                            port='3306',
                                            password='root')
    cursor = connection.cursor()
    print("Print.....",cursor)
    while True:
        clientsocket, ip = serversocket.accept()
        print("New client connected from: ",ip)

        clientsocket.send(bytes("Connected","utf-8"))
        # Get the client name
        clientname = clientsocket.recv(1024).decode()
        nameclientpair = [clientname, clientsocket]
        connectedlist.append(nameclientpair)
        clientsocket.send(bytes("Enable for chat","utf-8"))

        threading._start_new_thread(NewChatClient, (clientsocket, ip, cursor))

except Exception as e:
    print("Exception is ...................",e)

finally:
    cursor.close()
    
