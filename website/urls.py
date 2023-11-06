from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about-oils.html', views.about_oils, name='about_oils'),
    path('about-me.html', views.about_oils, name='about_me'),
]