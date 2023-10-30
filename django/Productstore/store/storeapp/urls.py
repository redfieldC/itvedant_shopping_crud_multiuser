from django.urls import path,include
from storeapp import views 

urlpatterns = [
    path('',views.home),
    path('home',views.homepage),
    path('contact',views.contact),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete),
    path('addition/<x>/<y>',views.addition),
    path('catfilter/<int:catv>',views.cat_filter),
    path('pricefilter/',views.price_filter),
    path('sort',views.sort),
    path('search',views.search),
    path('removecart/<cid>',views.remove_cart),
    path('pdetails/<pid>',views.pdetails),
    path('porder',views.placeorder),
    path('cart/<prod_id>',views.add_to_cart),
    path('removeitem/<rid>',views.remove_item),
    path('cart',views.cart_page)
]