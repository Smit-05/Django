from django.shortcuts import render
from product.models import Products
# Create your views here.

def index(request):
    products = Products.objects.all()
    return render(request,'index.html',{'products':products})