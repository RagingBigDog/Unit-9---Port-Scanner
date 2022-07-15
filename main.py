import sys
import socket
from datetime import datetime

# gets the ip address of the given url
ipaddress = socket.gethostbyname("hackthissite.org")

# prints out the ip address of the above ur;
print(ipaddress)

# prints the start time of the scan
print("Scan started at: " + str(datetime.now()))

# try block with exceptions for different errors that may arise
try:
    # loops through the ports in the given range and returns whether they are open or closed
    for port in range(75, 85):
        # creates a socket object with address family ip4 and sock_stream type 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connects to the given ip address and port
        conn = s.connect_ex((ipaddress, port))
        # if the connection returns 0, it prints open
        if conn == 0:
            print("Port {} is open".format(port))
        # otherwise the connection returns 1 and it prints closed
        else:
            print("Port {} is closed".format(port))
        # closes the connection
        s.close()
# raises an error if the program is interrupted by the keyboard
except KeyboardInterrupt:
    print("Port {} is open".format(port))
    sys.exit()

# raises an error if the there is an error relating to the address 
except socket.gaierror:
    print("Hostname could not be resolved!")
    sys.exit()

# raises an error for any system related errors
except socket.error:
    print("Server not responding!")
    sys.exi

# prints the end time of the scan
print("Scan finished at: " + str(datetime.now()))