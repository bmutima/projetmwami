from django.db import models


# Create your models here.

class Categorie(models.Model):
    codecat = models.CharField(max_length=10,primary_key=True)
    libcat = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.libcat




class Produit(models.Model):
    codeprod = models.CharField(max_length=10,primary_key=True)
    libprod = models.CharField(max_length=100,null=False)
    qte = models.IntegerField(null=False)
    pu = models.DecimalField(max_digits=5,decimal_places=2)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)

    def __str__(self):
        return self.libprod

    
   
