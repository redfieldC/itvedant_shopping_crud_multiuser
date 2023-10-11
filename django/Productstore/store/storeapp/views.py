from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def homepage(request):
    context = {"msg":"Hello all good morning"}
    context['x']=8000
    context['y']=8000
    context['number'] = [10,20,30,40,50,60,70,80,90,100]
    return render(request,'storeapp/home.html',context)

def contact(request):
    return HttpResponse("<h1>Welcome to ContactPage</h1>")

def edit(request,id):
    return HttpResponse("Welcome to Edit page " + id)

def delete(request,id):
    return HttpResponse("Welcome to delete page " + id)

def addition(request,x,y):
    result = int(x) + int(y)
    return HttpResponse("RESULT: " + str(result))