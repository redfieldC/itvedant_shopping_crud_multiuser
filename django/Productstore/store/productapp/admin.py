from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','qty','cat','is_available']
    list_filter = ('cat','is_available')


admin.site.register(Product,ProductAdmin)

admin.site.site_header="Ekart Administration"
admin.site.site_title="Ekart Admin Website"