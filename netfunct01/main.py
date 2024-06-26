#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import crayons #just so crayons works for coloring stuff

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring with RED:wq

        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f"Attempting to send {crayons.green('Command')} --> {mycmds}")
            # we'll learn to write code that sends cmds to device here
    return None

def devicereboot(ip_list):
    """Function to reboot devices"""
    for ip in ip_list:
        print(f"Connecting to {ip}...")
        print("REBOOTING NOW!")

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print("Welcome to the {crayons.blue('Network')} Device Command Pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    # reboot devices option
    ip_list = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    devicereboot(ip_list)

# call our main function
main()
