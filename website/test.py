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