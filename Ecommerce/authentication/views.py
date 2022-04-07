from asyncio.windows_events import NULL
import smtplib
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Users
from product.models import Products
# Create your views here.


def sendMail(To,Subject,message):
    # server = smtplib.SMTP('server name which is gmail was using',port number)
    # server.login('email address from which we are sending mail','password of that email address')
    # server.sendmail('sender mail id',reciever mail id,message)
    
    servername = 'smtp.gmail.com'
    portno = 587
    From = 'd.poriya05@gmail.com'
    FromPassword = 'dharmesh&07092003&dharmesh'
    message = 'Subject: {}\n\n{}'.format(Subject, message)
    server = smtplib.SMTP(servername,portno)
    server.starttls()
    server.login(From,FromPassword)
    server.sendmail(From,To,message)
    server.quit()
    print('mail sent')


def register(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        mname = request.POST['middlename']
        lname = request.POST['lastname']
        password = request.POST['password1']
        email = request.POST['email']
        phone = request.POST['phone']
        usertype = request.POST.get('usertype',False)   
        if(usertype==False):
            print("Customer")
        else:
            print("Vendor")
        if Users.objects.filter(email=email).exists():
            messages.info(request,"Email is already registered")
            return redirect('register')
        elif Users.objects.filter(username=username).exists():
            messages.info(request,"Username is already registered")
            return redirect('register')
        else:
            user = Users(firstname=fname,middlename=mname,lastname=lname,username=username,password=password,email=email,phone=phone,usertype=usertype)
            user.save()
            messages.success(request,"User created successfully")
            # sendMail(email,"You have been registerd","Jingalala")
            return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        email = request.POST['email']
        password = request.POST['password']
        if Users.objects.filter(email=email,password=password).exists():
            user = Users.objects.get(email=email,password=password)
            request.session['userid'] = user.id
            request.session['username'] = user.username
            request.session['is_vendor'] = False
            if user.usertype==True:
                request.session['is_vendor'] = True
                return redirect('/')
            else:
                return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    return render(request,'login.html')

def normal(request):
    if request.session.is_empty():
        return redirect('login')
    return render(request,'index.html')

def vendor(request):
    if request.session.is_empty():
        return redirect('login')
    return render(request,'vendor.html')

def logout(request):
    del request.session['userid']
    del request.session['username']
    del request.session['is_vendor']
    request.session.clear()
    return redirect('/')

def myProfile(request):
    if request.method == 'GET':
        user = Users.objects.get(id=request.session.get('userid'))
        if(request.session.get('is_vendor')==True):
            print(user.username)
        else:
            print(user.username)
    return render(request,'myProfile.html',{'user':user})