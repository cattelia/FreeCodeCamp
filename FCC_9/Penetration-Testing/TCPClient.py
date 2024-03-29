# CREATE THE TCP CLIENT

#!/usr/bin/python3
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
ipaddr = socket.gethostbyname(host)
port = 5500

clientsocket.connect((ipaddr, port))
message = clientsocket.recv(1024) #maximum amount of data that is allowed to come through the TCP protocol

clientsocket.close()

print(message.decode('ascii'))


#--------------------

