from rest_framework import serializers
from .models import Electeur, Arrondissement

class ArrondissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrondissement
        fields = '__all__'

class ElecteurSerializer(serializers.ModelSerializer):
    NumCIN = serializers.CharField(write_only=True)

    class Meta:
        model = Electeur
        fields = [
            'id', 'Nom', 'Prenom', 'DateNaissance', 'LieuNaissance',
            'NumCIN', 'Adresse', 'IdArrondissement', 'Profession',
            'Email', 'Image', 'NumeroTel'
        ]