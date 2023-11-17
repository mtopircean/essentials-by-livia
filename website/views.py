from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views import generic
from .models import AddProduct, AddPromotion, AppUser
from .forms import CustomSignupForm
from django.utils import timezone
from django.urls import reverse

def index_page(request):
    return render(request, 'index.html')

def about_oils(request):
    return render(request, 'about-oils.html')

def about_me(request):
    return render(request, 'about-me.html')

def data_protection(request):
    return render(request, 'data-protection.html')

def promotions(request):
    
    promotions = AddPromotion.objects.all()
    
    template_promotion = {
        'promotions' : promotions
    }
    
    return render(request, 'promotions.html', template_promotion)

def index(request):
    return render(request, 'index.html')

def recommended(request):
    return render(request, 'recommended.html')

def contact(request):
    return render(request, 'contact.html')

def user_account(request):
    return render(request, 'user-account.html')

def register(request):
    if request.method == 'POST':
        signup_form = CustomSignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save
            user.request_date = timezone.now()
            user.first_name = signup_form.cleaned_data['first_name']
            user.last_name = signup_form.cleaned_data['last_name']
            user.email = signup_form.cleaned_data['email']
            user.phone_number = signup_form.cleaned_data['phone']
            user.username = signup_form.cleaned_data['username']
            user.join_team = signup_form.cleaned_data['join_team']
            user.know_more_products = signup_form.cleaned_data['know_more_products']
            user.save()
            
            return HttpResponseRedirect(reverse('register-success'))
        
        else:
            return render(request, 'register.html', {'signup_form': signup_form})
    else:
        signup_form = CustomSignupForm()

    return render(request, 'register.html', {'signup_form': signup_form})

def register_success(request):
    return render(request, 'register-success.html')

def handler403(request, exception):
    return render(request, '403.html', status=403)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)