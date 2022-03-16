from django.contrib import admin

from .models import Products,Category

# Register your models here.
admin.site.register(Products)
admin.site.register(Category)