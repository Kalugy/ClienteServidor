#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
	print(" [x] %r" % body)
	a=[]
	a=str(body)
	print (a)
	datos1=a.split("'")
	print (datos1)
	datos=datos1[1].split("|")
	print(datos)
	
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
	#a=str(resultado)
	#connection.send(a)
	

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()