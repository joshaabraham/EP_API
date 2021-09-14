from rest_framework import serializers
from models import Utilisateurs, Phrase


class UtilisateursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateurs
        fields = ('UtilisateurID',
                  'UtilisateurNom',
                  'UtilisateurEmail')


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ('PhraseID')