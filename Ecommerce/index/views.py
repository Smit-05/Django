from django.shortcuts import render

# Create your views here.

def index(request):
    print(request.path)
    return render(request,'index.html')