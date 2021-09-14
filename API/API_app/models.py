from django.db import models


# Create your models here.

class Utilisateurs(models.Model):
    UtilisateurID = models.AutoField(primary_key=True)
    UtilisateurNom = models.CharField(max_length=100)
    UtilisateurEmail = models.EmailField(max_length=200)


class Phrase(models.Model):
    PhraseID = models.AutoField(primary_key=True)
