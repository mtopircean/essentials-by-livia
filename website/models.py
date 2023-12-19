#Importing the necessary modules
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


#Defines the Ailment model
class Ailment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Defines the AddProduct model including relationship to Ailment
class AddProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ailments = models.ManyToManyField(Ailment)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_on = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=255)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

#Defines the AddPromotion model
class AddPromotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    expires_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-expires_on']

    def __str__(self):
        return self.name

#Define the AppUser model with additional fields to the standard User module
class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    phone_number = models.CharField(max_length=20)
    request_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)
    join_team = models.BooleanField(default=False)
    i_want_to_know_more_about_the_products = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Updates AppUser when User change is triggered
@receiver(pre_save, sender=User)
def update_app_user_from_user(sender, instance, **kwargs):
    try:
        app_user = AppUser.objects.get(user=instance)
        app_user.first_name = instance.first_name
        app_user.last_name = instance.last_name
        app_user.email = instance.email
        app_user.save()
    except AppUser.DoesNotExist:
        pass

#Define the FavouriteSelection model and link to User
class FavouriteSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(AddProduct, on_delete=models.CASCADE)
    favourite_date = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} favorites {self.product.name}"
