#!/usr/bin/env python
import pika
import time

from threading import Thread, Lock
mutex = Lock()


connection = pika.BlockingConnection(
pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def div(n):
    #print(" [x] %r" % n)
    a=[]
    a=str(n)
    #print (a)
    datos1=a.split("'")
    #print (datos1)
    datos=datos1[1].split("|")
    
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
    return a
    #connection.send(a)



def on_request(ch, method, props, body):
    n = str(body)

    tiempo_inicial = time.time() 
    horadeinicio = time.strftime("%H") +":"+ time.strftime("%M") +":"+ time.strftime("%S")

    #print(" [.] fib(%s)" % n)
    response = div(n)

    horafinal = time.strftime("%H") +":"+ time.strftime("%M") +":"+ time.strftime("%S")
    tiempo_final = time.time() 
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    
    mutex.acquire()

    f = open ('log.txt','a')
    escritura="Dato recibido "+ str(n) + " Resultado "+  str(response) +"Horainicio" +str(horadeinicio) +"Horafinal"+str(horafinal)+"tiempotranscurrido "+str(tiempo_ejecucion)+"\n"
    f.write(escritura)
    f.close()
    mutex.release()
    #time.sleep(10)


    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()