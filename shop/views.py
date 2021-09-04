from django.shortcuts import render
from .models import Product,Contact
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(catprods)
    print(cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        print("#################$$$$$$$$$$-------Prod!!!!!!!!!!!!!!!!!!!!!!!!!################")
        print(prod)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        print(nSlides)
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----All Prods!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(allProds)
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request,myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request,"shop/prod_view.html",{'product':product[0]})

def checkOut(request):
    return HttpResponse("We are at checkout")
