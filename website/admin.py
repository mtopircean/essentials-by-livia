from django.contrib import admin
from .models import Ailment, AddProduct, AddPromotion, AppUser, FavouriteSelection
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from .resources import AddProductResource, AddPromotionResource
from .resources import AppUserResource


@admin.register(AddProduct)
class AddProductAdmin(SummernoteModelAdmin, ImportExportModelAdmin):
    summernote_fields = ('description',)
    resource_class = AddProductResource
    list_filter = ('name', 'ailments', 'added_on',)
    search_fields = ('name', 'ailments',)
    list_display = ('name', 'price',)


@admin.register(AddPromotion)
class AddPromotionAdmin(SummernoteModelAdmin, ImportExportModelAdmin):
    summernote_fields = ('description',)
    resource_class = AddPromotionResource
    list_filter = ('name', 'expires_on',)
    list_display = ('name', 'expires_on',)


@admin.register(Ailment)
class Ailment(ImportExportModelAdmin):
    resource_class = AddPromotionResource
    search_fields = ('name',)


@admin.register(AppUser)
class AppUser(ImportExportModelAdmin):
    resource_class = AppUserResource
    list_filter = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email',)
    list_display = ('first_name', 'last_name', 'email',
                    'phone_number', 'request_date',)
    actions = ['approve_user', 'remove_user',]

    def approve_user(self, request, queryset):
        queryset.update(approved=True)

    def remove_user(self, request, queryset):
        queryset.update(approved=False)
        

@admin.register(FavouriteSelection)
class FavouriteSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'favourite_date')
    list_filter = ('user', 'product', 'favourite_date')
