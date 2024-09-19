from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blog_home(request):
    return HttpResponse("Hello, it's the blog home!")
