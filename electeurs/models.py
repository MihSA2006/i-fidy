from django.db import models
from django.contrib.auth.hashers import make_password

class Arrondissement(models.Model):
    NumeroArrondissement = models.CharField(max_length=50, unique=True)
    NombreElecteursInscrits = models.IntegerField(default=0)

    def __str__(self):
        return f"Arrondissement {self.NumeroArrondissement}"

class Electeur(models.Model):
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    DateNaissance = models.DateField()
    LieuNaissance = models.CharField(max_length=100)
    NumCIN = models.CharField(max_length=50, unique=True)
    Adresse = models.TextField()
    IdArrondissement = models.ForeignKey(
        Arrondissement, 
        on_delete=models.CASCADE,
        related_name='electeurs'
    )
    Profession = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Image = models.ImageField(upload_to='electeurs/images/', null=True, blank=True)
    NumeroTel = models.CharField(max_length=20)

    from django.contrib.auth.hashers import make_password

    def save(self, *args, **kwargs):
        # Si c'est une nouvelle instance (pas encore d'ID) ou CIN changé
        if not self.pk or Electeur.objects.get(pk=self.pk).NumCIN != self.NumCIN:
            self.NumCIN = make_password(self.NumCIN)

        # Surcharge pour mise à jour compteur
        if not self.pk:
            super().save(*args, **kwargs)
            self.IdArrondissement.NombreElecteursInscrits += 1
            self.IdArrondissement.save()
        else:
            super().save(*args, **kwargs)

    
    def delete(self, *args, **kwargs):
        """Surcharge de la méthode delete pour décrémenter le compteur"""
        self.IdArrondissement.NombreElecteursInscrits -= 1
        self.IdArrondissement.save()
        super().delete(*args, **kwargs)

    def change_arrondissement(self, new_arrondissement):
        """Change l'arrondissement d'un électeur et met à jour les compteurs"""
        if self.IdArrondissement != new_arrondissement:
            # Décrémente l'ancien arrondissement
            self.IdArrondissement.NombreElecteursInscrits -= 1
            self.IdArrondissement.save()
            
            # Met à jour et incrémente le nouveau
            self.IdArrondissement = new_arrondissement
            self.save()  # Cela déclenchera la méthode save() qui incrémente
            
            # Alternative sans double incrément:
            # self.IdArrondissement.NombreElecteursInscrits += 1
            # self.IdArrondissement.save()
            # super().save()

    def __str__(self):
        return f"{self.Prenom} {self.Nom} ({self.NumCIN})"

    class Meta:
        verbose_name = "Électeur"
        verbose_name_plural = "Électeurs"