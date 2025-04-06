import sys
import socket
from datetime import datetime
import threading

def scan_port(target, port):
    try:                   #ipv4           #port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port: {port} is open")
        s.close()
    except socket.error as e:
        print(f"Socket error on port {port}: {e}")
    except Exception as e:
        print(f"Unexpected error on port {port}: {e}")

def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print("Invalid number of arguments")
        print("usage: <Python> <scan.py> <ip>")
        sys.exit(1) # exited with an error

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror: #host name issue
        print(f"Error: Unable to resolve host name '{target}'")
        sys.exit(1)

    print("=" * 30)
    print("SCANINATOR")
    print("=" * 30)
    print(f"Scanning target: {target_ip}")
    print(f"Time started: {datetime.now()}")
    print("=" * 30)

    try:
        threads = []
        for port in range(1, 65536):
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit(0)
    
    except socket.error as e:
        print(f"Socket error: {e}")
        sys.exit(1)
    
    print("=" * 20)
    print("\nScan completed.")
    print(f"Time Completed: {datetime.now()}")
    

if __name__ == '__main__':
    main()