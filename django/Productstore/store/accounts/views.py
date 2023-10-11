from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("WELCOME TO ACCOUNTS")