from contextlib import nullcontext
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Category, Products
from authentication.models import Users
# Create your views here.
def addProduct(request):
    categories = Category.objects.all()
    if request.method=='POST':
        cName = request.POST['pCategory']
        cat = Category.objects.get(cName=cName)
        pImage = request.FILES['pImage']
        pName = request.POST['pName']
        pDesc = request.POST['pDesc']
        pPrice = int(request.POST['pPrice'])
        pShipment = request.POST['pShipment']
        uId = request.POST['uId']
        product = Products(uId=Users(id = uId),cId=cat,pImage=pImage,pName=pName,pDesc=pDesc,pPrice=pPrice,pShipment=pShipment)
        product.save()
        return redirect('/')
    return render(request,'addProduct.html',{'categories':categories})

def addCategory(request):
    if request.method=='POST':
        cName = request.POST['cName']
        cDesc = request.POST['cDesc']
        if Category.objects.filter(cName=cName).exists():
            messages.error(request,"Category already exists")
            return redirect('addCategory')
        else:
            cat = Category(cName=cName,cDesc=cDesc)
            cat.save()
            messages.success(request,"Category added Successfully")
            return redirect('/')
    return render(request,'addCategory.html')

def viewProduct(request):
    if request.method=='GET':
        proid = request.GET.get('pid')
        product = Products.objects.filter(id=proid)
        if(product):
            print(len(product))
            mypro = nullcontext
            for p in product:
                mypro = p
            print(mypro)
            return render(request,'viewProduct.html',{'product':mypro})
        else:
            return redirect('/')
    return redirect('/')

def myProduct(request):
    user = request.session.get('userid')
    products = Products.objects.filter(uId = user)
    return render(request,'myProducts.html',{'products':products})