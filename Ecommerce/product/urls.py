from django.urls import include, path
from . import views
urlpatterns = [
    path('addProduct',views.addProduct,name='addProduct'),
    path('addCategory',views.addCategory,name='addCategory'),
    path('viewProduct',views.viewProduct,name='viewProduct'),
    path('myProduct',views.myProduct,name='myProduct'),
]