from django.urls import include, path
from . import views

urlpatterns = [
    path('addCart',views.addCart,name="addCart"),
    path('viewCart',views.viewCart,name="viewCart"),

]