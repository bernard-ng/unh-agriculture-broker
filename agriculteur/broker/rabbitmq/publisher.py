import pika
import json
import time


class RabbitMqPublisher:
    def __init__(self):
        credentials = pika.PlainCredentials('cansa', 'cansa')
        parameters = pika.ConnectionParameters('192.168.43.208', 5672, '/', credentials)
        connection = pika.BlockingConnection(parameters)
        self.channel = connection.channel()

        # Déclaration d'une queue durable
        self.queue_name = 'agriculteur'
        self.channel.queue_declare(queue=self.queue_name, durable=True)

    def __del__(self):
        self.channel.close()

    def publish(self, data):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=data,
            properties=pika.BasicProperties(
                delivery_mode=2,  # Rend le message durable
            )
        )
