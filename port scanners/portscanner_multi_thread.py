# Using a queue, adding the ports to be scanned into a queue,
# everytime that each one is evaluated it's removed from the queu

import queue
import socket
import threading
from queue import Queue



def port_scan(port):
    try:
        # socket.socket(socket_family, socket_type, protocol)
        # param1: using internet socket rather than a unix socket
        # param2: using tcp instead of udp
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # now we connect, but first we have to define where we're connecting to
        sckt.connect((target, port))

        # connection succesful: port  open
        return True
    except:
        #connection unsuccessful: port closed
        return False

# pass in a range of ports that will be scanned
# FIFO data structure, first port that enters the queue will be the first to be evaluated
def populate_queue(port_list):
    for port in port_list:
        queue.put(port)

# every thread will execute this function
def evaluate_next_port():
    # While the port isn't empty, get the next port in the queue and scan it
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print(f"Port {port} is open")
            open_ports.append(port)
        """
        else:
            # only print the open ports because that's all we care about and also it might get clunky with so many statements at once
            # can use below code as testing code to make sure it works
            print(f"Port {port} is closed")
        """
queue = Queue()
open_ports = []

target = input("What is the target ip address that you want to scan for open ports?")
start_port = int(input("What port would you like to start scanning from?"))
stop_port = int(input("What port would you like to stop scanning from?"))


# target = input("What is the target ip address you want to scan?")
port_list = range(start_port, stop_port+1)
populate_queue(port_list)

thread_list = []
for i in range(500):
    # creating x amounts of threads with the target function
    thread = threading.Thread(target = evaluate_next_port)
    thread_list.append(thread)


for thread in thread_list:
    thread.start()

for thread in thread_list:
    # synchronisation method,
    # wait/make sure all our threads are completed before continuing with code i.e printing open ports
    thread.join()

print("Open ports are: ", open_ports)