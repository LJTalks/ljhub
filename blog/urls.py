from django.urls import path
from . import views

urlpatterns = [
    # this is the blog home page that has all the blogs
    path('', views.blog_list, name='blog-list'),
    path('<slug:slug>/', views.blog_post,
         name='blog-post'),  # individual blog view
]
