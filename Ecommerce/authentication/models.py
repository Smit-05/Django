
from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50,default='')
    middlename = models.CharField(max_length=50,default='')
    lastname = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    usertype = models.BooleanField(default=False)
    