from django.db import models


class Transporteur(models.Model):
    produit = models.CharField(max_length=255)
    date = models.DateField()
    horaires_livraison = models.CharField(max_length=255)
    conditions_stockage = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    train = models.CharField(max_length=255)
    mer = models.CharField(max_length=255)
    air = models.CharField(max_length=255)
    source = models.CharField(max_length=255, default="Service Logistique Agricole")
    capacite_disponible = models.IntegerField()
    types_vehicules = models.CharField(max_length=255)
    itineraire = models.CharField(max_length=255)
    transporteur = models.CharField(max_length=255)
    date1 = models.DateField()
    num_cargaison_1 = models.CharField(max_length=255)
    avancement_1 = models.CharField(max_length=255)
    delai_livraison_1 = models.DateField()
    retard = models.BooleanField(default=False)
    num_cargaison_3 = models.CharField(max_length=255)
    avancement_3 = models.CharField(max_length=255)
    delai_livraison_3 = models.DateField()
    retards = models.BooleanField(default=False)
    source1 = models.CharField(max_length=255, default="Suivi de Livraison")

    class Meta:
        db_table = 'transporteur'
