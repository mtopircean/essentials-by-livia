#importing necessary models and modules
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.views import generic
from .models import AddProduct, AddPromotion, AppUser, Ailment, FavouriteSelection
from .forms import CustomSignupForm
from django.urls import reverse
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, Http404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

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

#Approve user view:
@staff_member_required
def user_approval(request):
    users_pending_approval = AppUser.objects.filter(approved=False)
    
    context = {
        'users_pending_approval': users_pending_approval,
    }

    return render(request, 'profile.html', context)

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
@staff_member_required
def edit_promotion(request, promotion_id):
    promotion = get_object_or_404(AddPromotion, pk=promotion_id)
    return render(request, 'edit_promotion.html', {'promotion': promotion})

#Updates the promotion description: first retrieves or 404 if not found, then updates
#and redirects user bat to promotion page
@staff_member_required
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
@staff_member_required
def delete_promotion(request, promotion_id):
    if request.method == 'POST':
        promotion = get_object_or_404(AddPromotion, pk=promotion_id)
        promotion.delete()
        return redirect('promotions')
    return redirect('promotions')
        
#Displays products based on ailments and favorites
def recommended(request):
    #Retries ailments, products and validates user admin status
    ailments = Ailment.objects.annotate(num_products=Count('addproduct')).filter(num_products__gt=0)
    products = AddProduct.objects.all().order_by('name')
    is_admin = request.user.is_superuser
    
    # Check user favorites and approval status
    is_user_approved = False
    user_favorites = []
    
    #Checks favorite status if user is logged in and approved
    if request.user.is_authenticated:
        try:
            app_user = AppUser.objects.get(user=request.user)
            is_user_approved = app_user.approved
            if is_user_approved:
                user_favorites = FavouriteSelection.objects.filter(user=request.user, is_favorite=True).values_list('product_id', flat=True)
            else:
                user_favorites = []
        except AppUser.DoesNotExist:
            is_user_approved = False
    else:
        is_user_approved = False
        user_favorites = []

    #Prepare context to display the template data and renders it
    context = {
        'is_admin': is_admin,
        'is_user_approved': is_user_approved,
        'products': products,
        'ailments': ailments,
        'user_favorites': user_favorites,
    }

    return render(request, 'recommended.html', context)

#Edit product description: first retrieves or 404 if not found, then updates description
#and redirects user to recommended page
@staff_member_required
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
@staff_member_required
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
@staff_member_required
def delete_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(AddProduct, pk=product_id)
        product.delete()
        return redirect('recommended')
    return redirect('recommended')

#Filters products based on selected ailments/conditions#
@login_required
def filter_ailments(request):
    #Collects ailments, products, selected filters, collects only the ailments with one product associated to them
    ailments = Ailment.objects.annotate(num_products=Count('addproduct')).filter(num_products__gt=0)
    products = AddProduct.objects.all().order_by('name')
    selected_filters = []
    
    is_user_approved = False
    user_favorites = []
    
    if request.user.is_authenticated:
        try:
            app_user = AppUser.objects.get(user=request.user)
            is_user_approved = app_user.approved
            if is_user_approved:
                user_favorites = FavouriteSelection.objects.filter(user=request.user, is_favorite=True).values_list('product_id', flat=True)
            else:
                user_favorites=[]
        except AppUser.DoesNotExist:
            is_user_approved = False
    else:
        is_user_approved = False
        user_favorites = []
    
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
        'is_user_approved':is_user_approved,
        'user_favorites':user_favorites,
    }
    return render(request, 'recommended.html', context)

#Renders the Contact page
def contact(request):
    return render(request, 'contact.html')

#Renders the User Account page
@login_required
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
@login_required
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
    
    user_context = {
        'user_data': app_user,
    }
    return render(request, 'profile.html', user_context)
        
#Deletes a user account and returns to index
@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('index')

    return render(request, 'profile.html')

#Displays the logged in user details: retrieves user and favorite data
#creates context and displays it
#prints 404 error if user doesn`t exist
@login_required
def logged_user_details(request):
    
    try:
        logged_in_user = request.user
        user_data = AppUser.objects.get(user=logged_in_user)
        user_favorites = FavouriteSelection.objects.filter(user=request.user, is_favorite=True)
        print(user_favorites)
        
        is_user_approved = user_data.approved
        
        context = {
            'user_data': user_data,
            'user_favorites': user_favorites
        }
        return render(request, 'profile.html', context)

    except AppUser.DoesNotExist:
            raise Http404("User does not exist")

#Displays custom logout
@login_required        
def custom_logout(request):
    logout(request)
    return redirect('index')

#Adds and removes product to and from favorites
#Applicable only for logged in users
#Retrieves the product and checks is favorite status
#If not favorite creates a new Favourite selection
#Redirects to recommended or to profile when a favourite selection is removed
#this is done by passing additional info in the url at form submission
@login_required
def favourite_selection(request, product_id):
    product = get_object_or_404(AddProduct, id=product_id)
    redirect_to = request.GET.get('source', 'recommended')
    try:
        favorite_selection = FavouriteSelection.objects.get(user=request.user, product=product)
        favorite_selection.is_favorite = not favorite_selection.is_favorite
        favorite_selection.save()
    except FavouriteSelection.DoesNotExist:
        FavouriteSelection.objects.create(user=request.user, product=product, is_favorite=True)

    if redirect_to == 'logged_user_details':
        return redirect('logged_user_details')
    else:
        return redirect('recommended')

#Displays user favorites:collects, creates context, renders
@login_required
def display_favorites(request):
    user_favorites = FavouriteSelection.objects.all()
    context = {
        'user_favorites': user_favorites,
    }
    return render(request, 'profile.html', context)

#Creates a product from the front end view when logged as an admin
@staff_member_required
def create_product(request):
    if request.method == 'POST':
        # Retrieve form data
        product_name = request.POST.get('add_product_name')
        product_description = request.POST.get('add_product_description')
        product_photo_url = request.POST.get('add_product_photo_url')

        #Retrieve and store selected id`s
        selected_ailment_ids = request.POST.getlist('add_product_ailments[]')
        
        # Create and save new product to the database
        new_product = AddProduct.objects.create(
            name=product_name,
            description=product_description,
            price=0.0, #no price used at this moment in development
            image_url=product_photo_url,
        )
        # Save selected ailments to the product
        for ailment_id in selected_ailment_ids:
            ailment = get_object_or_404(Ailment, id=ailment_id)
            new_product.ailments.add(ailment)

        # Redirect to recommended page
        return redirect('recommended')
    else:
        return redirect('recommended')
    
#Creates a promotion from the front end view when logged as an admin
@staff_member_required   
def create_promotion(request):
    if request.method == 'POST':
        # Retrieve form data
        promotion_name = request.POST.get('add_promotion_name')
        promotion_description = request.POST.get('add_promotion_description')
        promotion_date = request.POST.get('add_promotion_date')
        promotion_url = request.POST.get('add_promotion_photo_url')
        
        # Create and save new promotion to the database
        new_promotion = AddPromotion.objects.create(
            name = promotion_name,
            description = promotion_description,
            image_url = promotion_url,
            expires_on = promotion_date,
            
        )
        return redirect('promotions')
    else:
        return redirect('promotions')
    


#Renders confirmation of successfull registration page
@login_required
def register_success(request):
    return render(request, 'register-success.html')

#Renders errors: 403, 404, 500
def handler403(request, exception):
    return render(request, '403.html', status=403)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)