from django.contrib import admin
from .models import Product, Purchase
from django_summernote.admin import SummernoteModelAdmin


# Product Admin View
class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',) # Apply Summernote to the 'description' field
    list_display = ('title', 'slug', 'price', 'category') # removed stock and tier refs
    search_fields = ('title', 'description')
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)} # Auto Generates slug from title


# Purchase Admin View
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity',
                    'price_paid', 'purchase_date', 'status')
    list_filter = ('status', 'purchase_date')
    search_fields = ('user__username', 'product__title')
    ordering = ('-purchase_date',)


# Register the models with the custom views
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
