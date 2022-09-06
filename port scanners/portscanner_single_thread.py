# Not legal unless you have access to ports you attempt to scan
# Will use sockets to attempt to connect to servers/ip-addresses at specific port 
# If successful, port is open, if unsuccesful port is closed

import socket

# using local host - refers back to machine im using right now
target = "127.0.0.1"

def port_scan(port):
    try:
        # using internet socket rather than a unix socket
        # using tcp instead of udp
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # now we connect, but first we have to define where we're connecting to
        sckt.connect((target, port))

        # connection succesful: port  open
        return True
    except:
        #connection unsuccessful: port closed
        return False


# loop through standardised ports reserved for http, ftp etc
for port in range(1,1024):
    result = port_scan(port)
    if result:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
