from django.shortcuts import render,redirect,HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
# Create your views here.
def get_client(request):
    c = Client.objects.all()
    context  = []
    i=0
    for x in c:
        # context[i]={
        #     'id':x.id,
        #     'client_name':x.client_name,
        #     'created_at': x.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        #     'created_by':x.uid.first_name
        # }
        # i+=1
        #--------------------------------
        context[i]={
            'id':x.id,
            'client_name':x.client_name,
            'created_at': x.created_at,
            'created_by':x.uid.first_name
        }
        i+=1
        # client_dict = model_to_dict(x)
        # context.append(client_dict)
    print("************************")
    print("TYPE OF ALL CLIENTS:",type(context))
    print("ALL_CLIENTS:",context)
    json_data = json.dumps(context,default=str)
    return HttpResponse(json_data,content_type="application/json")
    # return HttpResponse(json_data)

@csrf_exempt
def create_client(request):
    
    cname = request.POST.get('cname')
    user_id = request.POST.get('user_id')
    u = User.objects.filter(id=user_id)
    print("************************")
    print(u[0])
    print("************************")   
    c= Client.objects.create(client_name=cname,uid=u[0])
    c.save()
    res={'success':'client created successfully'}
    json_data = json.dumps(res)
    return HttpResponse(json_data,content_type="application/json")

@csrf_exempt
def update_client(request,rid):
    print("*********************")

    print("*******************")
    data = json.loads(request.body)
    print("DATA in dicitonary",data)
    ucname = data['cname']
    c = Client.objects.filter(id=rid)
    c.update(client_name=ucname,updated_at=datetime.datetime.now())
    res = {'success':'client updated successfully'}
    json_data = json.dumps(res)
    return HttpResponse(json_data,content_type="application/json")

@csrf_exempt
def delete_client(request,rid):
    print("*********************")
    print(request)
    print("*********************")
    c = Client.objects.filter(id=rid)
    c.delete()
    res = {'success':'client deleted successfully'}
    json_data = json.dumps(res)
    return HttpResponse(json_data,content_type="application/json")

# def user_create(request):
#     return render(request,'user_create.html')

# def user_update(request):
#     return render(request,'user_update.html')