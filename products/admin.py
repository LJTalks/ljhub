from django.contrib import admin
from .models import Product, Purchase


# Product Admin View
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock',
                    'tier_one_limit', 'low_stock_threshold')
    search_fields = ('title',)
    list_filter = ('tier_one_limit', 'low_stock_threshold')
    ordering = ('title',)


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
