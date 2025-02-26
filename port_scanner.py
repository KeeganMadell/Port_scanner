import socket

# Add a feature to scan individual ports

def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
# 192.168.56.1 (for testing) 
def main():
    target_ip = input("Enter an Ip adress to scan for open ports: ")
    start_port = 1
    end_port = 80


    scan_ports(target_ip, start_port, end_port)
if __name__ == "__main__":
    main()