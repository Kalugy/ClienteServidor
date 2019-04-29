import socket
import sys
#import thread
import threading
import time
from multiprocessing import Process
#Desempeno
	#Tasa de servicio
		#Conexion
		#Responder
#Concurrencia
	##de conexiones activas al mismo de tiempo
	#Error hilo o recurso (timestamp (log))y comprar clientes y servidores
#Cliente servidor
	
#verificar ("Sv?")
#responder ("serv:/:puerto")



def proceso(connection, addr):
	
	
	#print connection.recv(16)
	#amount_received = 0
	#amount_expected = len(message)

	datos=[]
	i=True
	try:


		while i:
			a=connection.recv(1024)	
			#print connection.recv(16)
			#print len(connection.recv(16))
			
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
			b=str(resultado)
			#time.sleep(10)
			#Lectura de archivo y log

			f = open ('log.txt','a')
			escritura=" (Cliente,Puerto) " + str(addr) + " Dato recibido "+ a + " Resultado "+ str(resultado) +"\n"
			f.write(escritura)
			f.close()
			connection.send(b)

	except:
		print("Conexion fallida")
		# Clean up the connection
		connection.close()			



def proceso2(connection, addr):
	
	
	#print connection.recv(16)
	#amount_received = 0
	#amount_expected = len(message)

	datos=[]
	i=True
	try:


		while i:
			a=connection.recv(1024)	
			#print connection.recv(16)
			#print len(connection.recv(16))
			
			print (a)
			print (datos)
			resultado=0
			if (a==	"Sv?"):
				resultado="serv|/|9400"
			else:
				resultado="Error bro"

			print(str(resultado))
			b=str(resultado)
			connection.send(b)

	except:
		print("Conexion fallida")
		# Clean up the connection
		connection.close()			


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
#server_address = ('192.168.9.154', 9000)
server_address = ('localhost', 9401)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)



sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address2 = ('localhost', 8401)
print >>sys.stderr, 'starting up on %s port %s' % server_address2
sock2.bind(server_address2)

# Listen for incoming connections
sock.listen(1)
sock2.listen(1)
while True:

	connection, client_address = sock.accept()
	connection2, client_address2 = sock2.accept()

	#p = threading.Thread(target=hilo, args=(connection,client_address))

	p = Process(target=proceso, args=(connection,client_address))
	p2 = Process(target=proceso2, args=(connection2,client_address2))
	p.start()
	p2.start()
	p.join()
	p2.join()

	#hilow.destroy()

	#thread.start_new_thread(hilo,(connection,client_address))


