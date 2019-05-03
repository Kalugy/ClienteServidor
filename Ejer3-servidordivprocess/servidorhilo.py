import socket
import sys
#import thread
import threading
import time
from multiprocessing import Process
from threading import Thread, Lock

mutex = Lock()

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

#cuantas conexiones al mismo tiempo puedo tener
#Cuantas segundos por radio o por tiempo

#timestamp minimo maximo 
#cuantas conexiones fueron menores menos de 
def hilo(connection, addr):
	
	
	#print connection.recv(16)
	#amount_received = 0
	#amount_expected = len(message)

	datos=[]
	i=True
	print("hey")
	try:


		while i:
			print("entra")
			a=connection.recv(1024)	
			#print connection.recv(16)
			#print len(connection.recv(16))
			
			print (a)
			print(type(a))
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
			elif(datos[0]==""):
				print("dato vacio o fin")
				i=False;	
			else:
				resultado="Error en sintaxis"
			


			print(str(resultado))
			b=str(resultado)
			#time.sleep(10)
			#Lectura de archivo y log
			mutex.acquire()
			f = open ('log2.txt','a')
			escritura=" (Cliente,Puerto) " + str(addr) + " Dato recibido "+ a + " Resultado "+ str(resultado) +"\n"
			f.write(escritura)
			f.close()
			mutex.release()
			connection.send(b)

		#connection.close()
	except:
		print("Conexion fallida")
		# Clean up the connection
		connection.close()			





sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
#server_address = ('192.168.8.138', 9400)
server_address = ('localhost', 9456)
print >>sys.stderr, 'starting up on %s port %s' % server_address
try:
	sock.bind(server_address)
except:
	pass

"""
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address2 = ('localhost', 8432)
print >>sys.stderr, 'starting up on %s port %s' % server_address2
try:
	sock2.bind(server_address2)
except:
	pass
"""	
# Listen for incoming connections

sock.listen(1)
#sock2.listen(1)
"""
print("entre")
try:
	
	connection2, client_address2 = sock2.accept()
	p2 = Process(target=proceso2, args=(connection2,client_address2))
	p2.start()
	p2.join()
except:
	print("Error al conectarse")	
	connection2.close()	
"""	
while True:

	try:
		connection, client_address = sock.accept()
		#print("entro")
		#p = Process(target=proceso, args=(connection,client_address))
		#p = threading.Thread(target=hilo, args=(connection,client_address))
		hilow = threading.Thread(target=hilo, args=(connection,client_address))

		hilow.start()
		#p.start()
		#p.join()
			

	except:
		connection.close()	
	#p = threading.Thread(target=hilo, args=(connection,client_address))

		#print("Error al conectarse")	
		#connection2.send("Error al conectarse")

	#hilow.destroy()

	#thread.start_new_thread(hilo,(connection,client_address))
