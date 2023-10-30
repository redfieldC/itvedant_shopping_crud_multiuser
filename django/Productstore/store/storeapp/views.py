from django.shortcuts import render,redirect,HttpResponse
from productapp.models import *
# Create your views here.
from django.db.models import Q 
from accounts.models import Cart


def cart(request):
    return render(request,'storeapp/cart.html')

def home(request):
    products = Product.objects.filter(is_available=True)
    return render(request,"storeapp/index.html",{"pdata":products})


def homepage(request):
    context = {"msg":"Hello all good morning"}
    context['x']=8000
    context['y']=8000
    context['number'] = [10,20,30,40,50,60,70,80,90,100]
    return render(request,'storeapp/home.html',context)


def cat_filter(request,catv):
    # pdata = Product.objects.filter(cat=catv,is_available=True)
    q1 = Q(cat=catv)
    q2 = Q(is_available=True)
    pdata = Product.objects.filter(q1 & q2)
    return render(request,"storeapp/index.html",{"pdata":pdata})

def price_filter(request):
    min = request.GET['min']
    max = request.GET['max']
    if int(min) < 0 or int(max) > 0:
        return  render(request,"storeapp/index.html",{"errmsg":"Price cannot be negative"})
    
    elif int(min) > int(max):
        return  render(request,"storeapp/index.html",{"errmsg":"Minimum price cannot be larger than maximum price"})
    else:
        min = int(min)
        max = int(max)
        q1 = Q(price__gte = min)
        q2 = Q(price__lte = max)
        q3 = Q(is_available = True)
        pdata = Product.objects.filter(q1 & q2 & q3)
        print(pdata)
        return render(request,"storeapp/index.html",{"pdata":pdata})
    

def pdetails(request,pid):
    p = Product.objects.get(id=pid)
    context = { 'product' : p }
    return render(request, 'ashstore/product_details.html', context)

    
def sort(request):
    qpara = request.GET['q']
    if qpara == 'asc':
        x='price'
    elif qpara == 'desc':
        x='-price'

    pdata = Product.objects.filter(is_available=True).order_by(x)
    return render(request,"storeapp/index.html",{"pdata":pdata})

def search(request):
    x = request.GET['search']
    q1 = Q(name__icontains=x)
    q2 = Q(pdetails__icontains=x)
    pdata = Product.objects.filter(q1 | q2)
    return render(request,"storeapp/index.html",{"pdata":pdata})


def contact(request):
    return HttpResponse("<h1>Welcome to ContactPage</h1>")

def edit(request,id):
    return HttpResponse("Welcome to Edit page " + id)

def delete(request,id):
    return HttpResponse("Welcome to delete page " + id)

def addition(request,x,y):
    result = int(x) + int(y)
    return HttpResponse("RESULT: " + str(result))


def remove_cart(request,cid):
    c = Cart.objects.get(id=cid)
    c.delete()

    return redirect('/cart')

def cart_page(request):
    context={}
    if request.user.is_authenticated:
        c = Cart.objects.filter(uid=request.user.id)
        context['products']=c
        return render(request,'storeapp/cart.html',context)
    
    else:
        return redirect('/account/login')
    
def about_page(request):
    return render(request,'storeapp/about.html')


def cart(request):
    if request.user.is_authenticated:       #returns value as true or false depending upon the user is authenticated or not
        c=Cart.objects.filter(uid=request.user.id)
        context={'products':c}
        return render(request, 'ashstore/cart.html',context)
    else:
        return redirect('accounts/login')

def placeorder(request):
    if request.user.is_authenticated:
        return render(request, 'ashstore/placeorder.html')
    else:
        return redirect('accounts/login')
    
def add_to_cart(request,prod_id):
    if request.user.is_authenticated:

        user_id=request.user
        p_obj=Product.objects.get(id=prod_id)
        q1=Q(uid=user_id)
        q2=Q(pid=prod_id)

        check=Cart.objects.filter(q1 & q2)
        context={'product':p_obj}
        #print(check)
        #print(len(check))

        if len(check):   #if value is true it runs if-loop and runs else-loop if its false
            context={'msg1':"Product already exists"}
            return render(request,'ashstore/product_details.html',context)
        else:
            c=Cart.objects.create(uid=request.user, pid=p_obj)
            c.save()
            context={'msg2':"Added successfully"}
            return render(request,'ashstore/product_details.html',context)
    else:
        return redirect('/accounts/login')
    

def remove_item(request,rid):
    c=Cart.objects.get(id=rid)
    c.delete()
    return redirect('/cart')
