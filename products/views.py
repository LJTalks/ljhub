from django.shortcuts import render
from django.views.generic import TemplateView

# Products views


class HomePage(TemplateView):
    """
    Displays Home Page
    """
    template_name = 'index.html'
