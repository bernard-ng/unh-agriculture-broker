from django.db import models


class Market(models.Model):
    produit = models.CharField(max_length=50)
    date = models.DateField()
    prix_moyen = models.DecimalField(max_digits=10, decimal_places=2)
    tendance = models.CharField(max_length=50)
    source = models.CharField(max_length=100)

    # Fields for Disponibilite des produits
    produits = models.CharField(max_length=50)
    dates = models.DateField()
    quantite_disponible = models.IntegerField()
    offres_speciales = models.CharField(max_length=200)
    mois_precedent = models.IntegerField()
    mois_actuel = models.IntegerField()
    unite_quantite = models.CharField(max_length=50)
    sources = models.CharField(max_length=100)

    # Fields for Demande du marche
    produit2 = models.CharField(max_length=50)
    date2 = models.DateField()
    niveau_actuel = models.CharField(max_length=50)
    prevision = models.CharField(max_length=50)
    source2 = models.CharField(max_length=100)

    class Meta:
        db_table = 'market'
