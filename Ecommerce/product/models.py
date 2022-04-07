from django.db import models
from authentication.models import Users

# Create your models here.
class Category(models.Model):
    cName = models.CharField(max_length=100)
    cDesc = models.TextField(max_length=1000)
    
class Products(models.Model):
    pImage = models.ImageField(upload_to='pics/',default=0)
    pName = models.CharField(max_length=100)
    pDesc = models.TextField(max_length=1000)
    pPrice = models.IntegerField()
    pShipment = models.TextField(max_length=1000)
    cId = models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    uId = models.ForeignKey(Users,null=True,on_delete=models.CASCADE)
    
