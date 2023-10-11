from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=50)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())

class Project(models.Model):
    pname = models.CharField(max_length=50)
    cid = models.ForeignKey(Client,on_delete=models.CASCADE,db_column='cid')
    uid = models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')