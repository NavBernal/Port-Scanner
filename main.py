import socket
import threading
from queue import Queue

# Target IP address for the port scan (change this to the desired target)
target = '192.168.7.1'

# Queue to hold the ports that need to be scanned
queue = Queue()

# List to store open ports
open_ports = []

# Function to scan a single port
def portscan(port):
    try:
        # Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Try to connect to the target IP and port
        sock.connect((target, port))
        return True
    except:
        return False

# Function to fill the queue with the list of ports to be scanned
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)  # Add each port to the queue

# Worker function for scanning ports in the queue
def worker():
    while not queue.empty():
        port = queue.get()
        
        # If the port is open, print and store it
        if portscan(port):
            print('Port {} is open!'.format(port))
            open_ports.append(port)

# List of ports to scan (in this case, ports 1 to 1023)
port_list = range(1, 1024)

# Fill the queue with ports to be scanned
fill_queue(port_list)

# List to store the thread objects
thread_list = []

# Create 10 threads to perform the port scan concurrently
# More threads can be added for quicker results
for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

# Start each thread
for thread in thread_list:
    thread.start()

# Wait for all threads to finish before proceeding
for thread in thread_list:
    thread.join()

# Print the list of open ports found
print('Open ports are: ', open_ports)