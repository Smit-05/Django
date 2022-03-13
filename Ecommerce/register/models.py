from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()