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
    i_want_to_know_more_about_the_products = forms.BooleanField(required=False)

    def save(self, request):
        # Save the user with the stadard existing method
        user = super(CustomSignupForm, self).save(request)
        
        #Pull the cleaned data
        user_data = self.cleaned_data
        
        #Update the users with the input data
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.email = user_data['email']
        user.username = user_data['username']
        
        #Save the user
        user.save()
        
        #Creates the AppUser object
        app_user = AppUser.objects.create(
            user=user,
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            phone_number=user_data['phone_number'],
            username=user_data['username'],
            join_team=user_data['join_team'],
            i_want_to_know_more_about_the_products=user_data['i_want_to_know_more_about_the_products']
        )

        return user