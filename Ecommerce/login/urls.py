from django.urls import path
from . import views
urlpatterns = [
    path('',views.validate,name='validate')
]