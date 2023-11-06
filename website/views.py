from django.shortcuts import render
from django.views import generic
from .models import AddProduct, AddPromotion


def index_page(request):
    return render(request, 'index.html')

def about_oils(request):
    return render(request, 'about-oils.html')

def about_me(request):
    return render(request, 'about-me.html')

def page_404(request):
    return render(request, '404.html')

def page_403(request):
    return render(request, '403.html')

def page_500(request):
    return render(request, '500.html')