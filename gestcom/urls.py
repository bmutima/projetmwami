"""
URL configuration for gestcom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_gestcom.views import home,CategorieInfo,CategorieDetails,updateProduit,deleteProduit,modifierProduit,addProduit,categorie,ajouterCategorie,addCategorie,deleteCategorie,modifierCategorie,updateCategorie,produit,ajouterProduit

urlpatterns =[
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('categorie/',categorie, name="categorie"),
    path('ajouterCategorie/',ajouterCategorie, name="ajouterCategorie"),
    path('addCategorie/',addCategorie, name="addCategorie"),
    path('deleteCategorie<str:id>/',deleteCategorie, name="deleteCategorie"),
    path('modifierCategorie<str:id>/',modifierCategorie, name="modifierCategorie"),
    path('updateCategorie<str:id>/',updateCategorie, name="updateCategorie"),
    path('updateProduit<str:id>/',updateProduit, name="updateProduit"),

    path('categorieapi/',CategorieDetails.as_view(), name="categorieapi"),
    path("categorieapi/<str:id>/",CategorieInfo.as_view(),name="categorieapi"),

    path('produit/',produit, name="produit"),
    path('ajouterProduit/',ajouterProduit, name="ajouterProduit"),
    path('addProduit/',addProduit, name="addProduit"),
    path('deleteProduit<str:id>/',deleteProduit, name="deleteProduit"),
    path('modifierProduit<str:id>/',modifierProduit, name="modifierProduit"),

    #path('produitapi/',ProduitDetails.as_view(), name="produitapi"),
    #path("produitapi/<str:id>/",ProduitInfo.as_view(),name="produitapi"),

    
]
