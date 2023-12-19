#Admin and model imports
from django.contrib import admin
from .models import Ailment, AddProduct, AddPromotion, AppUser, FavouriteSelection
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from .resources import AddProductResource, AddPromotionResource, AddAilmentResource
from .resources import AppUserResource

# Admin display for AddProduct model including Summernote and Import/Export functionalities
@admin.register(AddProduct)
class AddProductAdmin(SummernoteModelAdmin, ImportExportModelAdmin):
    summernote_fields = ('description',)
    resource_class = AddProductResource
    list_filter = ('name', 'ailments', 'added_on',)
    search_fields = ('name', 'ailments',)
    list_display = ('name', 'price',)

# Admin display for AddPromotion model including Summernote and Import/Export functionalities
@admin.register(AddPromotion)
class AddPromotionAdmin(SummernoteModelAdmin, ImportExportModelAdmin):
    summernote_fields = ('description',)
    resource_class = AddPromotionResource
    list_filter = ('name', 'expires_on',)
    list_display = ('name', 'expires_on',)

#Admin display for Ailment model including Import/Export functionality
@admin.register(Ailment)
class Ailment(ImportExportModelAdmin):
    resource_class = AddAilmentResource
    search_fields = ('name',)

# Admin interface for AppUser model, including Import/Export functionality and customized interactions and actions
@admin.register(AppUser)
class AppUser(ImportExportModelAdmin):
    resource_class = AppUserResource
    list_filter = ('first_name', 'last_name', 'email', 'approved')
    search_fields = ('first_name', 'last_name', 'email', 'approved')
    list_display = ('first_name', 'last_name', 'email',
                    'phone_number', 'request_date', 'approved')
    actions = ['approve_user', 'remove_user',]

    def approve_user(self, request, queryset):
        queryset.update(approved=True)
        
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request):
        return False
        
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('first_name', 'last_name', 'email', 'phone_number', 'join_team', 
                    'i_want_to_know_more_about_the_products')
        else:
            return ()
        
    #Retrieves default form fields
    #converts fields into a list to allow modifications
    #checks if username is present and removes it
    #Took inspiration from StackOverflow on how to exclude fieldset    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            fieldsets = list(fieldsets)
            for fieldset in fieldsets:
                if 'username' in fieldset[1]['fields']:
                    fieldset[1]['fields'] = tuple(
                        field for field in fieldset[1]['fields'] if field != 'username'
                    )
            return tuple(fieldsets)
        return fieldsets
        
# Admin display for FavouriteSelection model
@admin.register(FavouriteSelection)
class FavouriteSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'favourite_date', 'is_favorite')
    list_filter = ('user', 'product', 'favourite_date')