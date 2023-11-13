from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about-oils.html', views.about_oils, name='about_oils'),
    path('about-me.html', views.about_me, name='about_me'),
    path('data-protection.html', views.data_protection, name='data_protection'),
    path('promotions.html', views.promotions, name='promotions'),
    path('index.html', views.index, name='index'),
    path('user-account.html', views.user_account, name='user_account'),
    path('recommended.html', views.recommended, name='recommended'),
    path('contact.html', views.contact, name='contact'),
    path('register.html', views.register, name='register'),
]

handler404 = views.handler404
handler403 = views.handler403
handler500 = views.handler500