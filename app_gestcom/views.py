from django.shortcuts import render
from app_gestcom.models import Categorie,Produit
from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import CategorieSerializer
from django.core.paginator import Paginator

# Create your views here.

def home(request):

    nrcategorie = Categorie.objects.all().count()
    nbrproduit = Produit.objects.all().count()

    ctx = {
         'nrcategorie':nrcategorie,
         'nbrproduit':nbrproduit
        
    }
    
    return render(request,'home.html',ctx)

def categorie(request):
    if request.method == "POST":
        rech = request.POST['rech']
        cat = Paginator(Categorie.objects.filter(codecat__contains=rech) |
        Categorie.objects.filter(libcat__contains=rech),20)
        page = request.GET.get('page')
        pages =cat.get_page(page)
        compte = len(pages)
        if rech == '':
             compte = len(Categorie.objects.all())      
    else:
        cat = Paginator(Categorie.objects.all(), 20)
        page = request.GET.get('page')
        pages =cat.get_page(page)
        
        compte = len(Categorie.objects.all())
    
    cxt = {
        'cat' : pages,
        'compte' : compte
    }
    

    return render(request,'categorie.html',cxt)


def ajouterCategorie(request):

    return render(request,'ajouterCategorie.html')




def addCategorie(request):
    message = None
    if request.method == 'POST':
        codecat = request.POST["code"]
        libcat = request.POST["libelle"]

        rs_cat = Categorie.objects.filter(codecat=codecat)

        if len(rs_cat)>0:
            message = "Ce code categorie existe"
        else:
            cates = Categorie(
                
                codecat = codecat,
                libcat = libcat,
            )

            cates.save()
            message = "categorie enregistrée avec succes"

    ctx = {
        'message': message
    }
    return render(request,'ajouterCategorie.html',ctx)

def deleteCategorie(request,id):
    cat = Categorie.objects.get(pk=id)
    cat.delete()

    return redirect('/categorie/')

def deleteProduit(request,id):
    pr = Produit.objects.get(pk=id)
    pr.delete()

    return redirect('/produit/')

def modifierCategorie(request,id):
    c = Categorie.objects.get(pk=id)

    ctx= {
        'c':c
    }
    return render(request,'modifierCategorie.html',ctx)


def modifierProduit(request,id):
    p = Produit.objects.get(pk=id)

    ctx= {
        'p':p
    }
    return render(request,'modifierProduit.html',ctx)


def updateCategorie(request,id):
    c = Categorie.objects.get(pk = id)
    lib = request.POST["libelle"]
    

    c.libcat = lib

        #print(f.intfrais,f.montant,f.codefrais)
    c.save()
    return redirect('/categorie/')



def updateProduit(request,id):
    p = Produit.objects.get(pk = id)
    lib = request.POST["libelle"]
    prix = request.POST["pu"]
    quantite = request.POST["qte"]

    
    p.libprod = lib
    p.pu = prix
    p.qte = quantite


    

        #print(f.intfrais,f.montant,f.codefrais)
    p.save()
    return redirect('/produit/')

#view produit

def produit(request):

    pr = Paginator(Produit.objects.all(),2)
    page = request.GET.get('page')
    pages = pr.get_page(page)
    compte = Produit.objects.all().count()
    
    cxt = {
        'pr' : pages,
        'compte' : compte
    }
    

    return render(request,'produit.html',cxt)


def ajouterProduit(request):

    cats = Categorie.objects.all()

    ctx ={
        'cats': cats

    }
    
    return render(request,'ajouterProduit.html',ctx)




def addProduit(request):
    message = None
    if request.method == 'POST':
        code = request.POST["code"]
        libcat = request.POST["libelle"]
        qte = request.POST["qte"]
        pu = request.POST["pu"]
        categorie = request.POST["categorie"]

        rs_pr = Produit.objects.filter(codeprod=code)
        cat = Categorie.objects.get(codecat=categorie)

        if len(rs_pr)>0:
            message = "Ce code produit existe"
        else:
            prod = Produit(  
                codeprod = code,
                libprod = libcat,
                pu = pu,
                qte = qte,
                categorie = cat,
            )

            prod.save()
            message = "produit enregistré avec succes"
            return redirect('/produit/')

    ctx = {
        'message': message
    }
    return render(request,'ajouterProduit.html',ctx)

class CategorieDetails(APIView):
    def get(self,request):
        obj = Categorie.objects.all()
        serializer = CategorieSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = CategorieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)


class CategorieInfo(APIView):
    
    def get(self,request,id):
        try:
            obj = Categorie.objects.get(pk=id)
        except:
            msg={"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorieSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            obj = Categorie.objects.get(pk=id)
            
        except Categorie.DoesNotExist:
            msg={"msg":"not found error"}
            
            return Response(msg, status = status.HTTP_404_NOT_FOUND)
        
        serializer = CategorieSerialiser(obj,data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        try:
            obj = Categorie.objects.get(pk=id)
            
        except Categorie.DoesNotExist:
            msg={"msg":"not found error"}
            
            return Response(msg, status = status.HTTP_404_NOT_FOUND)
        
        serializer = CategorieSerializer(obj,data = request.data,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            obj = Categorie.objects.get(pk=id)
        
        except Categorie.DoesNotExist:
            msg = {"msg":"not found"}
            
            return Response(msg, status = status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
    
    


