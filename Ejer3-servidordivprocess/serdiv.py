import socket
import sys
#import thread
import threading
from multiprocessing import Process

def proceso(connection, addr):
	
	
	#print connection.recv(16)
	#amount_received = 0
	#amount_expected = len(message)

	datos=[]
	i=True
	while i:
		
		#print connection.recv(16)
		#print len(connection.recv(16))
		a=connection.recv(1024)
		print (a)
		datos=a.split("|")
		print (datos)
		resultado=0
		if (datos[0]=="/"):
			try :
				if(datos[2]!="0"):
					resultado=int(datos[1])/int(datos[2])
				else:
					resultado="Operando indeterminada"
			except:
				resultado="Error operando"
		else:
			resultado="Error en sintaxis"
		
		print(str(resultado))
		a=str(resultado)
		connection.send(a)
		#i=False
	# Clean up the connection
	connection.close()




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 9001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:

	connection, client_address = sock.accept()


	#p = threading.Thread(target=hilo, args=(connection,client_address))


	p = Process(target=proceso, args=(connection,client_address))
	p.start()
	p.join()
	#hilow.destroy()

	#thread.start_new_thread(hilo,(connection,client_address))

