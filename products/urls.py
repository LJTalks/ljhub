from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('products/<slug:slug>/', views.product_detail, name='product-detail'),
    path('purchase/<int:product_id>/', views.purchase_product, name='purchase-product'),
    path('history/', views.purchase_history, name='purchase-history'),
]
