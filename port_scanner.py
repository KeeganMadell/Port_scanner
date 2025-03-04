import socket
import sys
from datetime import datetime

def scan_ports(ip, start_port, end_port):
    """
    Scans for open ports on a given IP address within a specified range of ports.

    Args:
        ip (str): The target IP address to scan.
        start_port (int): The first port to scan.
        end_port (int): The last port to scan.
    """
    print(f"\nStarting scan on host: {ip}")
    print(f"Scanning ports from {start_port} to {end_port}\n")

    open_ports = []  # List to store open ports

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
        sock.settimeout(0.5)  # Set a timeout for the connection attempt
        result = sock.connect_ex((ip, port))  # Attempt to connect to the port

        if result == 0:
            print(f"Port {port} is open")  # If the connection attempt is successful, the port is open
            open_ports.append(port)
        else:
            print(f"Port {port} is closed")  # If the connection attempt is unsuccessful, the port is closed
        sock.close()  # Close the socket

    if open_ports:
        print("\nOpen ports found:")
        for port in open_ports:
            print(f"- Port {port} is open")
    else:
        print("\nNo open ports found.")

def validate_ip(ip):
    """
    Validates the format of the provided IP address.

    Args:
        ip (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    try:
        socket.inet_aton(ip)  # Check if the IP address is valid
        return True
    except socket.error:
        return False

def main():
    pass

if __name__ == "__main__":
    main()