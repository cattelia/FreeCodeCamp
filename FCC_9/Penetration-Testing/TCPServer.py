# tcp
# udp
# (web) socket

#! /usr/bin/python3
import socket

# CREATING THE TCP SERVER
#create the socket object
''' AF_INET == IPv4
    AF_INET6 == IPv6 '''
# choose socket family and the socket type
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# You should be able to automatically get the hostname/IP address
host = socket.gethostbyname()
port = 444

server_socket.bind((host, port))

# setup a listener for however many you are looking to listen to
server_socket.listen(3)
while True:
    client_socket, address = server_socket.accept()
    print("received connection from {}").format(str(address))
    message = "Welcome to the server./n"
    client_socket.send(message)
    client_socket.close()



