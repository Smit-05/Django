from django.shortcuts import render
from product.models import Products,Category
# Create your views here.

def index(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    return render(request,'index.html',{'products':products,'categories':categories})

def cSort(request):
    print(request.GET['cid'])
    catid = request.GET.get('cid')
    products = Products.objects.filter(cId=catid)
    categories = Category.objects.all()
    return render(request,'index.html',{'products':products,'categories':categories})