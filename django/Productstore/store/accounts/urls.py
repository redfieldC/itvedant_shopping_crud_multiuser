from django.urls import path
from accounts import views 


urlpatterns = [
    path('homepage',views.homepage),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('register', views.user_register),
]
