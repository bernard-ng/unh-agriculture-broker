from django.db import models


class Consommateur(models.Model):
    consommateur_id = models.CharField(max_length=200, unique=True)
    bio = models.BooleanField(default=False)
    local = models.BooleanField(default=False)
    sans_gluten = models.BooleanField(default=False)
    vegetarien = models.BooleanField(default=False)
    vegetalien = models.BooleanField(default=False)
    produit1 = models.CharField(max_length=200)
    avis1 = models.TextField()
    evaluation1 = models.IntegerField()
    date_evaluation1 = models.DateField()
    produit2 = models.CharField(max_length=200)
    avis2 = models.TextField()
    evaluation2 = models.IntegerField()
    date_evaluation2 = models.DateField()
    produit_demande1 = models.CharField(max_length=200)
    motif_demande1 = models.TextField()
    produit_demande2 = models.CharField(max_length=200)
    motif_demande2 = models.TextField()

    class Meta:
        db_table = 'consommateur'
