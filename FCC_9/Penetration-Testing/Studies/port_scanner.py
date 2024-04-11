#!/usr/bin/Python3

import socket

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 and TCP connection
#HOST = "137.74.187.102"
HOST = input("IP Address: ")
PORT = 80

def portScanner(port):
    if SOCKET.connect_ex((HOST, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(PORT)

