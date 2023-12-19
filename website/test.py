import unittest
from . import views 
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from .models import AddProduct, AddPromotion

#Testing static pages
class StaticPages(TestCase):

    def test_index_page_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_oils_view(self):
        response = self.client.get(reverse('about_oils'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about-oils.html')
        
    def test_about_me_view(self):
        response = self.client.get(reverse('about_me'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about-me.html')
        
    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        
    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
    
    def test_promotions_success_view(self):
        response = self.client.get(reverse('promotions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'promotions.html')
        
    def test_recommended_view(self):
        response = self.client.get(reverse('recommended'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recommended.html')
    
    
    def test_data_protection_view(self):
        response = self.client.get(reverse('data_protection'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'data-protection.html')
        
    def test_404_error_view(self):
        response = self.client.get('/404/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        
    def test_403_error_view(self):
        response = self.client.get('/403/')
        self.assertEqual(response.status_code, 403)

    def test_500_error_view(self):
        with self.assertRaises(Exception):
            self.client.get('/500/')

#Testing decorator impacted views to further test at a later stage
# class DecoratorTests(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='user', password='password')
        
#     def test_login_required_decorator(self):
        
#         response = self.client.get(reverse('delete-account'))
#         self.assertNotEqual(response.status_code, 200)
        
#         self.client.login(username='user', password='password')
#         response = self.client.get(reverse('delete-account'))
#         self.assertEqual(response.status_code, 200)
        
#     def test_staff_member_required_decorator(self):
#         staff_user = User.objects.create_user(username='staff', password='password', is_staff=True)
            
#         self.client.login(username='user', password='password')
#         response = self.client.get(reverse('create_product'))
#         self.assertNotEqual(response.status_code, 200)

#         self.client.login(username='staff', password='password')
#         response = self.client.get(reverse('create_product'))
#         self.assertEqual(response.status_code, 200)    