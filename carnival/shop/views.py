from math import ceil, prod
from re import A
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import  Product,Contact


def index (request):
    
    # products = Product.objects.all()
    # print(products)
#sending the parameters to index.html
    # params = {'no_of_slides' : nSlides ,'range' : range(1,nSlides),'product' : products}
    # allProds = [[products, range(1,nSlides), nSlides],
    #                    [products, range(1,nSlides), nSlides]]   
    allProds = []    
    catProds = Product.objects.values('category', 'id')
    cats ={item['category'] for item in catProds}
    for cat in cats :
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n //4 + ceil ((n/4) - (n//4))
        allProds.append([prod,range(1,nSlides), nSlides])

    params = {'allProds' : allProds}
    return render (request,'shop/index.html',params)



def about (request):
    return render(request,"shop/about.html")

def contact (request):
    if(request.method=='POST'):

        # fetch the data of user 
        name = request.POST.get('name', ' ')   
        email = request.POST.get('email', ' ')
        phone = request.POST.get('phone', ' ')
        desc = request.POST.get('desc', ' ')
        print(name,email,phone,desc)

        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"shop/contact.html")

def tracker (request):
    return render(request,"shop/tracker.html")

def search (request):
    return render(request,"shop/search.html")

def productview (request,myid):
    # fetch the product using id 
    product = Product.objects.filter(id=myid)
    # print(product)
    params = {'product' : product[0]}
    return render(request,"shop/prodView.html",params)

def chekout (request):
    return render(request,"shop/checkout.html")
