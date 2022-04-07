from itertools import product
from django.shortcuts import redirect, render
from product.models import Products
from authentication.models import Users
from .models import Order 
# Create your views here.


def addCart(request):
    if request.method=='POST':
        product = request.POST['pID']
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        # request.session.get('cart').clear()
    return redirect('/authentication/normal') 

def viewCart(request):
    ids = list(request.session.get('cart').keys())
    products = Products.objects.filter(id__in=ids)
    return render(request,'viewCart.html',{'products':products})

def checkout(request):
    if request.method=='POST':
        address = request.POST['address']
        phone = request.POST['phone']
        user = request.session.get('userid')
        cart = request.session.get('cart')
        products = Products.objects.filter(id__in=list(cart.keys()))
        for p in products:
            print(cart.get(p.id))
            order = Order(user=Users(id = user),product=p,price=p.pPrice,quantity=cart.get(str(p.id)),address=address,phone=phone)
            order.save()
        
        request.session['cart'] = {}
    return redirect('viewCart')

def viewOrder(request):
    user = request.session.get('userid')
    orders = Order.objects.filter(user = user)
    print(orders)
    return render(request,'orders.html',{'orders':orders})
    