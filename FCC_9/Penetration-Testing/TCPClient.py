# CREATE THE TCP CLIENT

#!/usr/bin/python3
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_host = socket.gethostname()
client_port = 444

client_socket.connect((client_host, client_port))
message = client_socket.recv(1024) #maximum amount of data that is allowed to come through the TCP protocol

client_socket.close()
print(message.decode('ascii'))

