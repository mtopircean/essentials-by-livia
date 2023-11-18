from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views import generic
from .models import AddProduct, AddPromotion, AppUser
from .forms import CustomSignupForm
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
    is_admin = request.user.is_superuser
    
    template_promotion = {
        'is_admin': is_admin,
        'promotions': promotions
    }
    
    return render(request, 'promotions.html', template_promotion)

def edit_promotion(request, promotion_id):
    promotion = get_object_or_404(AddPromotion, pk=promotion_id)
    return render(request, 'edit_promotion.html', {'promotion': promotion})
    

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
            
            user = User.objects.create_user(
                username=signup_form.cleaned_data['username'],
                password=signup_form.cleaned_data['password1'], 
                first_name=signup_form.cleaned_data['first_name'],
                last_name=signup_form.cleaned_data['last_name'],
                email=signup_form.cleaned_data['email']
            )
            
            app_user = AppUser.objects.create(
                user=user, 
                phone_number=signup_form.cleaned_data['phone_number'],
                join_team=signup_form.cleaned_data['join_team'],
                know_more_products=signup_form.cleaned_data['know_more_products']
            )

            return HttpResponseRedirect(reverse('register-success'))
        
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