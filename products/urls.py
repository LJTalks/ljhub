from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('purchase/<int:product_id>/',
         views.purchase_product, name='purchase_product'),
    path('history/', views.purchase_history, name='purchase_history'),
]
