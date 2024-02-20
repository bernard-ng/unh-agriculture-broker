from django.shortcuts import render

from .broker.mqtt.publisher import Publisher
from .models import Agriculteur
from django.http import HttpResponseRedirect
import random
import string
import json
from datetime import datetime

from .serializers import AgriculteurSerializer


def capteur():
    random_chars = ''.join(random.choices(string.ascii_letters, k=3))
    random_int = random.randint(1, 1000)
    id_capteur = f"{random_chars}{random_int}".upper()
    latitude = round(random.uniform(-90.0, 90.0), 2)
    longitude = round(random.uniform(-180.0, 180.0), 2)
    timestamp = datetime.now()
    mesures = {
        "humidite_sol": round(random.uniform(0.0, 100.0), 2),
        "temperature": round(random.uniform(-20.0, 50.0), 2),
        "humidite_air": round(random.uniform(0.0, 100.0), 2),
    }

    chars = ''.join(random.choices(string.ascii_letters, k=3))
    agriculteur_id = f"{chars}{random_int}".upper()

    data = {
        "id_capteur": id_capteur,
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": str(timestamp),
        "mesures": mesures,
        "agriculteur_id": agriculteur_id
    }

    return json.dumps(data)


def receive(request):
    return render(request, 'agriculteur_receive.html')


def publish(request):
    if request.method == 'POST':
        sensor_data = capteur()
        parcelle_id = request.POST['informations[parcelle_id]']
        culture = request.POST['informations[culture]']
        variete = request.POST['informations[variete]']
        date_plantation = request.POST['informations[date_plantation]']
        technique_type = request.POST['informations[techniques_culturales][type]']
        fertilization = request.POST['informations[techniques_culturales][fertilisation]']
        irrigation = request.POST['informations[techniques_culturales][irrigation]']
        phytopathological_treatments = request.POST['traitements_phytosanitaires[]']
        rendement_attendu_valeur = request.POST['rendement_attendu_valeur']
        rendement_attendu_unite = request.POST['rendement_attendu_unite']
        farmer_id = request.POST['agriculteur_id']
        culture_stats = request.POST['culture']
        annee = request.POST['annee']
        zone_production = request.POST['zone_production[]']
        quantite_recoltee = request.POST['quantite_recoltee[]']
        unite_quantite = request.POST['unite_quantite[]']
        periode_recolte_debut = request.POST['periode_recolte_debut[]']
        periode_recolte_fin = request.POST['periode_recolte_fin[]']
        agriculteur = Agriculteur.objects.create(sensor_data=sensor_data, parcelle_id=parcelle_id, culture=culture,
                                                        variete=variete,
                                                        date_plantation=date_plantation, technique_type=technique_type,
                                                        fertilization=fertilization,
                                                        irrigation=irrigation,
                                                        phytopathological_treatments=phytopathological_treatments,
                                                        rendement_attendu_valeur=rendement_attendu_valeur,
                                                        rendement_attendu_unite=rendement_attendu_unite, farmer_id=farmer_id,
                                                        culture_stats=culture_stats, annee=annee,
                                                        zone_production=zone_production,
                                                        quantite_recoltee=quantite_recoltee, unite_quantite=unite_quantite,
                                                        periode_recolte_debut=periode_recolte_debut,
                                                        periode_recolte_fin=periode_recolte_fin)

        # envoyer les donnees au broker

        data = AgriculteurSerializer(agriculteur).data
        publisher = Publisher()
        publisher.publish(json.dumps(data))

        return HttpResponseRedirect(request.path)
    else:
        json_data = capteur()
        return render(request, 'agriculteur_publish.html', {'json_data': json_data})
