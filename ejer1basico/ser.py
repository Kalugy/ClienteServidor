import socket
import sys
import thread



def hilo(connection, addr):
	while True:
		
		#print connection.recv(16)
		#amount_received = 0
		#amount_expected = len(message)

		datos=[]
		i=True
		while i:
			
			#print connection.recv(16)
			#print len(connection.recv(16))
			a=connection.recv(16)
			datos.append(a)
			print (datos)
			#print len(connection.recv(16))
			if len(a)<13:
				print "entro"
				i=False
				

		print >>sys.stderr, 'received "%s"' % datos
		if datos:
			print >>sys.stderr, 'sending data back to the client'
			data=" "
			for x in datos:
				data=data + x
			connection.sendall(data)
		else:
			print >>sys.stderr, 'no more data from', client_address
		                     
		# Clean up the connection
		#connection.close()



while 1:


	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the port
	server_address = ('localhost', 9026)
	print >>sys.stderr, 'starting up on %s port %s' % server_address
	sock.bind(server_address)

	# Listen for incoming connections
	sock.listen(1)

	connection, client_address = sock.accept()

	print >>sys.stderr, 'connection from', client_address

    
	thread.start_new_thread(hilo,(connection,client_address))


