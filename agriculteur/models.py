from django.db import models


class Agriculteur(models.Model):
    sensor_data = models.TextField()
    parcelle_id = models.CharField(max_length=100)
    culture = models.CharField(max_length=100)
    variete = models.CharField(max_length=100)
    date_plantation = models.DateField()
    technique_type = models.CharField(max_length=100)
    fertilization = models.CharField(max_length=100)
    irrigation = models.CharField(max_length=100)
    phytopathological_treatments = models.TextField()
    rendement_attendu_valeur = models.FloatField()
    rendement_attendu_unite = models.CharField(max_length=100)
    farmer_id = models.CharField(max_length=100)
    culture_stats = models.TextField()
    annee = models.IntegerField()
    zone_production = models.TextField()
    quantite_recoltee = models.FloatField()
    unite_quantite = models.CharField(max_length=100)
    periode_recolte_debut = models.DateField()
    periode_recolte_fin = models.DateField()

    class Meta:
        db_table = 'agriculteur'

