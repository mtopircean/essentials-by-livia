from django.contrib import admin
from .models import Ailment, AddProduct, AddPromotion
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from .resources import AddProductResource, AddPromotionResource


@admin.register(AddProduct)
class AddProductAdmin(SummernoteModelAdmin, ImportExportModelAdmin):
    summernote_fields = ('description')
    resource_class = AddProductResource

@admin.register(AddPromotion)
class AddPromotionAdmin(SummernoteModelAdmin, ImportExportModelAdmin):
    summernote_fields = ('description')
    resource_class = AddPromotionResource


@admin.register(Ailment)
class Ailment(ImportExportModelAdmin):
    resource_class = AddPromotionResource
