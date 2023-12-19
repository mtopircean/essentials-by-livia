from . import views
from django.urls import path, include
from allauth.account.views import PasswordResetView
from .views import simulated_403_view
from .views import simulated_500_view 
from website.views import custom_403_handler

urlpatterns = [
    path('', views.index_page, name='index'),
    path('accounts/', include('allauth.urls')),
    path('about-oils.html', views.about_oils, name='about_oils'),
    path('about-me.html', views.about_me, name='about_me'),
    path('data-protection.html', views.data_protection, name='data_protection'),
    path('promotions.html', views.promotions, name='promotions'),
    path('edit-promotion/<int:promotion_id>/', views.edit_promotion, name='edit_promotion'),
    path('update-description/<int:promotion_id>/', views.update_description, name='update_description'),
    path('delete-promotion/<int:promotion_id>/', views.delete_promotion, name='delete_promotion'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('update-product/<int:product_id>/', views.update_product, name='update_product'),
    path('recommended', views.update_product, name='recommended'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('recommended/', views.delete_product, name='recommended'),
    path('index.html', views.index, name='index'),
    path('user-account.html', views.user_account, name='user_account'),
    path('profile.html', views.logged_user_details, name='logged_user_details'),
    path('recommended.html', views.recommended, name='recommended'),
    path('contact.html', views.contact, name='contact'),
    path('register.html', views.register, name='register'),
    path('register/success/', views.register_success, name='register-success'),
    path('custom-logout/', views.custom_logout, name='custom_logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('favorites/<int:product_id>/', views.favourite_selection, name='favourite_selection'),
    path('profile/', views.display_favorites, name='display_favorites'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('filter-ailments', views.filter_ailments, name='filter_ailments'),
    path('create_product/', views.create_product, name='create_product'),
    path('create_promotion/', views.create_promotion, name='create_promotion'),
    #Urls created for testing purpose:
    path('403/', simulated_403_view, name='simulated_403'),
    path('500/', simulated_500_view, name='simulated_500'),
]

handler404 = views.handler404
handler403 = views.handler403
handler500 = views.handler500