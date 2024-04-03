#!/usr/bin/python3
import nmap 

SCANNER = nmap.PortScanner()
CHECK = True
print("Welcome")

IPADDR = input("What IP do you want to scan?: ")
answer = input("You entered {}, is this correct? True or False".format(IPADDR))
if answer.lower().strip() == False:
    IPADDR = input("What IP do you want to scan?: ")



