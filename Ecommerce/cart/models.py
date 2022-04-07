from django.db import models
from product.models import Products
from authentication.models import Users
import datetime
# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)

    def placeOrder(self):
        self.save()