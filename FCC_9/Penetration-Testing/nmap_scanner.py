#!/usr/bin/python3

import nmap # Used for NMAP scanning
import time # Used in Try/Except statement
import sys # Used in Try/Except statement
from colorama import Fore # Used in Try/Except statement

SCANNER = nmap.PortScanner()
CHECK = True
print("Welcome")

#IPADDR = input("Please enter the IP Address you want to scan: ")
#print("The IP you entered was {}".format(str(IPADDR)))
#type(IPADDR)

# Dictionary to easily update scanning options for future scaling of NMAP features
choices = {1:"EXIT", 2:"UDP Scan", 3:"SYN ACK Scan", 4:"Comprehensive Scan"}


# Ask user to indicate which scan they would like to run. 
#   "1" will always be EXIT for them to leave the program.
#   If there are additional NMAP features to be added,
#   this is where you will include those options.
#   AND under "except KeyError"
resp = input("\n1) {}\n2) {}\n3) {}\n4) {}\nPlease enter the type of scan you want to run: ".format(
    choices[1], 
    choices[2],
    choices[3],
    choices[4]
))

# While True, ask the user what they want to do.
while CHECK:

    # Let them exit immediately and shut the program down.
    # Using `import sys`
    if int(resp) == 1:
        print("\nExiting program...")
        sys.exit(0)

    # Input sanitation. Make sure they enter the options provided above.
    # Will throw a KeyError if not.
    try:
        print("\nYou've selected: {}".format(choices[int(resp)]))
        CHECK = False

    # If KeyError is caught, tell them that they need to entire from the options provided above.
    except KeyError:
        # Using Fore to color the text Red so they immediately notice it.
        print(Fore.RED + "\nPlease choose a valid option from the list above...")
        # Give them 1 second to absorb the message and then feed the options again.
        time.sleep(1)
        resp = input(Fore.WHITE + "\n1) {}\n2) {}\n3) {}\n4) {}\nPlease enter the type of scan you want to run: ".format(
            choices[1], 
            choices[2],
            choices[3],
            choices[4]
        ))
    else:
        pass