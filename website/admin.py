from django.contrib import admin
from .models import Ailment, AddProduct, AddPromotion
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from .resources import AddProductResource, AddPromotionResource


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
