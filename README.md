This is a port scanner that I made for school. It prints the IP address of the given URL and the time the scan starts. Then it uses a try except block to loop through the given port range. It creates a socket object with a family address of IP 4 with a sock_stream type. Then it connects to the given ip address and the current port in the loop. If the connection returns 0, it prints open. If the connection returns 1, it prints closed. Then it closes the connention. There are several exceptions that it can raise. They are if interreupted by the keyboard, error relating to the IP address, or if there are any system related errors. If it finishes the scan it prints out the time the scan ended. ONLY FOR USE SCANNING SITES THAT ALLOW YOU TO (like hackthissite.org) OR IF YOU HAVE PERMISSION TO SCAN THEM. 