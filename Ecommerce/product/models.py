from tkinter import CASCADE
from django.db import models

# Create your models here.
class Products(models.Model):
    pName = models.CharField(max_length=100)
    pDesc = models.TextField(max_length=1000)
    pPrice = models.IntegerField()
    pShipment = models.TextField(max_length=1000)
    

class Category(models.Model):
    cName = models.CharField(max_length=100)
    cDesc = models.TextField(max_length=1000)
    pId = models.ForeignKey(Products,on_delete=models.CASCADE)
