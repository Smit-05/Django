from django.shortcuts import redirect, render
from product.models import Products
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