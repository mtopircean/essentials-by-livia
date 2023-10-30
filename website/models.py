from django.db import models
from django.contrib.auth.models import User


class Ailment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AddProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ailments = models.ManyToManyField(Ailment)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=255)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class AddPromotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name