from django.test import TestCase, Client
from django.urls import reverse
from .models import AddPromotion, AddProduct, AppUser, Ailment, FavouriteSelection
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
    def test_index_page(self):
        response = self.client.get(reverse('index_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')