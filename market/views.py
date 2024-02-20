from django.shortcuts import render
from django.http import HttpResponseRedirect

from market.models import Market


def publish(request):
    if request.method == 'POST':
        produit = request.POST['produit']
        date = request.POST['date']
        prix_moyen = request.POST['prix']
        tendance = request.POST['tendance']
        source = request.POST['source']
        produits = request.POST['produits']
        dates = request.POST['dates']
        quantite_disponible = request.POST['quantite_disponible']
        offres_speciales = request.POST['offres_speciales']
        mois_precedent = request.POST['mois_precedent']
        mois_actuel = request.POST['mois_actuel']
        unite_quantite = request.POST['unite_quantite']
        sources = request.POST['sources']
        produit2 = request.POST['produit2']
        date2 = request.POST['date2']
        niveau_actuel = request.POST['niveau_actuel']
        prevision = request.POST['prevision']
        source2 = request.POST['source2']

        # Create a new MarketData object and save it to the database
        Market.objects.create(
            produit=produit,
            date=date,
            prix_moyen=prix_moyen,
            tendance=tendance,
            source=source,
            produits=produits,
            dates=dates,
            quantite_disponible=quantite_disponible,
            offres_speciales=offres_speciales,
            mois_precedent=mois_precedent,
            mois_actuel=mois_actuel,
            unite_quantite=unite_quantite,
            sources=sources,
            produit2=produit2,
            date2=date2,
            niveau_actuel=niveau_actuel,
            prevision=prevision,
            source2=source2
        )

        # Redirect the user to a success page
        return HttpResponseRedirect(request.path)

    else:
        # Render the form
        return render(request, 'market_publish.html')


def receive(request):
    return render(request, 'market_receive.html')