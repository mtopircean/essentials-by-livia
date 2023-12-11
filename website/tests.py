from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

def setUp(self):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.promotions_url = reverse('promotions')
    
def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
def test_promotions_view(self):
        response = self.client.get(self.promotions_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'promotions.html')