import socket
import sys
import thread

import threading
import time
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
"""
server_address = ('localhost', 8441)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)


try:
    
    # Send data
    #for i in range(1 50) 
    message = 'Sv?'
    print >>sys.stderr, 'sending "%s"' % message
    sock.send(message)

  
    data = sock.recv(1024)

    #message = '/|1043|147'
    #print >>sys.stderr, 'sending "%s"' % message
    #sock.send(message)

    #print (data)
    print >>sys.stderr, 'received "%s"' % data
    #sock.close()

finally:
    print >>sys.stderr, 'closing socket'
    #time.sleep(10)
    sock.close()


"""

def hilo():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 9443)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)

    message = '/|1043|147'
    print >>sys.stderr, 'sending "%s"' % message
    sock.send(message)
    data = sock.recv(1024)
    print (data)
    """
    #print (data)
    print >>sys.stderr, 'received "%s"' % data
    #sock.close()
    message = '/|10|14'
    print >>sys.stderr, 'sending "%s"' % message
    sock.send(message)
    data = sock.recv(1024)
    print >>sys.stderr, 'received "%s"' % data
    message = '/|109|0'
    print >>sys.stderr, 'sending "%s"' % message
    sock.send(message)
    data = sock.recv(1024)
    print >>sys.stderr, 'received "%s"' % data
    """
    sock.close()


    # Send data
    #for i in range(1 50) 

NUM_HILOS = 1000

for num_hilo in range(NUM_HILOS):
    hilo1 = threading.Thread(name='hilo%s' %num_hilo, target=hilo)    
    hilo1.start()

    #hilow = threading.Thread(target=hilo, args=(connection,client_address))

    #hilow.start()
    #hilow.destroy()
    #sock.close()

    
