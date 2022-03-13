from django.urls.conf import include
from django.urls import URLPattern, path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('register',include('login.urls')),
]