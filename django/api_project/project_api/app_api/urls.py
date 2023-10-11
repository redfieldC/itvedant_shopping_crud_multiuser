from django.urls import path
from . import views
urlpatterns = [
    path('get_client',views.get_client,name="get_client"),
    path('create_client',views.create_client,name="create_client"),
    path('update_client/<rid>',views.update_client,name="update_client"),
    path('delete_client/<rid>',views.delete_client,name="delete_client")
    # path('user_create/',views.user_create,name="user_create"),
    # path('user_update/',views.user_update,name="user_update")
]