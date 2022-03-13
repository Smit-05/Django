from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from .models import Users
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
@csrf_protect
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        if password1 == password2:
            if Users.objects.filter(username=username).exists():
                messages.info(request, 'Username is not available')# print('Username is not available')
                return redirect('signup')
            elif Users.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('signup')
            else:
                user = Users(username=username, password=make_password(password1), email=email,
                                                phone=phone)
                user.save()
                messages.info(request, 'User Created')
                return redirect('signup')
        else:
            print('Password not matching')
            return redirect('/')
    else:
        return render(request, 'signup.html')
