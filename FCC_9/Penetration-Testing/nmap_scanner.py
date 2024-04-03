#!/usr/bin/python3
import nmap 

SCANNER = nmap.PortScanner()
CHECK = True
print("Welcome")

#IPADDR = input("Please enter the IP Address you want to scan: ")
#print("The IP you entered was {}".format(str(IPADDR)))
#type(IPADDR)

choices = {1:"SYN ACK Scan", 2:"UDP Scan", 3:"Comprehensive Scan"}


resp = input("\n1) {}\n2) {}\n3) {}\nPlease enter the type of scan you want to run: ".format(
    choices[1], 
    choices[2],
    choices[3]
))

print("\nYou've selected: {}".format(choices[int(resp)]))