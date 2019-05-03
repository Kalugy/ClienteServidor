import socket
import sys
#import thread
import threading
import time
from multiprocessing import Process

def proceso2(connection, addr):
	
	
	#print connection.recv(16)
	#amount_received = 0
	#amount_expected = len(message)

	datos=[]
	i=True
	#print("alo")
	try:
		while i:
			a=connection.recv(1024)	
			#print connection.recv(16)
			#print len(connection.recv(16))
			
			print (a)
			#print (datos)
			datos=a.split("|")
			resultado=0
			if (a==	"Sv?"):
				resultado="serv|/|9400"
			elif(datos[0]==""):
				print("dato vacio o fin")
				i=False;	
			else:
				resultado="Error bro"

			print(str(resultado))
			b=str(resultado)
			
			connection.send(b)
			#i=False	
		connection.close()	
	except:
		print("Conexion fallida")
		# Clean up the connection
		connection.close()	

		
				



sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address2 = ('192.168.8.138', 8400)
print >>sys.stderr, 'starting up on %s port %s' % server_address2
sock2.bind(server_address2)

# Listen for incoming connections
sock2.listen(1)
while True:


	
	try:
		connection2, client_address2 = sock2.accept()
		p2 = Process(target=proceso2, args=(connection2,client_address2))
		p2.start()
		p2.join()
	except:
		print("Error al conectarse")	
		connection2.close()	
	
	#p = threading.Thread(target=hilo, args=(connection,client_address))

		#print("Error al conectarse")	
		#connection2.send("Error al conectarse")

	#hilow.destroy()

	#thread.start_new_thread(hilo,(connection,client_address))