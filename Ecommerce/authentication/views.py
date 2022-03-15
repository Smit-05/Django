import smtplib
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Users
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
        password = request.POST['password1']
        email = request.POST['email']
        phone = request.POST['phone']
        if Users.objects.filter(email=email).exists():
            messages.info(request,"Email is already registered")
            return redirect('register')
        elif Users.objects.filter(username=username).exists():
            messages.info(request,"Username is already registered")
            return redirect('register')
        else:
            user = Users(username=username,password=password,email=email,phone=phone)
            user.save()
            messages.success(request,"User created successfully")
            sendMail(email,"You have been registerd","Jingalala")
            return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        if Users.objects.filter(email=email,password=password).exists():
            messages.info(request,"Email is already registered")
            sendMail(email,"You have been logged in","Jingalala")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    return render(request,'login.html')


