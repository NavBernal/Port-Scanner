# Port Scanner

This Python-based project is a simple multi-threaded port scanner that scans a range of ports (1-1023) on a target IP address to check if they are open. The project uses threading to speed up the scanning process by concurrently checking multiple ports.

## How It Works

1. **Target IP input:** The user is prompted to input the IP address of the system they want to scan.
2. **Port scanning:** The program attempts to connect to each port in the range from 1 to 1023.
3. **Multithreading:** The scan is performed concurrently using 10 threads (configurable) to improve performance.
4. **Open port detection:** If a connection is successful on a port, that port is considered open and is stored and printed.

## Running the Project

### 1. Run the Port Scanner:
Execute the port scanner script in your terminal:

`python port_scanner.py`

### 2. Enter the Target IP:
Once the script starts, you will be prompted to enter the IP address of the target system:

`Enter a target IP to be scanned: 192.168.1.1`

The script will then begin scanning ports on the target IP and print out any open ports.

## Example

### Output:
```bash
Enter a target IP to be scanned: 192.168.1.1
Port 22 is open!
Port 80 is open!
Port 443 is open!
Open ports are:  [22, 80, 443]
```

## Notes
- **Speed:** The script uses 10 threads by default to scan ports concurrently, but you can increase this number for faster scans (at the risk of being rate-limited by the target system).
- **Target IP:** This script assumes that the target system is reachable and that the ports you are scanning are not blocked by a firewall.
- **Port Range:** The current port range is set to 1–1023. You can modify the port_list to scan a different range of ports.
