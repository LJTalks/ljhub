from django.urls import path
from . import views

urlpatterns = [
    # this is the blog home page that has all the blogs
    path('', views.blog_list, name='blog_list'),  # The blog home page/list view
    path('<slug:slug>/', views.blog_post, name='blog_post'), # Individual Blog posts with slug address 
]
