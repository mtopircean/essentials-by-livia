# Import necessary views and modules
from . import views
from django.urls import path, include
from allauth.account.views import PasswordResetView
from .views import simulated_403_view
from .views import simulated_500_view
from website.views import custom_403_handler

# URL  patterns needed for application.
# Includes all necessary CRUD operations on promotions and products
urlpatterns = [

    # General views for part of the static pages, and allauth functionalities
    path('', views.index_page,
         name='index'),
    path('accounts/', include('allauth.urls')),
    path('about-oils/', views.about_oils,
         name='about_oils'),
    path('about-me/', views.about_me,
         name='about_me'),
    path('data-protection/', views.data_protection,
         name='data_protection'),
    path('promotions/', views.promotions,
         name='promotions'),
    path('contact/', views.contact,
         name='contact'),
    path('recommended/', views.recommended,
         name='recommended'),
    path('index/', views.index,
         name='index'),
    # URLs for CRUD operations on promotions

    path('edit-promotion/<int:promotion_id>/', views.edit_promotion,
         name='edit_promotion'),
    path('update-description/<int:promotion_id>/', views.update_description,
         name='update_description'),
    path('delete-promotion/<int:promotion_id>/', views.delete_promotion,
         name='delete_promotion'),
    path('create_promotion/', views.create_promotion,
         name='create_promotion'),


    # URLs for CRUD operations on products
    path('edit-product/<int:product_id>/', views.edit_product,
         name='edit_product'),
    path('update-product/<int:product_id>/', views.update_product,
         name='update_product'),
    path('delete-product/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('register.html', views.register,
         name='register'),

    # URLs for CRUD operations on users
    path('create_product/', views.create_product,
         name='create_product'),
    path('user-account.html', views.user_account,
         name='user_account'),
    path('profile.html', views.logged_user_details,
         name='logged_user_details'),

    path('register-success.html', views.register_success,
         name='register_success'),
    path('custom-logout/', views.custom_logout,
         name='custom_logout'),
    path('password_reset/', PasswordResetView.as_view(),
         name='password_reset'),
    path('edit-profile/', views.edit_profile,
         name='edit_profile'),
    path('delete-account/', views.delete_account,
         name='delete_account'),

    # URL for favouriting a product
    path('favorites/<int:product_id>/', views.favourite_selection,
         name='favourite_selection'),
    path('profile/', views.display_favorites,
         name='display_favorites'),
    path('filter-ailments/', views.filter_ailments,
         name='filter_ailments'),

    # Test URLs for simulating error pages
    path('403/', simulated_403_view,
         name='simulated_403'),
    path('500/', simulated_500_view,
         name='simulated_500'),
]

handler404 = views.handler404
handler403 = views.handler403
handler500 = views.handler500
