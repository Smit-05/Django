from pyexpat.errors import messages
from re import I
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password
from register.models import Users
# Create your views here.
def validate(request):
    if request.method=='POST':
        email =request.POST['email']
        password =request.POST['password']
        user = Users.objects.all()
        if Users.objects.filter(email=email,password=check_password(password,user.password)).exists():
            return render(request,'index.html')
        else:
            return redirect('login')
    return render(request,'login.html')
