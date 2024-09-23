from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'), # Product list view
    path('products/<slug:slug>/', views.product_detail, name='product_detail'), # Product detail view
    path('products/product_list', views.product_list, name='product_list'),
    path('purchase/<int:product_id>/', views.purchase_product, name='purchase_product'),
    path('history/', views.purchase_history, name='purchase_history'),
]
