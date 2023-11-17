from allauth.account.forms import SignupForm
from django import forms
from .models import AppUser

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=300)
    phone_number = forms.CharField(max_length=20)
    username = forms.CharField(max_length=100)
    join_team = forms.BooleanField(required=False)
    know_more_products = forms.BooleanField(required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user_data = self.cleaned_data
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.email = user_data['email']
        user.username = user_data['username']

        app_user = AppUser.objects.create(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            phone_number=user_data['phone_number'],
            username=user_data['username'],
            join_team=user_data['join_team'],
            know_more_products=user_data['know_more_products']
        )
        app_user.save()

        return user