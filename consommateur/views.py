import json
import random

import pika
from django.shortcuts import render

from .broker.rabbitmq.publisher import RabbitMqPublisher
from .models import Consommateur
from django.http import HttpResponseRedirect

from .serializers import ConsommateurSerializer


def publish(request):
    if request.method == 'POST':
        consommateur_id = random.randint(1000, 9999)
        bio = request.POST['bio'] == 'true'
        local = request.POST['local'] == 'true'
        sans_gluten = request.POST['sans_gluten'] == 'true'
        vegetarien = request.POST['vegetarien'] == 'true'
        vegetalien = request.POST['vegetalien'] == 'true'
        produit1 = request.POST['produit1']
        avis1 = request.POST['avis1']
        evaluation1 = request.POST['evaluation1']
        date_evaluation1 = request.POST['date_evaluation1']
        produit2 = request.POST['produit2']
        avis2 = request.POST['avis2']
        evaluation2 = request.POST['evaluation2']
        date_evaluation2 = request.POST['date_evaluation2']
        produit_demande1 = request.POST['produit_demande1']
        motif_demande1 = request.POST['motif_demande1']
        produit_demande2 = request.POST['produit_demande2']
        motif_demande2 = request.POST['motif_demande2']

        consommateur = Consommateur.objects.create(
            consommateur_id=consommateur_id,
            bio=bio,
            local=local,
            sans_gluten=sans_gluten,
            vegetarien=vegetarien,
            vegetalien=vegetalien,
            produit1=produit1,
            avis1=avis1,
            evaluation1=evaluation1,
            date_evaluation1=date_evaluation1,
            produit2=produit2,
            avis2=avis2,
            evaluation2=evaluation2,
            date_evaluation2=date_evaluation2,
            produit_demande1=produit_demande1,
            motif_demande1=motif_demande1,
            produit_demande2=produit_demande2,
            motif_demande2=motif_demande2
        )

        data = ConsommateurSerializer(consommateur).data
        publisher = RabbitMqPublisher()
        publisher.publish(json.dumps(data))

        return HttpResponseRedirect(request.path)
    else:
        return render(request, 'consommateur_publish.html')


def receive(request):
    def callback(ch, method, properties, body):
        data = json.loads(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    credentials = pika.PlainCredentials('cansa', 'cansa')
    parameters = pika.ConnectionParameters('192.168.43.254', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    queue_name = 'consommateur'
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)
    channel.start_consuming()
    return render(request, 'consommateur_receive.html')
