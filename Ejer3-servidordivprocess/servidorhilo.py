import socket
import sys
#import thread
import threading
import time
from multiprocessing import Process
from threading import Thread, Lock

#from time import time
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
def hilo(connection, addr, tiempo_inicial,horadeinicio):
	datos=[]
	a=connection.recv(1024)	
	datos=a.split("|")
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
		#i=False;	
	else:
		resultado="Error en sintaxis"
	print ("dato recivido: "+ str(datos)+ "resultado"+str(resultado) )
	b=str(resultado)
	time.sleep(60)
	connection.send(b)
	horafinal = time.strftime("%H") +":"+ time.strftime("%M") +":"+ time.strftime("%S")
	tiempo_final = time.time() 
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	
	mutex.acquire()

	f = open ('log2.txt','a')
	escritura="(Cliente,Puerto) " + str(addr) + " Dato recibido "+ a + " Resultado "+ str(resultado) +"Horainicio" +str(horadeinicio) +"Horafinal"+str(horafinal)+"tiempotranscurrido "+str(tiempo_ejecucion)+"\n"
	f.write(escritura)
	f.close()
	mutex.release()
	
	connection.close()
		

	

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_address = ('192.168.8.138', 9400)
server_address = ('localhost', 9015)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(50)
while True:
	try:
		connection, client_address = sock.accept()
		tiempo_inicial = time.time() 
 		horadeinicio = time.strftime("%H") +":"+ time.strftime("%M") +":"+ time.strftime("%S")
		hilow = threading.Thread(target=hilo, args=(connection,client_address, tiempo_inicial,horadeinicio))
		hilow.start()
	except:
		connection.close()	
		#pass




