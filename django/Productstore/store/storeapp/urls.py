from django.urls import path,include
from storeapp import views 

urlpatterns = [
    path('home',views.homepage),
    path('contact',views.contact),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete),
    path('addition/<x>/<y>',views.addition),
]