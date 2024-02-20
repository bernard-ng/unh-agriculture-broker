from django.shortcuts import render
from django.http import HttpResponseRedirect
import random
import json
from datetime import datetime

from laboratoire.models import Laboratoire


def meteo():
    timestamp = datetime.now()
    latitude = round(random.uniform(-90, 90), 2)
    longitude = round(random.uniform(-180, 180), 2)
    temperature_actuelle = round(random.uniform(-40, 40), 2)
    temperature_ressentie = round(random.uniform(temperature_actuelle - 10, temperature_actuelle + 10), 2)
    intensite_precipitations = ["Legere", "Moderee", "Forte"]
    intensite_precipitations = random.choice(intensite_precipitations)
    probabilite_precipitations = round(random.uniform(0, 100), 2)
    vitesse_vent = round(random.uniform(0, 100), 2)
    directions_vent = ["Nord", "Est", "Sud", "Ouest"]
    direction_vent = random.choice(directions_vent)
    data = {
        "date": str(timestamp),
        "localisation": {
            "latitude": latitude,
            "longitude": longitude
        },
        "previsions_meteo": {
            "temperature": {
                "actuelle": temperature_actuelle,
                "ressentie": temperature_ressentie,
                "unite": "°C"
            },
            "precipitations": {
                "intensite": intensite_precipitations,
                "probabilite": probabilite_precipitations,
                "unite": "%"
            },
            "vent": {
                "vitesse": vitesse_vent,
                "direction": direction_vent,
                "unite_vitesse": "km/h"
            }
        }
    }

    json_data = json.dumps(data, ensure_ascii=False)
    return json_data


def publish(request):
    if request.method == 'POST':
        id_lab = request.POST['id_lab']
        prevision_meteo = meteo()
        Laboratoire.objects.create(id_lab=id_lab, prevision_meteo=prevision_meteo)
        return HttpResponseRedirect(request.path)
    else:
        json_data = meteo()
        return render(request, 'laboratoire_publish.html', {'json_data': json_data})


def receive(request):
    return render(request, 'laboratoire_receive.html')
