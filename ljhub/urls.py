"""
URL configuration for ljhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products import views


urlpatterns = [
    path('accounts/', include('allauth.urls')),  # allauth for authentication
    path('admin/', admin.site.urls),  # Admin panel
    path('blog/', include('blog.urls')),  # Blog app
    path('products/', include('products.urls')),  # Products app
    path('summernote/', include('django_summernote.urls')),
    
    # Custom login_or_signup page before slug or catch all's
    # Directly route login_or_signup
    path('login_or_signup/', views.login_or_signup, name='login_or_signup'),
    
    # Home page points to blog app for now
    path('', include('blog.urls'), name='blog-urls'),
]
