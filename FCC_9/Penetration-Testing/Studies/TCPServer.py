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
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# You should be able to automatically get the hostname/IP address
host = socket.gethostname() #>> Amaterasu
ipaddr = socket.gethostbyname(host) #>> IP Address
port = 5500
''' 
The class made us use port 444, which I was getting a system error #13.
I have since found out that  all ports <1024 are system reserved and you have to 
be running as a "priviledged" user. 

Curious thing though, when I try to run this program as sudo python3 TCPServer.py, 
trying to give this root priviledges, it does not work. In turn, I changed the port
to 1024 to address the problem. Worked just fine.
'''

serversocket.bind((ipaddr, port))

# setup a listener for however many you are looking to listen to
serversocket.listen(3)
while True:
    clientsocket, address = serversocket.accept()
    print("received connection from {}").format(str(address))
    message = "Welcome to the server.\n"
    clientsocket.send(message)
    clientsocket.close()



