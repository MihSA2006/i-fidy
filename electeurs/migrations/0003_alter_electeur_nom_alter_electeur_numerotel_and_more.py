# Generated by Django 5.2.3 on 2025-06-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electeurs', '0002_alter_electeur_numcin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electeur',
            name='Nom',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='electeur',
            name='NumeroTel',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='electeur',
            name='Prenom',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='electeur',
            name='Profession',
            field=models.CharField(max_length=225),
        ),
    ]
