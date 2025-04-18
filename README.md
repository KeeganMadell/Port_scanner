A python program that scans your network for open ports.


The program consists of a single file 
File:
- scan.py

Functions:
scan_port - takes in a ip address and port number and checks if the port is open or closed.


How it works:
You can run the program by passing an IP address as a command line argument. The program will then scan the specified IP address for open ports in the range of 1 to 65535. It uses the socket library to create a connection to each port and checks if it is open or closed. If the port is open, it will print the port number and its status. The program uses threading to speed up the scanning process by scanning multiple ports at once.

This program is useful for network administrators who want to scan their network for open ports.

To run the program:
Open a terminal and navigate to the directory where the program is located and type:
- scan.py <ip adress> or python3 scan.py <ip adress>

Created by:
KeeganMadell

The HUB: https://github.com/KeeganMadell

## Changes - 25/04/06
Made it cleaner and more efficient by using terminal arguments for IP address input and it now uses threading to scan open ports much faster than what I had before.
- old code is located in 'oldcode.txt'