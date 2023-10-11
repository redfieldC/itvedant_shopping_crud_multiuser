from django.shortcuts import render,redirect,HttpResponse
from .models import *
# Create your views here.
def homepage(request):
    return HttpResponse("Hi welcome to productapp")

def add_product(request):
    if request.method == 'GET':
        return render(request,"product/store_product.html")
    else:
        name = request.POST['pname']
        amt = request.POST['price']
        qty = request.POST['qty']
        cat = request.POST['cat']
        is_avail = request.POST['avail']
        product = Product.objects.create(name=name,price=amt,qty=qty,cat=cat,is_available=is_avail)
        print("PRODUCT--------->", product)
        product.save()
        return redirect("/productapp/productdash")
    

def product_dashboard(request):
    products = Product.objects.all()
    for product in products:
        print("****************")
        print()
        print("Product name: ",product.name)
        print("Product Quantity: ",product.qty)
        print("Product Cost: ",product.price)
        print("Product Category: ",product.cat)
        print("Product Is Available?: ",product.is_available)
        print()
        print("****************")
    context = {'products':products}
    return render(request,'product/dashboard.html',context)


def delete_product(request,pid):
    product = Product.objects.filter(id=pid)
    print("OProduct to be delete ---------> ",product)
    product.delete()
    return redirect('/productapp/productdash')

def update_product(request,pid):
    products = Product.objects.filter(id=pid)
    if request.method == 'GET':
        products = Product.objects.filter(id=pid)
        context  = {}
        context['products'] = products
        return render(request,'product/editproduct.html',context)
    
    else:
        uname = request.POST['pname']
        uprice = request.POST['price']
        uqty = request.POST['qty']
        ucat = request.POST['cat']
        uavail = request.POST['avail']
        
        products.update(name=uname,price=uprice,qty=uqty,cat=ucat,is_available=uavail)
        return redirect('/productapp/productdash')