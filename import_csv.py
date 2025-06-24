# import_csv.py

import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back.settings')  # Remplace 'back' par ton nom de projet
django.setup()

from electeurs.models import Electeur  # Assure-toi que ce modèle est correct

with open('data/electeurs_electeur.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
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

print("✅ Import terminé")
