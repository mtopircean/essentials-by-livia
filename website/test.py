import unittest
from . import views 
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import AddProduct, AddPromotion

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = AddProduct.objects.create(name='Test Product', description='Test Description')
        self.promotion = AddPromotion.objects.create(name='Test Promotion', description='Test Description')
        
    def test_index_page(self):
        response = self.client.get(reverse('index_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')