#importing necessary models and modules
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.views import generic
from .models import AddProduct, AddPromotion, AppUser, Ailment, FavouriteSelection
from .forms import CustomSignupForm
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404

#Renders the index page
def index_page(request):
    return render(request, 'index.html')
def index(request):
    return render(request, 'index.html')

#Renders the About Oils page
def about_oils(request):
    return render(request, 'about-oils.html')

#Renders the About Me page
def about_me(request):
    return render(request, 'about-me.html')

#Renders the GDPR page
def data_protection(request):
    return render(request, 'data-protection.html')

#Renders the Promotions page
def promotions(request):
    
    #Collects all promotions and checks admin status
    promotions = AddPromotion.objects.all()
    is_admin = request.user.is_superuser
    
    #Prepares the context to display and renders it
    template_promotion = {
        'is_admin': is_admin,
        'promotions': promotions
    }
    
    return render(request, 'promotions.html', template_promotion)

#Renders the edit setions in promotion
def edit_promotion(request, promotion_id):
    promotion = get_object_or_404(AddPromotion, pk=promotion_id)
    return render(request, 'edit_promotion.html', {'promotion': promotion})

#Updates the promotion description: first retrieves or 404 if not found, then updates
#and redirects user bat to promotion page
def update_description(request, promotion_id):
    if request.method == 'POST':
        promotion = get_object_or_404(AddPromotion, pk=promotion_id)
        new_description = request.POST.get('new_description')
        promotion.description = new_description
        promotion.save()
        return redirect('promotions')
    return redirect('promotions')

#Deletes promotion:first retrieves or 404 if not found, then deletes
#and redirects user bat to promotion page
def delete_promotion(request, promotion_id):
    if request.method == 'POST':
        promotion = get_object_or_404(AddPromotion, pk=promotion_id)
        promotion.delete()
        return redirect('promotions')
    return redirect('promotions')
        
#Displays products based on ailments and favorites
def recommended(request):
    #Retries ailments, products and validates user admin status
    ailments = Ailment.objects.all()
    products = AddProduct.objects.all()
    is_admin = request.user.is_superuser
    
    #Checks favorite status if user is logged in
    if request.user.is_authenticated:
        user_favorites = FavouriteSelection.objects.filter(user=request.user, is_favorite=True).values_list('product_id', flat=True)
    else:
        user_favorites = []

    #Prepare contest to display the template data and renders it
    context = {
        'is_admin': is_admin,
        'products': products,
        'ailments': ailments,
        'user_favorites': user_favorites,
    }

    return render(request, 'recommended.html', context)

#Edit product description: first retrieves or 404 if not found, then updates description
#and redirects user to recommended page
def edit_product(request, product_id):
    product = get_object_or_404(AddProduct, pk=product_id)

    if request.method == 'POST':
        new_description = request.POST.get('new_description')
        if new_description:
            product.description = new_description
            product.save()
            return redirect('recommended')
    
    return render(request, 'recommended.html', {'product': product, 'is_admin': True})

#Update product description: first retrieves product or 404 if not found, then updates description
#if user is admin and redirects to recommended
def update_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(AddProduct, pk=product_id)
        
        if request.user.is_superuser:
            new_description = request.POST.get('new_description')
            if new_description is not None:
                product.description = new_description
                product.save()
        
        return redirect('recommended')

    return redirect('recommended')

#Delete product: first retrieves product or 404 if not found, then deletes it
#if user is admin and redirects to recommended
def delete_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(AddProduct, pk=product_id)
        product.delete()
        return redirect('recommended')
    return redirect('recommended')

#Filters products based on selected ailments/conditions
def filter_ailments(request):
    #Collects ailments, products, selected filters
    ailments = Ailment.objects.all()
    products = AddProduct.objects.all()
    selected_filters = []
    
    if request.method == "GET":
        selected_filters = request.GET.getlist('filter_checkbox')
        if selected_filters:
            # Create query to filter products based on selected ailments
            # combines multiple into a single query
            queries = [Q(ailments__name=filter_val) for filter_val in selected_filters]
            combined_query = queries.pop()
            for query in queries:
                combined_query |= query
            #applies the combined query to filter AddProduct
            products = AddProduct.objects.filter(combined_query).distinct()
    
    #creates the context and renders it returning to recommended    
    context = {
        'ailments' : ailments,
        'products' : products,
        'selected_filters': selected_filters,
    }
    return render(request, 'recommended.html', context)

#Renders the Contact page
def contact(request):
    return render(request, 'contact.html')

#Renders the User Account page
def user_account(request):
    return render(request, 'user-account.html')

#Renders the account registration form using the customized allauth form
def register(request):
    if request.method == 'POST':
        signup_form = CustomSignupForm(request.POST)
        if signup_form.is_valid():
            
            #Creates the new user in the AppUser model
            user = User.objects.create_user(
                username=signup_form.cleaned_data['username'],
                password=signup_form.cleaned_data['password1'], 
                first_name=signup_form.cleaned_data['first_name'],
                last_name=signup_form.cleaned_data['last_name'],
                email=signup_form.cleaned_data['email']
            )
            
            #This code extends the std functionality and creates the AppUser,
            #in addition to the standard user(2 sections in admin)
            app_user = AppUser.objects.create(
                user=user, 
                first_name=signup_form.cleaned_data['first_name'],
                last_name=signup_form.cleaned_data['last_name'],
                email=signup_form.cleaned_data['email'],
                phone_number=signup_form.cleaned_data['phone_number'],
                join_team=signup_form.cleaned_data['join_team'],
                i_want_to_know_more_about_the_products=signup_form.cleaned_data['i_want_to_know_more_about_the_products']
            )

            #Redirects user to a registration success page
            return HttpResponseRedirect(reverse('register-success'))
        
    else:
        signup_form = CustomSignupForm()

    return render(request, 'register.html', {'signup_form': signup_form})

#Allows to edit the user profile: retrieves user data
#updates the data
def edit_profile(request):
    user = request.user
    app_user = AppUser.objects.get(user=user)

    if request.method == 'POST':
        app_user.first_name = request.POST.get('first_name')
        app_user.last_name = request.POST.get('last_name')
        app_user.email = request.POST.get('email')
        app_user.phone_number = request.POST.get('phone_number')
        app_user.join_team = request.POST.get('join_team') == 'yes'
        app_user.i_want_to_know_more_about_the_products = request.POST.get('i_want_to_know_more_about_the_products') == 'yes'
        
        app_user.save()
    
    context = {
        'user_data': app_user,
    }
    return render(request, 'profile.html', context)
        
#Deletes a user account and returns to index
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('index')

    return render(request, 'profile.html')

#Displays the logged in user details: retrieves user and favorite data
#creates context and displays it
#prints 404 error if user doesn`t exist
def logged_user_details(request):
    
    try:
        logged_in_user = request.user
        user_data = AppUser.objects.get(user=logged_in_user)
        user_favorites = FavouriteSelection.objects.filter(user=request.user, is_favorite=True)
        print(user_favorites)
        
        context = {
            'user_data': user_data,
            'user_favorites': user_favorites
        }
        return render(request, 'profile.html', context)

    except AppUser.DoesNotExist:
            raise Http404("User does not exist")

#Displays custom logout        
def custom_logout(request):
    logout(request)
    return redirect('index')

#Adds and removes product to and from favorites
#Applicable only for logged in users
#Retrieves the product and checks is favorite status
#If not favorite creates a new Favourite selection
#Redirects to recommended
@login_required
def favourite_selection(request, product_id):
    product = get_object_or_404(AddProduct, id=product_id)
    try:
        favorite_selection = FavouriteSelection.objects.get(user=request.user, product=product)
        favorite_selection.is_favorite = not favorite_selection.is_favorite
        favorite_selection.save()
    except FavouriteSelection.DoesNotExist:
        FavouriteSelection.objects.create(user=request.user, product=product, is_favorite=True)

    return redirect('recommended')

#Displays user favorites:collects, creates context, renders
def display_favorites(request):
    user_favorites = FavouriteSelection.objects.all()
    context = {
        'user_favorites': user_favorites,
    }
    return render(request, 'profile.html', context)

#Renders confirmation of successfull registration page
def register_success(request):
    return render(request, 'register-success.html')

#Renders errors: 403, 404, 500
def handler403(request, exception):
    return render(request, '403.html', status=403)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)