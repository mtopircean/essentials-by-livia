from django.shortcuts import render
from django.views import generic
from .models import AddProduct, AddPromotion


def index_page(request):
    return render(request, 'index.html')
