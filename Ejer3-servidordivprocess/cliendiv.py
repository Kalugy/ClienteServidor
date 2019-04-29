import socket
import sys

import time
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8401)
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
    time.sleep(10)
    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 9401)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    #for i in range(1 50) 


    message = '/|1043|147'
    print >>sys.stderr, 'sending "%s"' % message
    sock.send(message)
    data = sock.recv(1024)
    #print (data)
    print >>sys.stderr, 'received "%s"' % data
    #sock.close()
    message = '/|10|14'
    print >>sys.stderr, 'sending "%s"' % message
    sock.send(message)
    data = sock.recv(1024)
    print >>sys.stderr, 'received "%s"' % data
    #sock.close()
finally:
    print >>sys.stderr, 'closing socket'
    time.sleep(10)
    sock.close()
