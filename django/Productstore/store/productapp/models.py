from django.db import models

# Create your models here.

CAT = (
    (1,"Mobile"),
    (2,"Shoes"),
    (3,"Clothes")
)

AVAIL = (
    (1,"YES"),
    (0,"NO")
)

class Product(models.Model):
    name = models.CharField(max_length=50,verbose_name="Product Name")
    price = models.FloatField(verbose_name="Product Price Per Item")
    qty = models.IntegerField(verbose_name="Product Quantity")
    cat = models.IntegerField(verbose_name="Product Category",choices=CAT)
    is_available = models.BooleanField(verbose_name="Product Availability",choices=AVAIL)

    def __str__(self):
        return self.name