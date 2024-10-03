from django.contrib import admin
from .models import Product, Purchase
from django_summernote.admin import SummernoteModelAdmin


# Product Admin View
class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'excerpt',) # Apply Summernote to these fields
    list_display = ('title', 'slug', 'price', 'category') # removed stock and tier refs
    search_fields = ('title', 'content')
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)} # Auto Generates slug from title
    filter_horizontal = ('related_products',) # Adds a UI widget for ManyToManyField


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
