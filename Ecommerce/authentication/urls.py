from django.urls import include, path
from . import views
urlpatterns = [
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    
]