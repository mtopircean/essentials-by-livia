from django.shortcuts import render
from django.views import generic
from .models import AddProduct, AddPromotion


def index_page(request):
    return render(request, 'index.html')

def about_oils(request):
    return render(request, 'about-oils.html')

def about_me(request):
    return render(request, 'about-me.html')