from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/product_list', views.product_list, name='product_list'),
    path('purchase/<int:product_id>/', views.purchase_product, name='purchase_product'),
    path('history/', views.purchase_history, name='purchase_history'),
]
