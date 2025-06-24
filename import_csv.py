import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back.settings')
django.setup()

from electeurs.models import Electeur, Arrondissement  # Ajoute Arrondissement ici
from django.db import IntegrityError

# Étape 1 : Création des arrondissements par défaut
romains = ['I', 'II', 'III', 'IV', 'V', 'VI']
for i, numero in enumerate(romains, start=1):
    Arrondissement.objects.get_or_create(
        id=i,
        defaults={
            'NumeroArrondissement': numero,
            'NombreElecteursInscrits': 0
        }
    )

# Étape 2 : Import des électeurs
with open('data/electeurs_electeur.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            Electeur.objects.create(
                Nom=row['Nom'],
                Prenom=row['Prenom'],
                DateNaissance=row['DateNaissance'],
                LieuNaissance=row['LieuNaissance'],
                NumCIN=row['NumCIN'],
                Adresse=row['Adresse'],
                Profession=row['Profession'],
                Email=row['Email'],
                Image=row['Image'],
                NumeroTel=row['NumeroTel'],
                IdArrondissement_id=row['IdArrondissement_id'],
            )
        except IntegrityError:
            print(f"❌ Erreur d'intégrité pour l'email : {row['Email']} (probablement un doublon)")

print("✅ Import terminé")
