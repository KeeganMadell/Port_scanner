A python program that scans your network for open ports.

It uses the `socket` library to scan for open ports on a given IP address.

The program consists of a single file and 2 functions, 
File:
- port_scanner.py

Functions:
- validate_ip(ip) - This function validates the IP address entered by the user.
- scan_ports(ip, start_port, end_port) - This function scans the IP address for open ports.


How it works:
- The program takes an IP address as input.
- It then scans the the start and end port the user chooses on that IP address.
- It then prints out the open ports on that IP address.

This program is useful for network administrators who want to scan their network for open ports.

To run the program, simply run the `port_scanner.py`.

Created by:
KeeganMadell

The HUB: https://github.com/KeeganMadell