from django.contrib import admin
from .models import Categorie,Produit
# Register your models here.

admin.site.register(Categorie,list_diplay=['codecat','libcat'])
admin.site.register(Produit,list_display=['codeprod','libprod','pu'])
