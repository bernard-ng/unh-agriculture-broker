from django.shortcuts import render
from django.http import HttpResponseRedirect

from transporteur.models import Transporteur


def publish(request):
    if request.method == 'POST':
        produit = request.POST.get('produit')
        date = request.POST['date']
        horaires_livraison = request.POST['horaires_livraison']
        conditions_stockage = request.POST['conditions_stockage']
        route = request.POST['route']
        train = request.POST['train']
        mer = request.POST['mer']
        air = request.POST['air']
        source = request.POST['source']
        capacite_disponible = request.POST['capacite_disponible']
        types_vehicules = request.POST['types_vehicules']
        itineraire = request.POST['itineraire']
        transporteur = request.POST['transporteur']
        date1 = request.POST['date1']
        num_cargaison_1 = request.POST['num_cargaison_1']
        avancement_1 = request.POST['avancement_1']
        delai_livraison_1 = request.POST['delai_livraison_1']
        retard = request.POST['retard'] == 'true'
        num_cargaison_3 = request.POST['num_cargaison_3']
        avancement_3 = request.POST['avancement_3']
        delai_livraison_3 = request.POST['delai_livraison_3']
        retards = request.POST['retards'] == 'true'
        source1 = request.POST['source1']

        Transporteur.objects.create(
            produit=produit,
            date=date,
            horaires_livraison=horaires_livraison,
            conditions_stockage=conditions_stockage,
            route=route,
            train=train,
            mer=mer,
            air=air,
            source=source,
            capacite_disponible=capacite_disponible,
            types_vehicules=types_vehicules,
            itineraire=itineraire,
            transporteur=transporteur,
            date1=date1,
            num_cargaison_1=num_cargaison_1,
            avancement_1=avancement_1,
            delai_livraison_1=delai_livraison_1,
            retard=retard,
            num_cargaison_3=num_cargaison_3,
            avancement_3=avancement_3,
            delai_livraison_3=delai_livraison_3,
            retards=retards,
            source1=source1
        )

        return HttpResponseRedirect(request.path)
    else:
        return render(request, 'transporteur_publish.html')


def receive(request):
    return render(request, 'transporteur_receive.html')