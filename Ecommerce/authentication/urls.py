from django.urls import include, path
from . import views
urlpatterns = [
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('normal',views.normal,name="normal"),
    path('logout',views.logout,name="logout"),
    
]