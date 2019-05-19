----------------------------------------



from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time
import math
import sys
#import thread
from multiprocessing import Process
from threading import Thread, Lock
mutex = Lock()

class MyFuncs:

    def dividir(self, x, y):

        time.sleep(10)
        return float(x) / float(y)
    """    
    def suma(self, x, y):
        return float(x) + float(y)
    def resta(self, x, y):
        return float(x) - float(y)
    def multiplicar(self, x, y):
        return float(x) * float(y)

    def potencia(self, x, y):
        return float(x) ** float(y)
    def radicacion(self, x, y):
        return math.pow(float(x), float(y))
    def logaritmo(self, x, y):
        return math.log(float(x), float(y))
    """

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self):
         threading.Thread.__init__(self)
         self.localServer = SimpleThreadedXMLRPCServer(("localhost",10056))
         
         self.localServer.register_instance(MyFuncs())

    def run(self):
         self.localServer.serve_forever()

server = ServerThread()
server.start() # The server is now running
print "Listo servidor."

class ClientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.s = xmlrpclib.ServerProxy('http://localhost:10056')

    def run(self):

        tiempo_inicial = time.time() 
        horadeinicio = time.strftime("%H") +":"+ time.strftime("%M") +":"+ time.strftime("%S")
        #time.sleep(3)
        print "Llamada cliente"
        self.fin=2
        while(self.fin!=1):

            """
            print 'Operaciones: \n - suma o "+" \n - resta o "-" \n - multiplicar o "*" \n - dividir o "/'
            print ' - potencia o "^" \n - logaritmo \n - radicacion \n - salir '
            self.num=raw_input("Ingrese la siguiente sintaxis: numero1 operacion numero2: ")
            palabra1=""
            palabra2=""
            palabra3=""
            cuenta=0
            contador=0
            #cuando cuantas veces esta un signo dentro de la palabra y las separa segun la cantidad de signos
            for carac in self.num:
                if carac == ' ':
                    cuenta+=1
                else:
                   contador+=1
                   if cuenta==0:
                       palabra1+=carac
                   if cuenta==1:
                       palabra2+=carac
                   if cuenta==2:
                       palabra3+=carac
            """
            palabra1=1066
            palabra3=469
            try:
                b= self.s.dividir(palabra1,palabra3)
                horafinal = time.strftime("%H") +":"+ time.strftime("%M") +":"+ time.strftime("%S")
                tiempo_final = time.time() 
                tiempo_ejecucion = tiempo_final - tiempo_inicial
                
                mutex.acquire()

                f = open ('log.txt','a')
                escritura="Dato recibido "+ str(palabra1)+"/" + str(palabra3) + " Resultado "+ str(b) +"Horainicio" +str(horadeinicio) +"Horafinal"+str(horafinal)+"tiempotranscurrido "+str(tiempo_ejecucion)+"\n"
                f.write(escritura)
                f.close()
                mutex.release()
                self.fin=1 
            except:   
                print ("ERROR")
                mutex.acquire()

                f = open ('log.txt','a')
                escritura="error" +"Dato recibido "+ str(palabra1)+"/" + str(palabra3) + " Resultado "+ str(b) +"Horainicio" +str(horadeinicio) +"Horafinal"+str(horafinal)+"tiempotranscurrido "+str(tiempo_ejecucion)+"\n"
                f.write(escritura)
                f.close()
                mutex.release()

              


            sys.exit()
            """    
            if(palabra2 == 'suma' or palabra2 == '+'):
                print self.s.suma(palabra1,palabra3)
            elif(palabra2 == 'resta' or palabra2 == '-'):
                print self.s.resta(palabra1,palabra3)

            elif(palabra2 == 'multiplicar' or palabra2 == '*'):
                print self.s.multiplicar(palabra1,palabra3)



            elif(palabra2 == 'potencia' or palabra2 == '^'):
                print self.s.potencia(palabra1,palabra3)

            elif(palabra2 == 'logaritmo'):
                print self.s.logaritmo(palabra1,palabra3)

            elif(palabra2 == 'radicacion'):
                print self.s.radicacion(palabra1,palabra3)

            """
                

NUM_HILOS = 500

for num_hilo in range(NUM_HILOS):
    #hilo1 = threading.Thread(name='hilo%s' %num_hilo, target=hilo)    
    #hilo1.start()
    client = ClientThread()
    client.start() # The server is now running
    #hilow = threading.Thread(target=hilo, args=(connection,client_address))

    #hilow.start()
    #hilow.destroy()
    #sock.close()
#hilo1.join()
print("termino")
client.join()   
