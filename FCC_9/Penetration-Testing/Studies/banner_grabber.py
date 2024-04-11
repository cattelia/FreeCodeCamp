#!/usr/bin/python3

import socket


def banner(ip, port):
    SOCKET = socket.socket()
    SOCKET.connect((ip, int(port)))
    print(SOCKET.recv(1024)) #max amount of data that we should receive back


def main():
    IPADDR = input("Please enter IP address: ")
    PORT = input("Please enter the port: ")
    banner(IPADDR, PORT)


main()