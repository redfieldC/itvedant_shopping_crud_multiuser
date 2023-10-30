from django.urls import path
from ash_store import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home',views.homepage),
    path('about',views.about),
    path('contact',views.contact),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete),
    path('addition/<x>/<y>',views.addition),

    path('',views.home),
    path('aboutus',views.about_us),
    path('contactus',views.contact_us),
    path('cart',views.cart),
    path('porder',views.placeorder),
    path('catfilter/<cid>',views.cat_filter),
    path('pricerange',views.pricerange),
    path('sort',views.sort),
    path('search',views.search),

    path('pdetails/<pid>',views.pdetails),
    path('cart/<prod_id>',views.add_to_cart),
    path('removeitem/<rid>',views.remove_item),
    path('changeqty/<cqid>',views.changeqty),
    
]

if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
