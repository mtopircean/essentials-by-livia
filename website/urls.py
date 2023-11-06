from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about-oils.html', views.about_oils, name='about_oils'),
    path('about-me.html', views.about_me, name='about_me'),
]

handler404 = 'website.views.404'
handler403 = 'website.views.403'
handler500 = 'website.views.500'