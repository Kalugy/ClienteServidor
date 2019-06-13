#!/usr/bin/env pythons
import pika
import uuid

from threading import Thread, Lock
import threading
class FibonacciRpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare('', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=n)
        while self.response is None:
            self.connection.process_data_events()
        return float(self.response)

    def run(self):
        print ("LOL")
        response=self.call("/|5|4")
        print (" [.] Got %r" % response)




NUM_HILOS = 3

for num_hilo in range(NUM_HILOS):
    #hilo1 = threading.Thread(name='hilo%s' %num_hilo, target=hilo)    
    #hilo1.start()

    #div_rpc = threading.Thread(name='FibonacciRpcClient%s' %num_hilo, target=FibonacciRpcClient)    
    #print(" [x] Requesting /|5|4")
    #div_rpc.start()
    #print(" [.] Got %r" % response)

    mihilo=FibonacciRpcClient()
    
    div_rpc = threading.Thread(name='mihilo%s' %num_hilo, target=mihilo.run())    
    div_rpc.start()

    #client.start() # The server is now running
    #hilow = threading.Thread(target=hilo, args=(connection,client_address))

    #hilow.start()
    #hilow.destroy()
    #sock.close()
#hilo1.join()
print("termino")
div_rpc.join()   
