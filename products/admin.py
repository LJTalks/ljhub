from django.contrib import admin
from .models import Product, Purchase


# Product Admin models
admin.site.register(Product)
admin.site.register(Purchase)
